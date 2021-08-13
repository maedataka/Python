class Person(object):
    
    num_legs = 2
    
    
    #クラスの中の変数をメソッドとよぶ
    #constructor
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def walk(self):
        print(f"{self.name} is walking")
        
    def run(self):
        print(f"{self.name} is running")
        
john = Person("John", "28", "male")
taro = Person("Taro", "18", "male")
emma = Person("Emma", "40", "female")

#インスタンス変数
#「.に続けてアクセス可能
print(john.age)
john.walk()
emma.run()

print(john.num_legs)
Person.num_legs = 3
print(john.num_legs)
