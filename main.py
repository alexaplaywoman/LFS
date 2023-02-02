import cmd2
import os 
#import shutil
import getpass
import socket
import re
#from os import system 

class ShellLFS(cmd2.Cmd):
    def __init__(self):
        super().__init__()
        username = getpass.getuser()
        homedir = os.getcwd()
        hostname = socket.gethostname() #nombre del UNIX
        self.default_to_shell = True #use default shell commands
        self.prompt = f"{username}@{hostname}:{homedir}$"
        self.poutput("Shell Gonzalez-Ortiz")
        #cmd2.Cmd._init_(self)
    
        
    def do_creardir (self, frase):
        space = " "
        if bool(re.search(space,frase)):
            for i in re.split(space,frase):
                os.mkdir(i)
        else:
            os.mkdir(frase)


    def do_printDir(self,dirPATH):
        cwd=os.getcwd()
        self.poutput(cwd) #genera una salida

    def do_hello(self,statement):
        self.poutput(statement.arg_list)




if __name__ == '_main_':
    import sys
    c = ShellLFS()
    sys.exit(c.cmdloop())
