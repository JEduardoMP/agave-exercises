class parenclass:

    def __init__(self, fullname):  
        self.fullname = fullname

    def GetFirstName(self):
        return self.fullname.split(" ")[0]

    def hey(self):
        print("Hello " + self.GetFirstName())


class Child_class(parenclass):

    def __init__(self, fullname, age=None):
        super().__init__(fullname)  
        self.age = age

    def hey(self):
        if self.age and self.age < 18: 
            print("What's up " + super().GetFirstName() + "?")
            
        elif self.age and self.age > 18 or not self.age:
            super().hey()

        # elif not self.age:
        #     super().hey(fullname)

if __name__ == "__main__":


    a = parenclass("Alfredo Topete Escamilla")    

    b = Child_class("Alfredo Topete Escamilla")   

    c = Child_class("Alfredo Topete Escamilla", 14)

    a.hey()

    b.hey()

    c.hey()