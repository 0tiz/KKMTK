#hier muss die IRDA angesteuert werden mit ("COM1", 115000, Parity.None, 8, StopBits.One
import serial
from serial.serialutil import STOPBITS_ONE, Timeout
from serial.win32 import WaitCommEvent
import time
import screen300

com_Port = "COM3"

ser = serial.Serial(port='COM3', baudrate=115000, bytesize=serial.EIGHTBITS,timeout=0,
    parity=serial.PARITY_NONE)
#ser.flushInput()
#ser = serial.Serial(port='COM3', baudrate=115000, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, timeout=1)
    


#Sendebefehle
befehlHandshake3 = b"\x1b\x30\x3b \x1b\x30\x3b \x1b\x30\x3b"
befehlHandshake2 = b"\x1b\x30\x3b \x1b\x30\x3b"
befehlHandshake1 = b"\x1b\x30\x3b"
befehlVerbindeMitPC = b"\x1b\x33\x6e\x01"
befehl_MTK_modus = b"\x1b\x33\xe1\x42\x54\x4b\x45\x67\xf5\x4d\xa1\x3f\x34\x33\x5b\x1b\x2b\xaf\x5f\x2f\x53\x90"

#Antwort von Screen
antwortFirmware = b"\x1b0<SCR"
antwortHandshakePoint = b"\x1b"
antwortSerienummer = b"CS"
antwortEingeschaltet = b"\n"
antwortEinschaltsignal = b"\x1bIJ"


handshake = False
einschaltCheck= True
connectTopc = False
mtkModus = False
readStream = False

screenRecorder = screen300.Screen300()
#Handshake 

while einschaltCheck == False:
    read = ser.read_all()
    ser.write(screenRecorder.doHandshake1)

    if screenRecorder.getEingeschaltet in read:
        print(read)
        print("Screen Recorder wurde eingeschaltet")
        einschaltCheck = True

    time.sleep(0.6)

while handshake == False:
    read = ser.read_all()
    ser.write(screenRecorder.doHandshake2)
    print(read)
    if antwortFirmware in read:
        print("Handshake erfolgreich")
        handshake = True
        
    time.sleep(0.6)


while readStream == False:
    read = ser.read_all()
    ser.write(screenRecorder.do_MTK_modus)
    print(read)
    time.sleep(0.3)
    






 


    
 