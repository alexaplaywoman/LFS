import pathlib
from posixpath import splitdrive
import subprocess
from datetime import datetime
import cmd2
import os 
import shutil
import getpass
import socket
import re
import logging
import datetime
from pathlib import Path
from os import path, system
from cmd2 import Cmd2ArgumentParser, with_argparser
import psutil
from datetime import datetime
import hashlib
import base64
import ftplib
import string
import time

import sys
import pwd
import crypt

OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
WHITE = '\033[37m'
MAGENTA='\033[35m'
HEADER = '\033[95m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

#!/usr/bin/env python
"""A simple shell application."""
class shellLFS(cmd2.Cmd):
    def __init__(self):
        super().__init__()
        username = getpass.getuser() #user 
        homedir = os.getcwd() #cwd
        hostname = socket.gethostname() #hostname
      #  self.colors = mutilities.colors()
        
        self.default_to_shell = True #use default shell commands
        self.prompt =f"{username}@{hostname}:{homedir}$"
        self.maxrepeats = 3
        self.poutput("\nSHELL ORTIZ")


###4.1. Copiar (no puede ser una llamada a sistema a la función cp) - copiar
    def do_copiar(self, phrase):
        space = " "
        new_arr = [i for i in phrase.split() if not space in i] #coloco cada palabra en un indice
        dst_path1 = path.abspath(new_arr[-1])
        open(new_arr[-1],'w')

        for file in range(len(new_arr)-1) : #recorre los elementos 
            open(new_arr[file],'a')
             #el destino siempre va a ser el ultimo elemento
            src_path = path.abspath(new_arr[file]) 
            if bool(path.isdir(dst_path1)): 
                dst_path = f"{dst_path1}/{new_arr[file]}"
                shutil.copy(src_path, dst_path)
            elif bool(path.isfile(dst_path1)): #si es un archivo se copia el archivo con otro nombre
                shutil.copyfile(src_path ,dst_path1) 
            
        print("Exito en la copia")

###4.2. Mover - mover
    def do_mover(self,phrase):
        space = " "
        new_arr = [i for i in phrase.split() if not space in i] #coloco cada palabra en un indice
        dst_path1 = path.abspath(new_arr[-1]) #la direccion del destino siempre va a ser el ultimo elemento

        for file in range(len(new_arr)-1) : #recorre los elementos 
            src_path = path.abspath(new_arr[file]) #la direccion original

            if bool(path.isdir(src_path)): #si es un directorio mueve cada archivo en el directorio ingresado
                for file_name in os.listdir(src_path):
                    source = f"{src_path}/{file_name}"
                    shutil.move(source, dst_path1)

            elif bool(path.isfile(src_path)): #si es un archivo, se mueve el archivo en el directorio ingresado   
                dst_path = f"{dst_path1}/{new_arr[file]}"
                shutil.move(src_path,dst_path)
        print("Exito en mover",src_path)


###4.3. Renombrar - renombrar       
    def do_renombrar(self,phrase):
        space = " "
        new_arr = [i for i in phrase.split() if not space in i]

        old = path.abspath(new_arr[0])
        old_name = Path(old).parent
        new_name = new_arr[-1]

        if os.path.isfile(new_name):
            print("The file already exists",new_name)
        else:
            # Rename the file
            source = f"{old_name}/{new_name}"
            print("este es el padre",old_name, "\n este es como se va a llamar",source)
            #os.rename(old_name, new_name)
            




### 4.5. Crear un directorio - creardir
    def do_creardir(self, phrase):
        space = " "
        if bool(re.search(space,phrase)):
            for i in re.split(space,phrase):
                os.mkdir(i)
        else:
            os.mkdir(phrase)


### 4.11. Imprimir el directorio en el que se encuentra la shell actualmente - pwd
    def do_printdir(self,c):
        name = 'printdir'
        try:
            cwd=os.getcwd()#obtener diretorio actual
            #guardarParam = (name,cwd) 
            self.poutput(cwd)#imprimir directorio actual
        except:
            print(FAIL+"Error printdir",cwd)
          #  self.logRegistroError(''.join(guardarParam))

if __name__ == '__main__':
    c = shellLFS()
    sys.exit(c.cmdloop())

