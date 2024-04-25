# class Perro:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def saludar(self):
#         return f"Hello"
    
#     def __str__(self) -> str:
#         return print("Mi nombre es: ", self.name)
    
# Tobby = Perro("Tobby", 3)
# print(Tobby.name)
# print(Tobby.age)
# print(Tobby.saludar())
# print(Tobby.__str__())

class Persona:

    def saludar(self):
        return f"Hello world!"
    
kevin=Persona()
print(kevin.saludar())

class Pelota:
    def __str__(self) -> str:
        return f"Yo puedo rebotar"
    
futbol=Pelota()
print(futbol.__str__())