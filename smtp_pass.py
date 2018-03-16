#Testing SASL authentication to Postfix SMTP with SASL back-ended by Active Directory
#This creates the password string to use with the 'AUTH PLAIN' command when connecting directly to the mail server

import base64
import getpass

uname = input("Username: ").encode()
passwd = getpass.getpass().encode()

auth_string = b'\0' + uname + b'\0' + passwd

encoded_auth = base64.b64encode(auth_string)

print(encoded_auth.decode())