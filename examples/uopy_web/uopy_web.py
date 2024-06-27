from flask import Flask, flash, request, url_for, redirect, \
    send_from_directory, flash
from flask import render_template
from wtforms import Form, TextAreaField, validators, \
    StringField, SubmitField, RadioField, SelectField
import pandas as pd
import uopy
import os

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
app.static_folder = os.path.abspath('./static/')


class Login(Form):

    server = StringField('Server:',
                       validators=[validators.DataRequired()])
    account = StringField('Account:',
                        validators=[validators.DataRequired()])
    user = StringField('User:', validators=[validators.DataRequired(),
                     validators.Length(min=6, max=35)])
    password = StringField('Password:',
                         validators=[validators.DataRequired(),
                         validators.Length(min=3, max=35)])
    dbms = RadioField('dbms', [validators.DataRequired()],
                      choices=[('udcs', 'UniData'), ('uvcs', 'UniVerse'
                      )], default='udcs')


class DisplayForm(Form):

    state = SelectField('State', choices=[('NY', 'New York'), ('CT',
                        'Connecticut'), ('NJ', 'New Jersey'), ('PA',
                        'Pennsylvania')])


class MemFile(Form):

    memberid = SelectField('Member', choices=[
        ('0855', 'Adcock Doug'),
        ('0526', 'Baildham Ehab'),
        ('0704', 'Campana Nick'),
        ('0281', 'Svoboda Kenny'),
        ('0042', 'Tanner Lance'),
        ('2053', 'Zimmerman Giora'),
        ])


class MemEdit(Form):

    lastname = StringField('LastName',
                         validators=[validators.DataRequired()])
    firstname = StringField('FirstName',
                          validators=[validators.DataRequired()])
    address1 = StringField('Address1',
                         validators=[validators.DataRequired()])
    address2 = StringField('Address2')
    city = StringField('City', validators=[validators.DataRequired()])
    statecode = StringField('State',
                          validators=[validators.DataRequired()])
    zip = StringField('Zip', validators=[validators.DataRequired()])


class MemSearch(Form):

    id = StringField('LastName', validators=[validators.DataRequired()])

@app.route('/', methods=['GET', 'POST'])
def hello():

        global user
        global password
        global dbms
        global server
        global account
        global memberid

        form = Login(request.form)
        if request.method == 'POST':
            server = request.form['server']
            account = request.form['account']
            password = request.form['password']
            user = request.form['user']
            dbms = request.form['dbms']
            print (
                server,
                ' ',
                account,
                ' ',
                user,
                ' ',
                dbms,
                )

            try:
                with uopy.connect(host=server, user=user,
                                  password=password, account=account,
                                  service=dbms):

                    cmd = uopy.Command()
                    if dbms == 'uvcs':
                        cmd.command_text = 'CT VOC RELLEVEL'
                    else:
                        cmd.command_text = 'VERSION'
                    cmd.run()
                    print(cmd.response)

                return redirect(url_for('index', path='index.html',
                                user=user))
            except uopy.UOError as  e:

                print(e.code)
                if e.code == 39129:

                    error = 'Note: The account name ' + account \
                        + ' is not defined in the ud_database file for UniData or UV.ACCOUNT for UniVerse.'

                    return render_template('login.html', form=form,
                            error=error)
                else:

                    error = \
                        'Error logging in - please recheck entries or change database option'
                    return render_template('login.html', form=form,
                            error=error)

        return render_template('login.html', form=form)


@app.route('/<path>')
def index(path):
    user = request.args.get('user')

    return render_template('index.html', user=user)


@app.route('/sales_chart')
def chart():
    try:
        with uopy.connect(host=server, user=user, password=password,
                          account=account, service=dbms):
            if dbms == 'udcs':
                sub = uopy.Subroutine('CHART_DATA_UD', 2)
            else:
                sub = uopy.Subroutine('*CHART_DATA_UV', 2)

            sub.args[0] = dbms
            sub.args[1] = ''
            sub.call()
            u2data = sub.args[1]
            values = u2data.list
            print(values)
            legend = 'Monthly Data'
            labels = [
                'January',
                'February',
                'March',
                'April',
                'May',
                'June',
                'July',
                'August',
                ]

            # values = [10, 9, 8, 7, 6, 4, 7, 8]

        return render_template('default.html', user=user,
                               content=render_template('chart.html',
                               values=values, labels=labels,
                               legend=legend))
    except uopy.UOError as e:
        flash(e.code)
        print(e.code)
    return render_template('index.html', user=user)


@app.route('/logout')
def logout():
    return redirect(url_for('hello'))


