class animals:
    typ = 'червемуха'
    age = 12
    stepen_prirychennosti = 4
    
    def __init__(self, typ, age, stepen_prirychennosti):
        self.typ = typ
        self.age = age
        self.stepen_prirychennosti = stepen_prirychennosti

    def who_am_i(self):
        print(self.typ)
        print(self.age)
        print(self.stepen_prirychennosti)

    def uvelichit_prirychennost(self):
        if self.stepen_prirychennosti < 10:
            self.stepen_prirychennosti += 1
        else:
            print('невозможно повысить прирученность')
    
person_myha = animals('червемуха', 12, 4)
person_myha.who_am_i()
person_myha.uvelichit_prirychennost()