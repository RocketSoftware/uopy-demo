"""
This uopycommand.py program is working with UniData 8.2.1 and UniVerse 11.3.1 against XDEMO account.
Version: 1.0.0 [Q01597]
Date: 7/31/2020

Functions:

- Open a UO connection using uopy.py driver
- Menu / Button state handling (NORMAL / DISABLED)
- Put the Connect time (seconds) in the "Connect/cmd time (sec)" field
- Get the UniData or UniVerse information in the result field 
- Run a UO Command (Commdn Button)
- Put the response in the result field with scrolled bar
- U2 Error handling
- Load / Save configuration file - connect information
- Use tkinter grid mode with menu option
- Use the Esc key or Exit button to close the Help Window (tkinter pack mode)

"""

glversion = "1.0.0"

###########
# Imports #
###########
import sys
import types
import tkinter as tk
from tkinter import *
from tkinter import simpledialog
import datetime
from datetime import date
from tkinter import messagebox
import configparser

import uopy
import time
import base64

###############################################
# Load the UOMembersDemo.cfg configuration file #
###############################################

config = configparser.ConfigParser()
serverx = "localhost"
account_path = "XDEMO"
userx = "xxx"
passwordx = "xxx"
servicex = "udcs"
dbmstype = "unidata"
cmdx = ""

try:
   
    config.read('uopycommand.cfg')
    default_setting = config['appSettings']
    try:
        serverx = default_setting['server']
    except:
        pass
    try:
        servicex = default_setting['service']
    except:
        servicex = ""
        pass
    try:
        dbmstype = default_setting['dbmstype'].lower()
    except:
        dbmstype = ""
        pass
    try:
        account_path = default_setting['account_path']
    except:
        pass
    try:
        userx = default_setting['username']
    except:
        pass
    try:
        passwordx = default_setting['password']
        if len(passwordx) > 3 and passwordx[0:3] == "!@#":
            passwordx = base64.b64decode(passwordx[3:].encode("utf-8")).decode("utf-8")
    except:
        pass
    try:
        cmdx = default_setting['cmd']
    except:
        pass
except:
    pass

###############################
# Find the XDEMO account path #
###############################
import os
program_path = os.getcwd()

# Windows or UNIX environment
if program_path.find(":\\"):
    windows = True
else:
    windows = False

##from uopy import UOError, EXEC_MORE_OUTPUT, SequentialFile, Command

from uopy import Session, File, List, DynArray
from uopy import Command
from uopy import EXEC_COMPLETE, EXEC_REPLY, EXEC_MORE_OUTPUT
from uopy import Subroutine
from uopy import UOError
#from uopy import uopy.connectError, FileError, UniListError
#from uopy import UniObjectsConsts

##################
# GUI Properties #
##################
root = Tk()
root.configure(background = "White")
root.title("[Q01597] uopycommand tool (ver: " + glversion + ")")
root.columnconfigure(0, minsize = 120)
root.columnconfigure(1, minsize = 120)
root.columnconfigure(2, minsize = 120)
root.columnconfigure(3, minsize = 120)
root.columnconfigure(4, minsize = 120)

root.resizable(width=FALSE, height=FALSE)
# root.geometry('{}x{}'.format(<widthpixels>, <heightpixels>))
# root.geometry("625x545+0+0")
w = 650
#h = 545
h = 445

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

#####################
# Declare Variables #
#####################
serverText = StringVar()
servicenameText = StringVar()
accountText = StringVar()
titleText = StringVar()
passwordText = StringVar()
userText = StringVar()
cmdText = StringVar()
timeText = StringVar()

dboptionInt = IntVar()
dboptioni = 1
session_open = False

if dbmstype == "unidata":
    dboptioni = 1
else:
    dboptioni = 2

############
# Exit GUI #
############
def quitgui():
    root.destroy()

##########################
# Clean all entry fields #
##########################
def clean_fields():
    accountText.set("")
    #servicenameText.set("")
    userText.set("")
    passwordText.set("")
	
    button_Connect.config(state=tk.NORMAL)
    button_Command.config(state=tk.DISABLED)
    button_Disconnect.config(state=tk.DISABLED)
    
    menu1.entryconfig(1, state=tk.NORMAL)    
    menu1.entryconfig(2, state=tk.DISABLED)
    menu1.entryconfig(3, state=tk.DISABLED)
	
    entry_server.configure(state='normal')
    data_account.configure(state='normal')
    data_user.configure(state='normal')
    data_password.configure(state='normal')
    data_servicename.configure(state='normal')
	
