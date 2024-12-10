class Votacao:
    def __init__(self):
        self.candidatos = {
            "11" : "candidato 1",
            "22" : "Candidato 2",
            "33" : "Candidato 3",
            "44" : "Candidato 4"
        }
        self.votos ={ "11": 0, "22" : 0, "33" : 0 , "44" : 0}
    def votar(self, numero):
        if numero in self.candidatos:
            print(f"Voto registrado para {self.candidatos[numero]}")    
        else:
            print("Número de candidato invalido")

    def vencendor(self):
        vencendor_numero = max(self.votos , key=self.votos.get)
        return self.candidatos[vencendor_numero]

votacao = Votacao()
votacao.votar("11")
votacao.votar("22")
votacao.votar("11")
print(f"Candidato vencedor : {votacao.vencendor()}")                