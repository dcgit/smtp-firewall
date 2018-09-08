import socket
import re


HOST = ''                 # Symbolic name meaning the local host
PORT = 25              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connected by', addr
IS_READING_DATA_SECTION = False
EMAILS = []
RCPT_EMAIL_RE = re.compile("^rcpt to\:\s+(.*)$")
PREVIOUS_WAS_BLANK = False

while 1:
    data = conn.recv(1024)
    if not data: break
    print(data)
    if PREVIOUS_WAS_BLANK and re.search('^\.$',data):
        print '---END OF TRANSMISSION---'
	print EMAILS
	EMAILS = []
        IS_READING_DATA_SECTION = False
    elif IS_READING_DATA_SECTION==True:
	#separate ifs for when data section is sent in one transmission
        if re.search('^from\:',data,flags=re.IGNORECASE|re.MULTILINE):
            print 'FOUND FROM'
        if re.search('^to\:',data,flags=re.IGNORECASE|re.MULTILINE):
            print 'FOUND TO'
        if re.search('^cc\:',data,flags=re.IGNORECASE|re.MULTILINE):
            print 'FOUND CC'
        if re.search('^subject\:',data,flags=re.IGNORECASE|re.MULTILINE):
            print 'FOUND SUBJECT'
    else:
        if re.search('^mail from\:',data,flags=re.IGNORECASE):
            print 'FOUND FROM'
        elif re.search('^rcpt to\:',data,flags=re.IGNORECASE):
            print 'FOUND RCPT_TO HEADER'
            matches = RCPT_EMAIL_RE.search(data)
            if matches:
		#check this for commadelimited list and "name" <email> notation
                EMAILS.append(matches.group(1))
        elif re.search('^DATA$',data,flags=re.IGNORECASE):
            print 'FOUND DATA HEADER. Listening for content...'    
    	    IS_READING_DATA_SECTION = True
    if re.search('^$',data):
	PREVIOUS_WAS_BLANK=True
	print 'found blank'
    else:
	PREVIOUS_WAS_BLANK=False



    
    


