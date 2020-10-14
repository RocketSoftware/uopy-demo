******************************************************************************
*
*   Header file for SSL BASIC programs
*
*	Module	%M%	Version	%I% 	Date	%H%
*
*	Rocket Software Confidential
*	OCO Source Materials
*	Copyright Rocket Software, Inc.  2003-2014
*
*******************************************************************************
*
*       Maintenence log - insert most recent change descriptions at top
*
*       Date.... GTAR# WHO Description.........................................
*       10/13/14 UNV-18961,UDT-12546 CUI added TLSv1.1/1.2
*	12/17/13 UNV-5146  CUI supported PKCS#12. PKCS#7 future possible.
*	06/12/12 UNV-12457 CUI added SHA224 as well
*	05/01/13 UNV-12457 CUI added new digest algorithms in OpenSSL 1.0.1c.
*	07/15/09 40336 CUI added new KEY_DERIVE codes and BASE64A. Make this
*		file part of distribution for UD (it is already in UV).
*	01/20/09 11569 CUI added SSL_URLENCODE
*	03/03/03       CUI added CertPath rule defines.
*	01/30/03       CUI initial creation.
*
*****************************************************************************

* SSL versions 
EQU SSL_SSLV2		TO	"SSLv2"
EQU SSL_SSLV3		TO	"SSLv3"
EQU SSL_TLSV1		TO	"TLSv1"
EQU SSL_TLSV11		TO	"TLSv1.1"
EQU SSL_TLSV12		TO	"TLSv1.2"
EQU SSL_TLSV2		TO	"TLSv2"	; *currently not supported

* SSL certificate type
EQU SSL_CERT_SELF	TO	1
EQU SSL_CERT_CA		TO	2
EQU SSL_CERT_CRL	TO	3

* SSL file format
EQU SSL_FMT_PEM		TO	1
EQU SSL_FMT_DER		TO	2
EQU SSL_FMT_P12		TO	3
EQU SSL_FMT_P7		TO	4	; *currently not supported

* SSL key algorithm
EQU SSL_KEY_RSA		TO	1
EQU SSL_KEY_DSA		TO	2

* SSL SCR property intended usage
EQU SSL_SERVER		TO	1
EQU SSL_CLIENT		TO	2

* SSL authentication rules
EQU SSL_RULE_PEER_NAME	TO	"PeerName"
EQU SSL_RULE_STRENGTH	TO	"VerificationStrength"
EQU SSL_RULE_CERTPATH	TO	"CertificatePath"
EQU SSL_CERTPATH_DEFAULT TO	1
EQU SSL_CERTPATH_RELATIVE TO	2
EQU SSL_CERTPATH_PATH	TO	3
EQU SSL_CERTPATH_ENV	TO	4

* SSL file location
EQU SSL_LOC_STRING	TO	1
EQU SSL_LOC_FILE	TO	2

* SSL client authentication
EQU SSL_CLIENT_AUTH	TO	1
EQU SSL_NO_CLIENT_AUTH	TO	0

* SSL message digest algorithm
EQU SSL_DIGEST_MD5	TO	1
EQU SSL_DIGEST_SHA1	TO	2
EQU SSL_DIGEST_SHA224	TO	3
EQU SSL_DIGEST_SHA256	TO	4
EQU SSL_DIGEST_SHA384	TO	5
EQU SSL_DIGEST_SHA512	TO	6

* SSL certificate generation
EQU SSL_CERT_SELF_SIGN	TO	1
EQU SSL_CERT_CA_SIGN	TO	2
EQU SSL_CERT_LEAF_SIGN 	TO	3

* SSL key-cert validation
EQU SSL_VALIDATE	TO	1
EQU SSL_NO_VALIDATE	TO	0

* SSL key action
EQU SSL_KEY_ACTUAL		TO 	1
EQU SSL_KEY_DERIVE		TO	2
EQU SSL_KEY_ACTUAL_OPENSSL	TO	3
EQU SSL_KEY_ACTUAL_COMPAT	TO	3
EQU SSL_KEY_DERIVE_MD5		TO	4
EQU SSL_KEY_DERIVE_SHA1		TO	5
EQU SSL_KEY_DERIVE_MD2		TO	6
EQU SSL_KEY_DERIVE_MDC2		TO	7
EQU SSL_KEY_DERIVE_RMD160	TO	8
EQU SSL_KEY_DERIVE_SHA		TO	9
EQU SSL_KEY_DERIVE_SHA224	TO	10
EQU SSL_KEY_DERIVE_SHA256	TO	11
EQU SSL_KEY_DERIVE_SHA384	TO	12
EQU SSL_KEY_DERIVE_SHA512	TO	13

* SSL encode algorithm
EQU SSL_BASE64		TO	"BASE64"
EQU SSL_BASE64_ONELINE	TO	"BASE64A"
EQU SSL_URLENCODE	TO	"URLENCODE"

* Cryptographic functions
EQU SSL_ENCODE		TO	1
EQU SSL_DECODE		TO	2

EQU SSL_ENCRYPT		TO	1
EQU SSL_ENCRYPT_ENCODE	TO	2
EQU SSL_DECRYPT		TO	3
EQU SSL_DECODE_DECRYPT	TO	4
* The following are for one-line base64 encode and decode
EQU SSL_ENCRYPT_ENCODE_A	TO	5
EQU SSL_DECODE_DECRYPT_A	TO	6

EQU SSL_ENCRYPT_NOPAD		TO	11
EQU SSL_ENCRYPT_ENCODE_NOPAD	TO	12
EQU SSL_DECRYPT_NOPAD		TO	13
EQU SSL_DECODE_DECRYPT_NOPAD	TO	14
* The following are for one-line base64 encode and decode
EQU SSL_ENCRYPT_ENCODE_A_NOPAD	TO	15
EQU SSL_DECODE_DECRYPT_A_NOPAD	TO	16

* Signature algorithms
EQU SSL_DIGEST_ONLY	TO	0
EQU SSL_RSA_SIGN	TO	1
EQU SSL_RSA_VERIFY	TO	2
EQU SSL_DSA_SIGN	TO	3
EQU SSL_DSA_VERIFY	TO	4

* SSL function return status
EQU SSL_SUCCESS		TO	0

