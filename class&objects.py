class human:
    def __init__(self,name, age):
        self.name=name
        self.age=age
    def methods(self):
        print("My name is"+ self.name)


h1=human(" Saurajit",26)
h2=human("Sridhar",25)
h1.methods()
print(h1.name)
print(h1.age)
print(h2.name)