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
        home_dir = os.getcwd() #cwd
        hostname = socket.gethostname() #hostname
      #  self.colors = mutilities.colors()
        
        self.default_to_shell = True #use default shell commands
        self.prompt =f"{username}@{hostname}:{home_dir}$"
        self.maxrepeats = 3
        self.poutput("\nSHELL ORTIZ")

    
    def logregistroComandos():
        logging.basicConfig(
        format = '%(asctime)-5s %(name)-15s %(levelname)-8s %(message)s', 
        level  = logging.INFO,      # Nivel de los eventos que se registran en el logger
        filename = "logs_info.log", # Fichero en el que se escriben los logs
        filemode = "a"              # a ("append"), en cada escritura, si el archivo de logs ya existe,
                                    # se abre y añaden nuevas lineas.
        )
        if logging.getLogger('').hasHandlers():
            logging.getLogger('').handlers.clear()

    
    def do_guardar():
        import readline
        readline.write_history_file('python_history.txt')
        file = open('python_history.txt','r')
        file.close()


###4.1. Copiar (no puede ser una llamada a sistema a la función cp) - copiar
    def do_copiar(self, phrase):
        logging.info("copiar",phrase)
        space = " "
        new_arr = [i for i in phrase.split() if not space in i] #coloco cada palabra en un indice
        dst_path1 = path.abspath(new_arr[-1])                   #el destino siempre va a ser el ultimo elemento
        try:
            for file in range(len(new_arr)-1) :                 #recorre los elementos 
                if path.exists(new_arr[file]) == False:
                    open(new_arr[file],'a')
                src_path = path.abspath(new_arr[file]) 
                if bool(path.isdir(dst_path1)): 
                    dst_path = f"{dst_path1}/{new_arr[file]}"
                    shutil.copy(src_path, dst_path)
                if bool(path.isfile(dst_path1)):                 #si es un archivo se copia el archivo con otro nombre
                    open(new_arr[-1],'w') 
                    shutil.copyfile(src_path ,dst_path1) 
            print("Exito en la copia")
        except:
            print("Error al copiar")
            
        

###4.2. Mover - mover      
    def do_mover(self,phrase):
        space = " "
        new_arr = [i for i in phrase.split() if not space in i]  
        dst_path = path.abspath(new_arr[-1])                        #destino de la carpeta
        src_path = path.abspath(new_arr[0])                         #origen de la carpeta
        if path.exists(dst_path) == False: 
            raise FileNotFoundError(f"ERROR: {dst_path} no se encuentra")
        try:
            if path.samefile(src_path,dst_path) == False:           #si no son iguales 
                shutil.move(src_path,dst_path)                      #se realiza mover
                print("Exito en mover")
        except:
            print("Error. Ya existe en la carpeta")
        else:
            print("Error.No se pudo realizar la operacion mover")


###4.3. Renombrar - renombrar       
    def do_renombrar(self,phrase):
        space = " "
        new_arr = [i for i in phrase.split() if not space in i]

        old = path.abspath(new_arr[0])
        old_name = Path(old).parent                                     #adquirir en que directorio esta
        new_name = new_arr[-1]                                          #adquirir el nombre nuevo
        try:
            if os.path.isfile(new_name) or os.path.isdir(new_name):
                print("El archivo ya existe",new_name)
            else:
                # Renombrar el archivo
                new1= f"{old_name}/{new_name}" 
                new = path.abspath(new1)
                os.rename(old, new)
                print("Exito al renombrar")
        except:
            print(FAIL+"Error al renombrar")


###4.4. Listar un directorio (no puede ser una llamada a sistema a la función ls) - listar

    def do_listar(self, argument):
        if argument == "":
            cwd = os.listdir()
            print(cwd)
        elif argument != "":
            direct_arg = os.listdir(argument)
            print(direct_arg)
        else:
            print("Error al listar")


### 4.5. Crear un directorio - creardir
    def do_creardir(self, phrase):
        space = " "
        try:
            for i in re.split(space,phrase):
                os.mkdir(i)
        except:
            print("Error al crear directorio")


###4.6. Cambiar de directorio (no puede ser una llamada a sistema a la función cd) - ir
    def do_ir(self,phrase):
        dst_dir = path.abspath(phrase)
        if path.exists(dst_dir):
            os.chdir(dst_dir)
        else:
            print("No se realizo el cambio")


###4.7. Cambiar los permisos sobre un archivo o un directorio - permisos
    def do_permisos(argument):
        new_arr = [i for i in argument.split() if not " " in i]
        path = new_arr [-1]
        perm = int(new_arr [0],8)   #convertimos en valor octal los permisos
        try:
            os.chmod(os.path.abspath(path), perm)
        except Exception:
            msg = "permisos: no se puedo realizar la operacion."
            #logSystemError(msg)
            print(msg)
            return 1
        return 0


### 4.11. Imprimir el directorio en el que se encuentra la shell actualmente - pwd
    def do_printdir(self,c):
        name = 'printdir'
        try:
            cwd=os.getcwd()             #obtener diretorio actual
            #guardarParam = (name,cwd) 
            self.poutput(cwd)           #imprimir directorio actual
        except:
            print(FAIL+"Error printdir",cwd)
          #  self.logRegistroError(''.join(guardarParam))


###4.13. Buscar un string en un archivo - grep
    def do_sgrep(self,argument):
        argnt = [i for i in argument.split() if not " " in i]
        file_one = open(f"{argnt[-1]}.txt", "r")
        if path.exists(f"{argnt[-1]}.txt"):
            line_num = 0
            flag = False
            for line in file_one:
                line_num += 1 
                if re.search(argnt[0], line):
                    print(f"Se encontro en la linea {line_num} {line}")
                    flag =  True
            if flag == False:
                print("No se encontro en el archivo",argnt[0])
        else:
            print("Error no se encontro archivo",argnt[0])      

if __name__ == '__main__':
    c = shellLFS()
    sys.exit(c.cmdloop())