@app.route('/membystate', methods=['GET', 'POST'])
def membystate():

    form = DisplayForm(request.form)
    if request.method == 'POST':
 #       print('here at membystate')
        return render_template('default.html', user=user,
                               content=render_template('display_members.html'
                               , user=user, form=form))
    else:
        try:
            with uopy.connect(user=user, password=password,
                              host=server, account=account,
                              service=dbms):
                cmd = uopy.Command('SELECT STATES BY STATE_NAME ')
                cmd.run()
                select_list = uopy.List()
                ids = select_list.read_list()
 #               print(ids)
                if not ids:
                    flash('No results found!')
                    print('no results found')
                    error = 'no records found'
                    return redirect('/index.html')
                else:
                    with uopy.File('STATES') as mem:
                            field_list = [
                                'ID',
                                'STATE_NAME',
                                ]
                            id_list = ids
                            read_rs = mem.read_named_fields(id_list, field_list)
                            u2data = read_rs[3]
 #                           print(u2data)
 #                           MemFile.memberid.choices[0] = ids
 #                           MemFile.memberid.choices[1] = u2data
                            form.state.choices = u2data
        except uopy.UOError as e:
                    print(e.code)
                    flash(e.code)

        return render_template('default.html', user=user,
                               content=render_template('membystate.html'
                               , user=user, form=form))


@app.route('/display_members', methods=['POST'])
def display_members():
    form = DisplayForm(request.form)
    if request.method == 'POST':
        state = request.form['state']

 #   print('at display')
    print(state)
    try:
        with uopy.connect(host=server, user=user, password=password,
                      account=account, service=dbms):
            cmd = \
                uopy.Command("SELECT MEMBERS BY CITY BY LAST_NAME WITH  STATE_CODE = '"
                          + state + "'")
            cmd.run()
            select_list = uopy.List()
            ids = select_list.read_list()

            with uopy.File('MEMBERS') as mem:
                field_list = [
                    'LAST_NAME',
                    'FIRST_NAME',
                    'CITY',
                    'STATE',
                    'BIRTHDATE',
                    'GENDER',
                    ]
                id_list = ids
                read_rs = mem.read_named_fields(id_list, field_list)
                U2data = read_rs[3]

                data = pd.DataFrame(U2data, columns=[
                    'LAST_NAME',
                    'FIRST_NAME',
                    'CITY',
                    'STATE',
                    'BIRTHDATE',
                    'GENDER',
                    ])
                data.set_index(['LAST_NAME'], inplace=True)
                data.index.name = None
                females = data.loc[data.GENDER == 'F']
                males = data.loc[data.GENDER == 'M']
        return render_template('default.html', user=user,
                           content=render_template('view.html',
                           tables=[females.to_html(classes='female'),
                           males.to_html(classes='male')], titles=['na'
                           , 'Women Members in ' + state,
                           'Men Members in ' + state]))
    except uopy.UOError as e:
        flash(e.code)
        print(e.code)
    return render_template('index.html', user=user)


@app.route('/memsearch', methods=['GET', 'POST'])
def memsearch():
    form = MemSearch(request.form)
    if request.method == 'POST':
        id = request.form['id']
        print(id)
        id1 = id.upper()
        print(id1)
        with uopy.connect(host=server, user=user, password=password,
                          account=account, service=dbms):
            cmd = uopy.Command('SELECT MEMBERS WITH  LAST_NAME_SEARCH LIKE '
                               + id1 + '...')
            cmd.run()
            select_list = uopy.List()
            ids = select_list.read_list()
            print(ids)
            if not ids:
                flash('No results found!')
                print('no results found')
                error = 'no records found'
                return redirect('/memsearch.html')
            else:
                with uopy.File('MEMBERS') as mem:
                    field_list = [
                        'ID',
                        'LAST_NAME',
                        'FIRST_NAME',
                        'ADDRESS',
                        'CITY',
                        'STATE',
                        'ZIP',
                        ]
                    id_list = ids
                    read_rs = mem.read_named_fields(id_list, field_list)
                    u2data = read_rs[3]
#                    print(u2data)
                    data = pd.DataFrame(u2data, columns=[
                        'ID',
                        'LAST_NAME',
                        'FIRST_NAME',
                        'ADDRESS',
                        'CITY',
                        'STATE',
                        'ZIP',
                        ])
                    ids = data.loc[data.ID != '']
                    html = ids.to_html()
                    mylist = ids.values.tolist()
        return render_template('default.html', user=user,
                               content=render_template('results.html',
                               tables=[ids.to_html()], titles=['na',
                               'Members with Last Name like ' + id1]))
    else:
        return render_template('default.html', user=user,
                               content=render_template('memsearch.html'
                               , user=user, form=form))


