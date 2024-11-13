class heroi:
    def __init__(self , nome , idade , tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo
    
    def atacar(self):
        ataque = ""
        if self.tipo == "Mago":
            ataque = "Magia"
        elif self.tipo == "Guerreiro":
            ataque = "Espadas"
        elif self.tipo == "Monge":
            ataque = "Artes Marciais"
        elif self.tipo == "Ninja":
            ataque = "Shuriken"

        print(f"O {self.tipo} atacou usando {ataque}")

herois_nome = ["Zar" , "Tar" , "Lian" , "Kai"] 
herois_idade = [56 , 23 , 16 , 32]
herois_tipo = ["Mago" , "Guerreiro" , "Monge" , "Ninja"]

def cria_heroi():
    i = 0
    while i < len(herois_nome):
        novos_herois = heroi(nome=herois_nome[i] , idade=herois_idade[i] , tipo=herois_tipo[i])
        novos_herois.atacar()
        i += 1
    print("Ataques concluídos")

cria_heroi()
# heroi_1 = heroi()
# heroi_2 = heroi()
# heroi_3 = heroi()
# heroi_4 = heroi()