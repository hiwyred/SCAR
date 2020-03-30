from bottle import route, run, template, static_file ,get,post, request

from Crypto.Cipher import AES

import time

import qrcode


from PIL import Image  
import PIL  

import os.path
from os import path

def whatisthis(s):
    if isinstance(s, str):
        print "ordinary string"
    elif isinstance(s, unicode):
        print "unicode string"
    else:
        print "not a string"

@get('/service/<filename:path>')
def send_static(filename):
    return static_file(filename+'.html', root='', mimetype='text/html')


@post('/service/Rescue')
def do_post():
    Nombre= request.forms.get('fnom')
    Empresa= request.forms.get('femp')
    Servicio= request.forms.get('fser')
    mail=request.forms.get('email')
    Mes = request.forms.get('Mes')
    Dia = request.forms.get('Dia')
    uname = request.forms.get('username')
    pawd = request.forms.get('pwd') 
    mensaje=Nombre+","+Empresa+","+Servicio+","+Mes+"."+Dia+","+uname+","+pawd+","+mail+","
    indice=16-(len(mensaje)%16)
    mensaje=mensaje+'.'*indice
    print ('la longitud del string es' +str(len(mensaje)))
    print(mensaje)
    obj = AES.new('0123456789abcdef', AES.MODE_CBC, '0123456789abcdef')
    cyphertext = obj.encrypt(mensaje)
    whatisthis(cyphertext)
    print(cyphertext)
    qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=7)
    qr.add_data(cyphertext)
    img = qr.make_image(fill_color="black", back_color="white")
    
    
    im1 = img.save("name.png") 
    time.sleep(3)
    print(cyphertext)
    return static_file('name.png', root='')



run(host='192.168.1.162', port=7000)
