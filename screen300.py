class Screen300():

        #Sendebefehle
    doHandshake3 = b"\x1b\x30\x3b \x1b\x30\x3b \x1b\x30\x3b"
    doHandshake2 = b"\x1b\x30\x3b \x1b\x30\x3b"
    doHandshake1 = b"\x1b\x30\x3b"
    doVerbindeMitPC = b"\x1b\x33\x6e\x01"
    do_MTK_modus = b"\x1b\x33\xe1\x42\x54\x4b\x45\x67\xf5\x4d\xa1\x3f\x34\x33\x5b\x1b\x2b\xaf\x5f\x2f\x53\x90"

    #Antwort von Screen
    getFirmware = b"\x1b0<SCR"
    getHandshakePoint = b"\x1b"
    getSerienummer = b"CS"
    getEingeschaltet = b"\n"
    getEinschaltsignal = b"\x1bIJ"

    def getHandshake(self, handshake):
        self.doHandshake1