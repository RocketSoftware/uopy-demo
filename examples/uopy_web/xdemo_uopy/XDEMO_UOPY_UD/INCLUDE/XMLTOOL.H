****************************************************************************
*
*       Include file for XMAP TOOL 
*
*       Module%M%Version%I% Date%H%
*
*       IBM Confidential
*       OCO Source Materials
*       Copyright (C) IBM Corp.  2004, 2004
*
*
*************************************************************************


* COMMON VARIABLE
COMMON /XMLTOOL/ OS.TYPE, OS.SEP, UDACCOUNT, UDHOME, FXMLDIR, ACCTPATH, FBPDIR

* CONSTANT defination
EQU	TRUE	TO	1
EQU	FALSE	TO	0

* ERROR number defination
EQU	ETOOL.BADCALL		TO	1	;* BAD call
EQU	ETOOL.NODIRECTORY	TO	2	;* OS browser, cannot find dir
EQU	ETOOL.XMAPOPENFAIL	TO	3	;* Open _U2XMAP_ failed
EQU	ETOOL.XMLDIROPENFAIL	TO	4	;* Open _XML_ failed
EQU	ETOOL.NOXMAPREC		TO	5	;* intermediate file not exist
EQU	ETOOL.XMAPWRITEFAIL	TO	6	;* Write to _U2XMAP_ failed
EQU	ETOOL.NSERROR		TO	7	;* NS conflict with IngoerNS
EQU	ETOOL.XMLWRITEFAIL	TO	8	;* Write to _XML_ failed
EQU	ETOOL.WRONGACCTID	TO	9	;* Wrong acct id 
EQU	ETOOL.NODTDID		TO	10	;* DTD id is not exist
EQU	ETOOL.OPENDICTFAIL	TO	11	;* failed to open dict file
EQU	ETOOL.NODICTID		TO	12	;* failed to read dict item
EQU	ETOOL.WRONGPATH		TO	13	;* failed to logto account
EQU	ETOOL.OPENFAIL		TO	14	;* open file failed
EQU	ETOOL.READFAIL		TO	15	;* read rec failed
EQU	ETOOL.TOXMLFAIL		TO	16	;* DBtoXML failed
EQU	ETOOL.TODBFAIL		TO	17	;* XMLtoDB failed
EQU	ETOOL.FILEEXIST		TO	18	;* file is existed
EQU	ETOOL.WRITEFAIL		TO	19	;* Write to file failed
EQU	ETOOL.FILELOCKED	TO	20	;* File locked

EQU	ETOOL.NEWACCT		TO	21	;* newaccount failed
EQU	ETOOL.RMACCT		TO	22	;* remove account failed
EQU	ETOOL.WRITEDICTFAIL	TO	23	;* write dict failed
EQU	ETOOL.CREATEFAIL	TO	24	;* ceate file/path failed
EQU	ETOOL.DELRECFAIL	TO	25	;* Delete @ID fail
EQU	ETOOL.LOCKED		TO	26	;* Locked by other user
EQU	ETOOL.RECORDEXIST	TO	27	;* Record exist
EQU	ETOOL.RECORDCHANGED	TO	28	;* Record changed

*
* Optimistic locking implementation
*
EQU	ETOOL.SIG_ORIG_DATA	TO	"_#Orig#_"
EQU	ETOOL.SIG_FORCE_FLAG	TO	"_#Force#_"
EQU	ETOOL.OPT_LOCKFAIL	TO	29	;* can't apply exclusive lock
EQU	ETOOL.OPT_DATACHANGED	TO	30	;* the original data has been changed

EQU     ETOOL.DELETEFAIL        TO      101     ;* Delete rec from file failed
EQU     ETOOL.RETCODEINVALID    TO      102     ;* Invalid return code
EQU     ETOOL.GETSCHMFAILED    	TO      103     ;* Get current map schema failed
EQU     ETOOL.GETPWDFAILED    	TO      104     ;* Get password failed
EQU     ETOOL.WRITEPWDFAILED   	TO      105     ;* Write password failed
EQU     ETOOL.GETSRVINFOFAILED 	TO      106     ;* Get server information failed
EQU     ETOOL.CONNECTIONFAILED 	TO      107     ;* Connection failed
EQU	ETOOL.CLIENTINFOFAILED	TO	108	;* Get client info. failed

