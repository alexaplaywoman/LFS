# Implementacion de Linux Shell en Python

Se implemento una shell de linux en python para una version de linux siguiendo el manual de LFS.

## Made with:

https://www.linuxfromscratch.org/lfs/view/systemd/index.html

### COMANDOS
### Copiar
___
```
copiar src_path dst_path1
src_path=origen
dst_path1=destino
```

#### ejemplo: copiar archivo carpeta

Copia el archivo de la direccion especificada a la direccion de destino. En caso de error, tira una excepcion 

### Mover
___
```
  mover src_path dst_path
  src_path=origen archivo/directorio
  dst_path=destino
```

#### ejemplo: mover carpeta carpeta

Mover un archivo/directorio de la direccion especificada a la direccion de destino.

### Renombrar
___
```
  renombrar old new
  old=nombre actual archivo/directorio
  new=nombre a cambiar archivo/directorio
```
#### ejemplo: renombrar hola.txt hola1.txt

Renombrar archivos/directorios.En caso de algun error, se lanza una excepcion.

### Listar
___
```
  listar 
  listar dirPATH
  listar= listar directorio actual
  direct_arg= direccion de la carpeta a listar
```
#### ejemplo: listar carpeta

Listar un directorio. En caso de algun error o directorio inexistente, se lanza una excepcion.

### Creardir
___
```
  creardir phrase 
  phrase= nombre(s) de carpetas a crear
```
#### ejemplo: creardir a

Crear un directorio. 
En caso de algun error o el directorio ya existe, se lanza una excepcion.

### Ir
___
```
  ir phrase 
  phrase=direccion para cambiar de directorio 
```
#### ejemplo: ir carpeta

Cambiar de directorio.\
En caso de algun error o el directorio no existe, se lanza una excepcion.

### Permisos
___
```
  permisos argument 
  argument=contiene los permisos y el archivo/directorio que desea cambiar sus permisos. 
```
#### ejemplo: permisos 777 a.txt

Cambiar los permisos sobre un archivo o un directorio.
En caso de algun error o el archivo/directorio no existe, se lanza una excepcion.

### Propietario
___
```
  propietario argument 
  argument=contiene el usuario/grupo y el archivo/directorio. 
```

#### ejemplo: propietario usuario:grupo a.txt

Cambiar los propietarios sobre un archivo.
En caso de algun error o el archivo/directorio no existe, se lanza una excepcion.

### Imprimir directorio
___
```
  printdir  
```

#### ejemplo: printdir

Imprime el directorio en el que se encuentra la shell actualmente.
En caso de algun error, se lanza una excepcion.

### Kill
___
```
  matar1 int_pid int_proc
  int_pid  = lista de procesos a ser terminados
  int_proc = 3 señales disponibles KILL, STOP, CONTINUE
```
#### ejemplo: matar1 -19 452152
Terminar procesos con señales determinadas.
En caso de algun error, se lanza una excepcion.

### Grep
___
```
  sgrep argument
  argument= Contiene el string a buscar y el archivo
  
```


#### ejemplo: sgrep mar new.txt

Buscar un string en un archivo .
En caso de algun error, archivo inexistente o palabra no encontrada, se lanza una excepcion.

### History
___

```
  historial
```

#### ejemplo: historial

Imprime el historial de comandos.
En caso de algun error, se lanza una excepcion.

## ARCHIVOS LOGS 

#### comandos.log

 * Guarda los comandos diarios realizados.

#### sistema_error.log

* Guarda los errores que se obtuvieron.

### historial.log

* Guarda los comandos realizados.

#### Implementación del LFS y SHELL

```
    Ingresamos en /sources y clonamos el repositorio.
    Luego copiamos o movemos el repositorio clonado a una carpeta creada llamada SO1 ubicada en /.
    chmod -R 777 /so1 (todos los permisos)
    luego dentro de / realizamos vi shell.sh y escribimos:
     
      #!/bin/bash
      cd /so1/LFS
      python3 main.py

    Despues ingresamos a /etc/profile y escribimos:
      bash /shell.sh
    
    Y por ultimo, en / realizar mkdir var/log/shell (crear carpeta shell para los logs) 
    chmod -R 777 /var/log/shell (todos los permisos) y listo.
  
```
## Autor

*Ethel Ortiz* (https://github.com/alexaplaywoman)
