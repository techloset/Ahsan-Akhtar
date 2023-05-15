class Person:
    def __init__(self, name,age,email) : # class constructor
        self.name=name
        self.age=age
        self.email=email


    def info(self):
        print(f'Name of this person is :{self.name}.age is :{self.age}.mailing adress is :{self.email}')
        

ali=Person('Ali',34,'alixyz.gmail') #object / instance 

ali.info()
