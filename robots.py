# programa para manejo de robots

# primero declarar la clase
class Robot:
    nombre = "robot"
    x = 0
    y = 0

    def __init__ (self, max_x = 10, max_y = 10):
        # print ("inicializando")
        self.x = 10
        self.y = 10
        self.derecha ()
        
        self.max_x = max_x
        self.max_y = max_y


    # def get_x (self):
    #     return x

    # def set_x (self, x):
    #     self.x = x

    def arriba (self):
        self.y += 1

    def abajo (self):
        self.y -= 1

    def derecha (self):
        self.x += 1

    def izquierda (self):
        self.x -= 1

    def __str__ (self):
        return "%s: x= %d, y= %d entre %d y %d" % (self.nombre, self.x, self.y, self.max_x, self.max_y)


max_x = 50
max_y = 50

robotito = Robot (max_x, max_y)
robotito.nombre = "robotito"
robotito.x = 10
robotito.algo = 1000
robotito.izquierda ()
robotito.arriba ()


robotin = Robot ()
robotin.nombre = "robotin"


print (robotito, robotin)