@app.route('/mempick', methods=['GET', 'POST'])
def mempick():
    form = MemFile(request.form)
    if request.method == 'POST':
        memberid = request.form['memberid']
        print(memberid)
        try:
            with uopy.connect(user=user, password=password,
                              host=server, account=account,
                              service=dbms):
                with uopy.File('MEMBERS') as mem_file:
                    field_list = [
                        'LAST_NAME',
                        'FIRST_NAME',
                        'ADDRESS',
                        'CITY',
                        'STATE_CODE',
                        'ZIP',
                        ]
                    id_list = [memberid]
                    read_rs = mem_file.read_named_fields(id_list,
                            field_list)
#                    print(read_rs)
                    LastName = read_rs[3][0][0]
                    FirstName = read_rs[3][0][1]
                    Address = read_rs[3][0][2]
                    City = read_rs[3][0][3]
                    StateCode = read_rs[3][0][4]
                    Zip = read_rs[3][0][5]
                    if isinstance(Address, list):
                        Address1 = Address[0]
                        Address2 = Address[1]
                    else:
                        Address1 = Address
                        Address2 = ''

                    return redirect(url_for(
                        'memedit',
                        Memberid=memberid,
                        LastName=LastName,
                        FirstName=FirstName,
                        Address=Address,
                        Address1=Address1,
                        Address2=Address2,
                        City=City,
                        StateCode=StateCode,
                        Zip=Zip,
                        ))
        except uopy.UOError as e:
            print(e.code)
            flash(e.code)
            return render_template('default.html', user=user)
    else:
        try:
            with uopy.connect(user=user, password=password,
                              host=server, account=account,
                              service=dbms):
                cmd = uopy.Command('SELECT MEMBERS BY LAST_NAME_FIRST ')
                cmd.run()
                select_list = uopy.List()
                ids = select_list.read_list()
 #               print(ids)
                if not ids:
                    flash('No results found!')
                    print('no results found')
                    error = 'no records found'
                    return redirect('/index.html')
                else:
                    with uopy.File('MEMBERS') as mem:
                            field_list = [
                                'ID',
                                'LAST_NAME_FIRST',
                                ]
                            id_list = ids
                            read_rs = mem.read_named_fields(id_list, field_list)
                            u2data = read_rs[3]
 #                           print(u2data)
 #                           MemFile.memberid.choices[0] = ids
 #                           MemFile.memberid.choices[1] = u2data
                            form.memberid.choices = u2data
        except uopy.UOError as e:
                    print(e.code)
                    flash(e.code)
        return render_template('default.html', user=user,
                               content=render_template('memfile.html',
                               user=user, form=form))


@app.route('/memedit', methods=['GET', 'POST'])
def memedit():
    Memberid = request.args.get('Memberid')
    LastName = request.args.get('LastName')
    FirstName = request.args.get('FirstName')
    Address = request.args.get('Address')
    Address1 = request.args.get('Address1')
    Address2 = request.args.get('Address2')
    City = request.args.get('City')
    StateCode = request.args.get('StateCode')
    Zip = request.args.get('Zip')
    form = MemEdit(request.form)
    if request.method == 'POST':
        try:
            with uopy.connect(user=user, password=password,
                              host=server, account=account,
                              service=dbms):
                with uopy.File('MEMBERS') as mem_file:
                    field_list = [
                        'LAST_NAME',
                        'FIRST_NAME',
                        'ADDRESS',
                        'CITY',
                        'STATE_CODE',
                        'ZIP',
                        ]
                    id_list = [Memberid]
                    LastName = form.lastname.data
                    FirstName = form.firstname.data
                    Address1 = form.address1.data
                    Address2 = form.address2.data
                    City = form.city.data
                    StateCode = form.statecode.data
                    Zip = form.zip.data
                    if Address2 == '':
                        Address = Address1
                    else:
                        Address = [Address1, Address2]

                    field_value_list = [[
                        LastName,
                        FirstName,
                        Address,
                        City,
                        StateCode,
                        Zip,
                        ]]
                    write_rs = mem_file.write_named_fields(id_list,
                            field_list, field_value_list)
                    print(write_rs)
        except uopy.UOError as e:

            flash(e.code)

        return render_template('default.html', user=user)
    else:
        form.lastname.data = LastName
        form.firstname.data = FirstName
        form.address1.data = Address1
        form.address2.data = Address2
        form.city.data = City
        form.statecode.data = StateCode
        form.zip.data = Zip
        return render_template('default.html', user=user,
                               content=render_template('memedit.html',
                               user=user, form=form))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
