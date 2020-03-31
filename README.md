
# SCAR

## Que es SCAR ?
Scar es un sistema facil de replicar y de instalar en sistemas limitados , pensado como sustitucion al control de acceso convencional (papel y lapiz) que se utiliza en muchas colonias privadas en mexico. su objetivo es lograr las siguientes cosas:

- [x] Control de acceso por Qr para zonas residenciales.
- [x] Alternativa Opensource a software de paga.
- [ ] Control de acceso seguro punto a punto .

## Arquitectura de SCAR
Se eligio el lenguaje de programacion de python , siendo las partes significativas escritas en este lenguaje.


## Dependencias
### en "index.html"
el index depende de Bulma, una poderosa libreria css y de fontawsome
### en "server.py"
la principal dependencia del servidor es bottle , un servicio de microservidor con base en python, confiable y rapido para dar posivilidad a escalarlo a una api restful, instala con:

    pip install bottle

o en python 3
 
    pip3 install bottle

la segunda dependencia es pycrypto, libreria para generar cifradores de manera eficiente . se eligio el cifrador de 16 bytes. se instala con:

    pip install pycrypto

o en python 3
    
    pip3 install pycrypto


una vez iniciado esto recuerda inicializar las variables de l cifrador y no dejar ni la llave ni 

'''python
obj2 = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
'''
**en progreso**

### en "gatekeep.py" 
**to-do**
### en "doorlock/doorlock.ino"
**to-do**
## Instalacion 
**to-do**

## Soporte
se le dara soporte hasta enero 31 2021 en caso de que no haber imprevistos como defuncion de miembros de el equipo, en la medida de lo razonable .El software se entrega sin garantias, vease el documento license

