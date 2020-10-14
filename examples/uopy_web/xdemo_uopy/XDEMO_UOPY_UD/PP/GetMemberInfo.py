####################################################
# Copyright (C) Rocket Software 1993-2015
# This Python program imports a U2 module, calls a catalogued
# U2 Basic subroutine GET_MEMBERS_RECORD to receive a specific
# record from the MEMBERS file in XML format. It then uses an
# xml.etree.ElementTree module to parse the received XML string.
# Note, the XML version of the U2 record is in the
# element-centric mode.
# Parameters: first(in) - record ID; second(out) - XML string;
# third(out) - error code from subroutine; fourth(out) - error msg

import xml.etree.ElementTree as ET
import u2py
s = u2py.Subroutine("GET_MEMBERS_RECORD", 4) 
s.args[0] = "0965"
s.call()
if str(s.args[2]) != '0':
    print("Error from the subroutine:", s.args[3])
else:
    xmlstring = s.args[1] 
    print("xmlstring=", xmlstring)
    # Parse XML from the string into element 
    tree = ET.fromstring(xmlstring)
    for child in tree:
        if child.tag != 'ADDRESS_MV': 
            print(child.tag, child.text)
        else:
            print('STREET_ADDRESS', child.find('ADDRESS').text)

####################################################
