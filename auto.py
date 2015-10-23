
class  AutoBasico:
    marca = ""
    modelo = ""
    n_llantas = 4
    encendido = False

    def __init__ (self, marca):
        self.marca = marca

    def set_modelo (self, modelo):
        self.modelo = modelo

    def obtiene_modelo (self):
        self.modelo = input ("dame modelo>>>")


    def arranca (self):
        self.encendido = True

    def claxon (self):
        print ("bep bep")

    def __str__ (self):
        if self.encendido:
            esta_enc = "si"
        else:
            esta_enc = "no"
        return "marca = %s, modelo = %s, encendido: %s" % (self.marca, self.modelo, esta_enc)
        

class Camioneta (AutoBasico):
    carga = 100.0

    def __str__ (self):
        if self.encendido:
            esta_enc = "si"
        else:
            esta_enc = "no"
        return "marca = %s, modelo = %s, encendido: %s carga = %g" % (self.marca, self.modelo, esta_enc, self.carga)
    


marca = "VW"
modelo = "Gol"
gol = AutoBasico(marca)

# gol.arranca ()

# gol.set_modelo (modelo)
# gol.modelo = modelo
# gol.obtiene_modelo ()

# print (gol)

# gol.claxon ()


cheyene = Camioneta ("chevrolet")
cheyene.arranca()

print (cheyene)
