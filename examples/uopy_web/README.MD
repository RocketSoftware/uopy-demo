

UOPY WEB EXAMPLES INSTALLATION

1. From the command prompt in the directory and run:

    `python uopy_web.py`
   
    If error try:
								
	`pip install -r requirements.txt`

    If still error please consult with support

2. Open a web browser and type

	`http://localhost:5000/`

	The uopy web examples login form will display
	
3. The data files for the examples are in a folder called xdemo_uopy. 

	XDEMO_DATA_UV
	
	XDEMO_DATA_UD
	
4. Move the desired account to the target database UD or UV

5. Add the account to the UD or UV account file using the EXTENSIBLE ADMIN TOOL or AE or ED

6. LOGTO the account and CATALOG BP CHART_DATA_UD or UV

    FOR UNIDATA : CATALOG BP CHART_DATA_UD
	
    FOR UNIVERSE : CATALOG BP *CHART_DATA_UV
	
7. Open a web browser and type
		
	`http://localhost:5000/`
	
	The uopy web examples login form will display.
	Fill in localhost for server
	Fill in XDEMO_DATA_UD OR UV for account
	Fill in a vaild user and password for  the database
	Select the database to connect to either unidata or universe
	submit
	
8. The uopy web examples menu (index.html) will display

9. Four examples available :
	Subroutine Example
	File Read/Write Example
	Query 1 Example
	Query 2 Example

Please view the session 3 uopy web examples recording for additional information
