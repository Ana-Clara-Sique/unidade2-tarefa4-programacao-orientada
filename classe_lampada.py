class Lampada:
    def __init__(self,estado_inicial=False):
        self.estado = estado_inicial

    def setStatus(self,estado):
        self.estado = estado

    def showStatus(self):
        if self.estado:
            print("A lâmpada está ligada.")
        else:
            print("A lâmpada está desligada.")

lampada =Lampada(True)
lampada.showStatus()
lampada.setStatus(False)
lampada.showStatus()