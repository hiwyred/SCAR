from Crypto.Cipher import AES

import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
from imutils.video import VideoStream
print("start videocammera")
cap =cv2.VideoCapture(0)
font =cv2.FONT_HERSHEY_DUPLEX

# --- preparation

import codecs

def slashescape(err):
    """ codecs error handler. err is UnicodeDecode instance. return
    a tuple with a replacement for the unencodable part of the input
    and a position where encoding should continue"""
    #print err, dir(err), err.start, err.end, err.object[:err.start]
    thebyte = err.object[err.start:err.end]
    repl = u'\\x'+hex(ord(thebyte))[2:]
    return (repl, err.end)

codecs.register_error('slashescape', slashescape)

# --- processing

obj2 = AES.new('0123456789abcdef', AES.MODE_CBC, '0123456789abcdef')
cypher2=""
cypher=""
Mensaje=b""
contador=0
string=b"...,...,...,Enero.31,Asff,,,...."
print(string.decode('ascii'))
print(string.decode('ascii'))
while True:

        _, frame =cap.read(0)
        decodedObjects=pyzbar.decode(frame)
        #print(decodedObjects)
        if(pyzbar.decode(frame)):
           
          
           (x, y, w, h) = decodedObjects[0].rect
           cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)
           #print(obj)
           #print(obj.data.decode('iso-8859-1').encode('utf8'))
           A=decodedObjects[0].data.decode('iso-8859-1').encode('utf8')
           B=decodedObjects[0].data.decode('iso-8859-1')
           C=decodedObjects[0].data.decode('utf8','unicode_escape').encode('iso-8859-1')
           D=decodedObjects[0].data.decode('iso-8859-1')
           #print(len(str(obj.data)))
           #print("##################################################") 
           #print("iso/utf")
           #print(obj.data.decode('iso-8859-1').encode('utf8'))
           #print("iso")
           #print(obj.data.decode('iso-8859-1'))
           #print("utf/iso")
           #print(obj.data.decode('utf8','unicode_escape').encode('iso-8859-1'))
           #print("utf")
           #print(obj.data.decode('utf8','unicode_escape')) 
           #print("##################################################")  

           #stringer=obj.data.decode('iso-8859-1') 
           #newString=b"" 
           #contador=0
           
           #for char in stringer :
               #if ((contador!=len(stringer)-1) and (contador>10)): 
                    #contador=contador+1
                    #newString=newString+char.to_bytes(1, 'little')
               #else:
                    #contador=contador+1


           #print(str(len(newString))+'::'+str(newString.decode("unicode_escape").encode('ascii')))

           cypher=obj2.decrypt(C)
           print('cypher')

     

           #print("##################################################") 
           #print("iso/utf")
           #print(cypher.decode('iso-8859-1').encode('ascii','backslashreplace'))
           #print("iso")
           #print(cypher.decode('iso-8859-1'))
           #print("utf/iso")
           #print(cypher.decode('utf8','unicode_escape').encode('iso-8859-1'))
           #print("utf")
           if(contador<1 and cypher!=cypher2):
               contador=contador+1
               cypher2=cypher
               Mensaje=cypher.decode('ascii')
               print("entro")
           print(str(contador))
           print(Mensaje)


           #print("##################################################")  
        del decodedObjects


    

        cv2.imshow('Frame',frame)
        key=cv2.waitKey(1)
        if key == 27:
           break
