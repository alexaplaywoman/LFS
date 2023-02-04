from lib2to3.pytree import convert
import pathlib
from posixpath import splitdrive
import signal
import subprocess
from datetime import datetime
import cmd2
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

import grp
import os
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

    def logSystemError(self,message):
        try:
               #creamos/llamamos al log
            log = logging.getLogger('systemError')
            log.setLevel(logging.ERROR)
                #creamos el archivo donde se van a almacenar los registros
            direccion = 'var/log/shell/sistema_error.log' #agg /var para lfs
            open(direccion,'a')
            fileHandler = logging.FileHandler(direccion, mode='a')
            fileHandler.setLevel(logging.ERROR)
                #le damos el formato deseado
            formato = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s')
            fileHandler.setFormatter(formato)
                #agregamos al log
            log.addHandler(fileHandler)
                #establecemos el mensaje
            log.error(message)
                #cerramos el log
            log.removeHandler(fileHandler)
            fileHandler.flush()
            fileHandler.close()
        except:
            log.fatal('Error inesperado al agregar log')
    
    # Funcion para generar log de movimientos de usuario -> comandos.log
    def logRegistroDiario(message):
        try:
            #creamos/llamamos al log
            log = logging.getLogger('registroDiario')
            log.setLevel(logging.DEBUG)
            #creamos el archivo donde se van a almacenar los registros
            direccion1 = 'var/log/shell/comandos.log' #agg /var para lfs
            open(direccion1,'a')
            fileHandler = logging.FileHandler(direccion1, mode='a')
            fileHandler.setLevel(logging.DEBUG)
            #le damos el formato deseado
            formato = logging.Formatter('%(asctime)s : %(message)s')
            fileHandler.setFormatter(formato)
            #agregamos al log
            log.addHandler(fileHandler)
            #establecemos el mensaje
            log.debug(message)
            #cerramos el log
            log.removeHandler(fileHandler)
            fileHandler.flush()
            fileHandler.close()
        except:
            log.fatal('Error inesperado al agregar log')

    def archivoHistorial(self,message):
        try:
                #creamos el archivo donde se van a almacenar los registros
            direc = 'var/log/shell/historial.log' #agg /var para lfs
            file = open(direc,'a')
            file.write(str(message) + '\n')
            file.close()
        except Exception as f:
            print(f)
    
    def do_historial(self,arg):
        name = "historial"
        self.archivoHistorial(name)
        f = open("var/log/shell/historial.log","r")
        line_num = 0
        for line in f:
            line_num += 1 
            print(line_num,line)


    


###4.1. Copiar (no puede ser una llamada a sistema a la función cp) - copiar
   ###4.1. Copiar (no puede ser una llamada a sistema a la función cp) - copiar
    def do_copiar(self, phrase):
        name = f"copiar {phrase}"
        self.archivoHistorial(name)
        print(name)
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
        except Exception :
            msg = "copiar: Error.No se pudo realizar la copia"
            self.logSystemError(msg)
            print(msg)
            
        

###4.2. Mover - mover      
    def do_mover(self,phrase):
        name = f"mover {phrase}"
        self.archivoHistorial(name)
        print(name)
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
        except Exception :
            msg = "mover: Error.Carpeta existente"
            self.logSystemError(msg)
            print(msg)
        else:
            msg = "mover: Error.No se pudo realizar la operacion mover"
            self.logSystemError(msg)
            print(msg)

###4.3. Renombrar - renombrar       
    def do_renombrar(self,phrase):
        name = f"renombrar {phrase}"
        self.archivoHistorial(name)
        print(name)
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
        except Exception :
            msg = "renombrar: Error al renombrar"
            self.logSystemError(msg)
            print(msg)


###4.4. Listar un directorio (no puede ser una llamada a sistema a la función ls) - listar

    def do_listar(self, argument):
        name = f"listar {argument}"
        self.archivoHistorial(name)
        print(name)
        try:
            if argument == "":
                cwd = os.listdir()
                print(cwd)
            if argument != "":
                direct_arg = os.listdir(argument)
                print(direct_arg)
        except Exception :
            msg = "listar: Error al listar"
            self.logSystemError(msg)
            print(msg)