#############################
# Search button (Member ID) #
#############################
def connect():
    #Global variables we need for connect
    global Session1
    
    label_message['text']=""
    result1.delete("1.0","end")

    serverx = serverText.get()
    servicex = servicenameText.get()
    account_path = accountText.get()
    userx = userText.get()
    passwordx = passwordText.get()
	
    try:
        start_time = time.time()
        Session1 = uopy.connect(host=serverx,user=userx, password=passwordx, account=account_path, service=servicex)
        connect_time = time.time() - start_time
        timeText.set(connect_time)
        session_open = True
        #
        cmd = Command(session=Session1)
        if dboptionInt.get() == 1:
            cmd.command_text = "VERSION"
        else:
            cmd.command_text = "CT VOC RELLEVEL"
        cmd.run()
        result1.insert(END,cmd.response)
        #		
    except UOError as e:
        if e.code == 39129:
            errorx = "Note: The account name " + account_path + " is not defined in the ud_database file for UniData or UV.ACCOUNT for UniVerse."
            result1.insert(END, errorx)
        #exit()
        label_message['text'] = e
        return
	
    button_Connect.config(state=tk.DISABLED)
    button_Command.config(state=tk.NORMAL)
    button_Disconnect.config(state=tk.NORMAL)
    
    menu1.entryconfig(1, state=tk.DISABLED)    
    menu1.entryconfig(2, state=tk.NORMAL)
    menu1.entryconfig(3, state=tk.NORMAL)
	
    entry_server.configure(state='disabled')
    data_account.configure(state='disabled')
    data_user.configure(state='disabled')
    data_password.configure(state='disabled')
    data_servicename.configure(state='disabled')
	
    optud_Button.config(state=tk.DISABLED)
    optuv_Button.config(state=tk.DISABLED)
    
    label_message['text'] = "Server " + serverx + " has been connected successfully!"
    #label_message.config(fg = "black")

################
# Disconnect   #
################
def disconnect():
    global Session1

    label_message['text']=""
    timeText.set('')
    result1.delete("1.0","end")

    try:
        Session1.close()
        #Session1 = nothing
        session_open = False
    except UOError as e:
        print(e)
        #exit()
        label_message['text'] = e
        return
	
    button_Connect.config(state=tk.NORMAL)
    button_Command.config(state=tk.DISABLED)
    button_Disconnect.config(state=tk.DISABLED)
    
    menu1.entryconfig(1, state=tk.NORMAL)    
    menu1.entryconfig(2, state=tk.DISABLED)
    menu1.entryconfig(3, state=tk.DISABLED)
	
    entry_server.configure(state='normal')
    data_account.configure(state='normal')
    data_user.configure(state='normal')
    data_password.configure(state='normal')
    data_servicename.configure(state='normal')
	
    optud_Button.config(state=tk.NORMAL)
    optuv_Button.config(state=tk.NORMAL)

    # messageWindow()
    label_message['text'] = "Server " + serverx + " has been disconnected successfully!"
    #label_message.config(fg = "black")

################
# command      #
################
def command():
    global Session1

    label_message['text']=""
    result1.delete("1.0","end")
    cmdx = cmdText.get()
    if len(cmdx) == 0:
        label_message['text'] = "Please entry a U2 command"
        return

    try:
        cmd = Command(session=Session1)
		#cmd.buffer_size = 30
        #cmd.buffer_size = 2048
        cmd.command_text = cmdx
        start_time = time.time()
        cmd.run()
        #uopy.EXEC_COMPLETE:0, uopy.EXEC_REPLY:1, EXEC_MORE_OUTPUT:2
		#while cmd.status = uopy.EXEC_COMPLETE:
        done = False
        i = 1
        while done != True:
            #print(cmd.status)
            i = i + 1
            if cmd.status == EXEC_COMPLETE:
                result1.insert(END, cmd.response)
                done = True
            elif cmd.status == EXEC_MORE_OUTPUT:
                result1.insert(END, cmd.response)
                cmd.next_response()
                """
                if i > 10:
                    done = True
					# clean the more buffer
                    while cmd.status == EXEC_MORE_OUTPUT:
                        cmd.next_response()
                """
            elif cmd.status == EXEC_REPLY:
                res = cmd.response
                replyx = simpledialog.askstring(title="Command Input", prompt=res)
                cmd.reply(replyx)
                #break
            else:
                break
        #
        connect_time = time.time() - start_time
        timeText.set(connect_time)
    except Exception as e:
        label_message['text'] = e
        return
	
    # messageWindow()
    label_message['text'] = "Run the command successfully!"
    #label_message.config(fg = "black")
	
