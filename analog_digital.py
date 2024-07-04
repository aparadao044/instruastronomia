import serial
import time
import datetime
import numpy as np
Ard = serial.Serial ( '/dev/ttyACM0' ,9600 , timeout =1.0)
# Ard = serial . Serial ( ’ COM5 ’ ,9600 , timeout =1.0)
# Preparar Archivo
now = datetime.datetime.now ()
name = str ( now.replace ( microsecond =0))
name = name.replace (":" ," -")
f = open ( name +". txt " , 'w+')
strt = time.time ()
Ard.flushInput ()
while (1):
# Se hace una solicitud de lectura al arduno cada segundo .
	if ( time.time () - strt < 1):
		buf = []
		for i in range (0 ,6):
			try :
# lectura Arduino , puerto serial .
				buf.append ( float ( Ard . readline ()))
			except ValueError :
				buf.append (0)
# Ard . write (( ’v ’). encode ())

		Vrd = np.median ( buf )
# Cadena de fecha
		now = datetime.datetime.now ()
		dt = str ( now.replace ( microsecond =0))
		# escribir archivo
		f . write ( str ( Vrd )+ ' , '+ dt )
		f . write ("\ n ")
		strt = time.time ()
		print (Vrd , ' , ', dt)
