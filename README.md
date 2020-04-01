
# SCAR

## Que es SCAR ?
Scar es un sistema facil de replicar y de instalar en sistemas limitados , pensado como sustitucion al control de acceso convencional (papel y lapiz) que se utiliza en muchas colonias privadas en mexico. su objetivo es lograr las siguientes cosas:

- [x] Control de acceso por Qr para zonas residenciales.
- [x] Alternativa Opensource a software de paga.
- [ ] Control de acceso seguro punto a punto .

## Arquitectura de SCAR
Se eligio el lenguaje de programacion de python , siendo las partes significativas escritas en este lenguaje.


##Lista Dependencias:
### EN **"index.html"**
#### BULMA
el index depende de Bulma, una poderosa libreria css y de fontawsome
### EN **"server.py"**
#### BOTTLE 
la principal dependencia del servidor es bottle , un servicio de microservidor con base en python, confiable y rapido para dar posivilidad a escalarlo a una api restful, instala con:

    pip install bottle

o en python 3
 
    pip3 install bottle
#### PYCRIPTO
la segunda dependencia es pycrypto, libreria para generar cifradores de manera eficiente . se eligio el cifrador de 16 bytes. se instala con:

    pip install pycrypto

o en python 3
    
    pip3 install pycrypto


una vez iniciado esto recuerda inicializar las variables de l cifrador (iv y key )y no dejar ni la llave ni el iv originales 

```Python

obj2 = AES.new('cambiar esta key', AES.MODE_CBC, 'cambiar esta iv ')
```

#### QRCODE
tambien pillow y qrcode para generar los svg
    
    pip install qrcode[pil]


### EN **"gatekeep.py"** 

#### PYCRIPTO 
tambien depende de la misma libreria de encripcion

    pip install pycrypto

o en python 3
    
    pip3 install pycrypto

muy importante: **sincroniza el cifrador en los 2 archivos** es decir ponerles el mismo iv y el mismo key 

#### OPENCV
es la libreria de vision por computadora por defacto , no vimos caso en cuestionar el status quo por el momento asi que en estos momentos usamos esta. 

    pip install opencv-python

o en python 3
    
    pip3 install opencv-python

#### PYZBAR
pyzbar ayuda en python allevar la magia de zbar esto es leer codigos qr y codigos de barras

    pip install pyzbar

o en python 3
    
    pip3 install pyzbar

#### NUMPY
numpy es la libreria defacto de metodos numericos (a contraste de algebraicos) se lleva muy bien con opencv

    pip install numpy

o en python 3
    
    pip3 install numpy

### EN **"doorlock/doorlock.ino"**
Se requiere tener arduino instalado solamente

#### Circuito de prueba

*to-do*
## Instalacion 
*to-do*

## Soporte
se le dara soporte hasta enero 31 2021 en caso de que no haber imprevistos como defuncion de miembros de el equipo, en la medida de lo razonable .El software y la documentacion se entregan sin garantias, vease el documento license