def keyid_enter(event):
    connect()
	
def command_enter(event):
    command()
	
def messageWindow1():
    win = Toplevel()
    win.title('Command Result')
    win.config(background= "white")
    win.geometry("240x100")
    message = "command test."
    Label(win, text=message, bg = "white", fg = "blue", font = ("Verdana", 10)).pack(pady = 10)
    Button(win, text='Ok', command=win.destroy, bg = "white", fg = "blue", font = ("Verdana", 10), width = 10).pack(pady = 10)
    
def switchdb():
    if dboptionInt.get() == 1:
        servicenameText.set("udcs")
    else:
        servicenameText.set("uvcs")
	
########
# Quit #
########
def quittest():
    global Session1
    #Session.disconnect()
    # Session1.close()
    if session_open:
        Session1.close()
    try:
        # Change back to the program path and create the UOMembersDemo.cfg configuration file in that folder
        serverx = serverText.get()
        servicex = servicenameText.get()
        account_path = accountText.get()
        userx = userText.get()
        passwordx = passwordText.get()
        cmdx = cmdText.get()
		
        os.chdir(program_path)
        config = configparser.ConfigParser()
        config['appSettings'] = {}
        config['appSettings']['server'] = serverx
        if len(servicex) > 0:
            config['appSettings']['service'] = servicex
        #if len(dbmstype) > 0:
        #    config['appSettings']['dbmstype'] = dbmstype
        config['appSettings']['account_path'] = account_path
        config['appSettings']['username'] = userx
        if len(passwordx) > 3:
            passwordx = "!@#" + base64.b64encode(passwordx.encode("utf-8")).decode("utf-8")
        config['appSettings']['password'] = passwordx
        config['appSettings']['cmd'] = cmdx
		
        if dboptionInt.get() == 1:
            config['appSettings']['dbmstype'] = "unidata"
        else:
            config['appSettings']['dbmstype'] = "universe"		
            
        with open('uopycommand.cfg', 'w') as configfile:
            config.write(configfile)
    except:
        pass
    
    
    root.destroy()
    #Exits the GUI window

########
# Help #
########
def help_function():
    # Opens a help window
    menu2.entryconfig(1, state=tk.DISABLED)
    h = help_Popup()
    
    # Waits until help_Popup closes before continuing
    # root.wait_window(h)

class help_Popup(object):
    def __init__(self):
        # Create the popup window with set configurations
        top=self.top=Toplevel()
        top.configure(background = "white")
        #top.geometry("1300x340")
        top.geometry("1000x300")

        top.title("MV uopycommand - Help")

        top.protocol("WM_DELETE_WINDOW", top.iconify)
        top.bind('<Escape>', lambda e: top.destroy())
        
        self.S = Scrollbar(top)
        self.S.pack(side=RIGHT, fill=Y)
        
        self.T = Text(top, height=12, width=90)
        self.T.pack(side=LEFT, fill=Y)
        self.S.config(command=self.T.yview)
        self.T.config(yscrollcommand=self.S.set)

        quote = """Functions:
        - Open a UO connection based on the defined service name using uopy.py driver
        - Put the Connect time (seconds) in the "Connect/cmd time (sec)" field
        - Get the UniData or UniVerse information in the result field 
        - Run a UO Command (Commdn Button)
	- Put the response in the result field with scrolled bar
	- Menu / Button state handling (NORMAL / DISABLED)
	- UOPY Error handling
	- Load / Save configuration file - last update command
        - Use tkinter grid mode with menu option
        - Use the Esc key or Exit button to close the Help Window (tkinter pack mode)"""
        self.T.insert(END, quote)
        
        self.B=Button(top,text='Exit',command=self.cleanup, fg = "blue", bg = "white", font = ("Verdana", 10), width = 16)
        self.B.pack(side=BOTTOM)
        return
 
    def cleanup(self):
        menu2.entryconfig(1, state=tk.NORMAL)
        self.top.destroy()