### 4.5. Crear un directorio - creardir
    def do_creardir(self, phrase):
        name = f"creardir {phrase}"
        self.archivoHistorial(name)
        print(name)
        space = " "
        try:
            for i in re.split(space,phrase):
                os.mkdir(i)
        except Exception :
            msg = "crear: Error al crear directorio"
            self.logSystemError(msg)
            print(msg)


###4.6. Cambiar de directorio (no puede ser una llamada a sistema a la función cd) - ir
    def do_ir(self,phrase):
        name = f"ir {phrase}"
        self.archivoHistorial(name)
        print(name)
        dst_dir = path.abspath(phrase)
        try:
            if path.exists(dst_dir):
                os.chdir(dst_dir)
        except Exception :
            msg = "ir: Error al cambiar de directorio"
            self.logSystemError(msg)
            print(msg)


###4.7. Cambiar los permisos sobre un archivo o un directorio - permisos
    def do_permisos(self,argument):
        name = f"permisos {argument}"
        self.archivoHistorial(name)
        print(name)
        new_arr = [i for i in argument.split() if not " " in i]
        path = new_arr [-1]
        perm = int(new_arr [0],8)   #convertimos en valor octal los permisos
        try:
            os.chmod(os.path.abspath(path), perm)
        except Exception:
            msg = "permisos: no se puedo realizar la operacion."
            self.logSystemError(msg)
            print(msg)
            

###4.8. Cambiar los propietarios sobre un archivo o un conjunto de archivos. - propietario
    def do_propietario(self,argument):
        name = f"propietario {argument}"
        self.archivoHistorial(name)
        print(name)
        new_arr = [i for i in argument.split() if not " " in i]
        p = new_arr[0].split(":")
        userID = p[0]
        group = p[1]
        dir_path = path.abspath(new_arr[1])
        uid = pwd.getpwnam(userID).pw_uid
        gid = grp.getgrnam(group).gr_gid
        try:
            os.chown(dir_path, uid, gid)
        except Exception:
            #registramos en el log -> sistema_error.log
            msg = "propietario: Error al cambiar de propietario."
            self.logSystemError(msg)
            print(msg)
            
        

### 4.11. Imprimir el directorio en el que se encuentra la shell actualmente - pwd
    def do_printdir(self,c):
        name = "printdir"
        self.archivoHistorial(name)
        print(name)
        try:
            cwd=os.getcwd()             #obtener diretorio actual
            #guardarParam = (name,cwd) 
            self.poutput(cwd)           #imprimir directorio actual
        except Exception:
            msg = "printdir: Error al imprimir directorio actual"
            self.logSystemError(msg)
            print(msg)
          


###4.13. Buscar un string en un archivo - grep
    def do_sgrep(self,argument):
        name = f"sgrep {argument}"
        self.archivoHistorial(name)
        print(name)
        argnt = [i for i in argument.split() if not " " in i]
        file_one = open(f"{argnt[-1]}.txt", "r")
        try:
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
        except Exception:
            msg = "sgrep: Error al buscar un string en archivo"
            self.logSystemError(msg)
            print(msg)    

    def do_matar1(self,argument):
        name = f"matar {argument}"
        self.archivoHistorial(name)
        print(name)
        pid = argument.split(' ',2)
        print(pid)
        int_pid = int(pid[0])
        int_proc = int(pid[1])
        print(type(int_pid),type(int_proc))
        try:
            if int_pid == -19:
                os.kill(int_proc, signal.SIGSTOP)
                print("Recibido. Exito en parar")
            elif int_pid == -18:
                os.kill(int_proc, signal.SIGCONT)
                print("\nRecibido. Exito en continuar")
            elif int_pid == -9:
                os.kill(int_proc, signal.SIGKILL)
                print("\nRecibido. Exito en matar")
        except:
            print("\nSigue en proceso")
            print("Process ID:", os.getpid())
            msg = "sgrep: Error al matar"
            self.logSystemError(msg)
            print(msg) 
        
    
if __name__ == '__main__':
    c = shellLFS()
    sys.exit(c.cmdloop())