class ScrolledText(Text):
    def __init__(self, master=None, **kw):
        self.frame = Frame(master)
        self.vbar = Scrollbar(self.frame)
        self.vbar.pack(side=RIGHT, fill=Y)

        kw.update({'yscrollcommand': self.vbar.set})
        Text.__init__(self, self.frame, **kw)
        self.pack(side=LEFT, fill=BOTH, expand=True)
        self.vbar['command'] = self.yview

        # Copy geometry methods of self.frame without overriding Text
        # methods -- hack!
        text_meths = vars(Text).keys()
        methods = vars(Pack).keys() | vars(Grid).keys() | vars(Place).keys()
        methods = methods.difference(text_meths)

        for m in methods:
            if m[0] != '_' and m != 'config' and m != 'configure':
                setattr(self, m, getattr(self.frame, m))

    def __str__(self):
        return str(self.frame)


# An optional step to create the Rocket label and the blue background
# Only GIF or PNG images are accepted
# canvas
#canvas1 = Canvas(root, height = 80, bg = "blue", width = 730)
canvas1 = Canvas(root, width = 650, height = 80, bg = "cyan")
canvas1.grid(row = 0, column = 0, columnspan = 10, padx = 0, sticky=W)
# image1 = PhotoImage(file = "logo.gif")
# label_image1 = Label(root, image = image1, height=100)
# label_image1.grid(row = 0,column=0, columnspan = 5, padx = 50, sticky=W)
label_rocket = Label(text = "Rocket MV UO Python - U2 Command", fg = "blue", bg = "white", font = ("Verdana", 20))
label_rocket.grid(row = 0,column=0, columnspan = 5, padx = 50, sticky=W)

# This is how you create the menu bar in TKinter
# The only relevant option was Quit for me but you can add anything other function you want

menubar = Menu(root, tearoff= 0)
menu1 = Menu(menubar)
menu1.add_command(label = "Connect", command = connect)
menu1.add_command(label = "Command", command = command)
menu1.add_command(label = "Dsiconnect", command = disconnect)
menu1.add_separator()
menu1.add_command(label = "Quit", command = quittest)
menu1.entryconfig(2, state=tk.DISABLED)
menu1.entryconfig(3, state=tk.DISABLED)
menubar.add_cascade(label = "File", menu = menu1)

menu2 = Menu(menubar)
menu2.add_command(label = "Help", command = help_function)
menubar.add_cascade(label = "Help", menu = menu2)

root.config(menu = menubar)

# input key id value and enter

label_server = Label(text = "Server:", fg = "blue", bg = "white", font = "Verdana")
label_server.grid(row = 5, column = 0, pady = (10,5), columnspan = 1, sticky = W)
entry_server = Entry(root, textvariable = serverText, font = "Verdana", width = 14)
entry_server.grid(row = 5, column = 1, pady = (10,5), sticky = W)

#entry_server.bind('<Return>', keyid_enter)

if serverx == "":
    serverText.set('localhost')
else:
    serverText.set(serverx)

#labelframe = tk.LabelFrame(padx=15, pady=10, text="DBMS Type:")
#labelframe.pack(fill="both", expand="yes")
#labelframe.grid(row = 6, column = 2, pady = 5, columnspan = 2, sticky = W)

top_frame = LabelFrame(root, bg='light blue', width = 300, height=40, pady=2, text="-----------------DBMS Type:").grid(row=5, column = 2, columnspan=2)
#dbms_label = Label(top_frame, text='DBMS Type:', fg = "black", bg = "white", font = ("Verdana", 10))
#dbms_label.grid(row=6, column = 2, columnspan=1)

optud_Button = Radiobutton(top_frame, text = "UniData", font = ("Verdana", 8), bg='light blue', variable = dboptionInt, value = 1, command=switchdb)
optud_Button.grid(row=5, column = 2, padx = 20, sticky=W)
optuv_Button = Radiobutton(top_frame, text = "UniVerse", font = ("Verdana", 8), bg='light blue', variable = dboptionInt, value = 2, command=switchdb)
optuv_Button.grid(row=5, column = 3, padx = 20, sticky=W)
dboptionInt.set(dboptioni)

if servicex == "":
    if dboptioni == 1:
        servicenameText.set("udcs")
    else:
        servicenameText.set("uvcs")
else:
    servicenameText.set(servicex)

label_account = Label(text = "Account:", fg = "blue", bg = "white", font = ("Verdana", 10))
label_account.grid(row = 6, column = 0, pady = 5, sticky = W)
data_account = Entry(root, textvariable = accountText, bg = "white", font = ("Verdana", 10), width = 18)
data_account.grid(row = 6, column = 1, pady = 5, sticky = W)
accountText.set(account_path)

label_servicename = Label(text = "Service Name:", fg = "blue", bg = "white", font = ("Verdana", 10))
label_servicename.grid(row = 6, column = 2, pady = 5, sticky = W)
data_servicename = Entry(root, textvariable = servicenameText, bg = "white", font = ("Verdana", 10), width = 18)
data_servicename.grid(row = 6, column = 3,  pady = 5, sticky = W)

label_user = Label(text = "User:", fg = "blue", bg = "white", font = ("Verdana", 10))
label_user.grid(row = 11, column = 0, pady = 5, sticky = W)
data_user = Entry(root, textvariable = userText, bg = "white", font = ("Verdana", 10), width = 18)
data_user.grid(row = 11, column = 1, pady = 5, sticky = W)
userText.set(userx)

label_password = Label(text = "Password:", fg = "blue", bg = "white", font = ("Verdana", 10))
label_password.grid(row = 12, column = 0, pady = 5, sticky = W)
data_password = Entry(root, textvariable = passwordText, show='*', bg = "white", font = ("Verdana", 10), width = 18)
data_password.grid(row = 12, column = 1, pady = 5, sticky = W)
passwordText.set(passwordx)

data_password.bind('<Return>', keyid_enter)

label_time = Label(text = "Connect/cmd time(sec):", fg = "blue", bg = "white", font = ("Verdana", 10))
label_time.grid(row = 12, column = 2, pady = 5, sticky = W)
data_time = Entry(root, textvariable = timeText, bg = "white", font = ("Verdana", 10), width = 18)
data_time.grid(row = 12, column = 3, pady = 5, sticky = W)
data_time.configure(state='readonly')

label_cmd = Label(text = "Command:", fg = "blue", bg = "white", font = ("Verdana", 10)).grid(row = 13, column = 0, sticky = W)
data_cmd = Entry(root, textvariable = cmdText, bg = "white", font = ("Verdana", 10), width = 60)
data_cmd.grid(row = 13, column = 1, pady = 5, columnspan = 3, sticky = W)
cmdText.set(cmdx)

data_cmd.bind('<Return>', command_enter)

# Vertical (y) Scroll Bar
#yscrollbar = Scrollbar(root)
#yscrollbar.pack(side=RIGHT, fill=Y)
#result1 = Text(root, yscrollcommand=yscrollbar.set, width = 40, height = 4, bg = "white", font = ("Verdana", 10))
label_result = Label(text = "Result:", fg = "blue", bg = "white", font = ("Verdana", 10)).grid(row = 14, column = 0, sticky = W)

#result1 = Text(root, width = 60, height = 4, bg = "white", font = ("Verdana", 10))
result1 = ScrolledText(bg='white', width = 60, height=4)
result1.grid(row = 14, column = 1, rowspan = 5, pady = (5,0), columnspan = 3, sticky = NW)

# Buttons setting

button_Connect = Button(root, text = "Connect", command = connect, fg = "blue", bg = "white", font = ("Verdana", 10), width = 18)
button_Connect.grid(row = 19, column = 0, pady = (10,10), sticky = W)

button_Command = Button(root, text = "Command", command = command, fg = "blue", bg = "white", font = ("Verdana", 10), width = 18)
button_Command.grid(row = 19, column = 1, pady = 10, sticky = NW)

button_Disconnect = Button(root, text = "Disconnect", command = disconnect, fg = "blue", bg = "white", font = ("Verdana", 10), width = 18)
button_Disconnect.grid(row = 19, column = 2, pady = 10, sticky = NW)

button_Quit = Button(root, text = "Quit", command = quittest, fg = "blue", bg = "white", font = ("Verdana", 10), width = 18)
button_Quit.grid(row = 19, column = 3, pady = 10, sticky = W)

label_message = Label(text = "", fg = "brown", bg = "white", font = ("Verdana", 10), width=60, justify=LEFT)
label_message.grid(row = 21, column = 0, columnspan = 4, padx = 0, pady = 5, sticky = W)

button_Command.config(state=tk.DISABLED)
button_Disconnect.config(state=tk.DISABLED)

label_message['text'] = "Python version: "+ str(sys.version_info[0]) + "." + str(sys.version_info[1]) + "." + str(sys.version_info[2]) 

root.mainloop()
