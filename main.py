class Person:
  def __init__(self, name, age,adress):
    self.name = name
    self.age = age
    self.adress= adress

p1 = Person("Enes", 20,"Słomińskiego 15")

print(p1.name)
print(p1.age)
print(p1.adress)

class Student:
  def __init__(self,name,last_name,index_number,nationality):
    self.name= name
    self.last_name= last_name
    self.index_number= index_number
    self.nationality= nationality

s1=Student("enes","fikir",35197,Turkish)
print(s1.name)
print(s1.last_name)
print(s1.index_number)
print(s1.nationality)

s2=Student("hans","mark",35100,German)
print(s2.name)
print(s2.last_name)
print(s2.index_number)
print(s2.nationality)

s3=Student("johnny","sins",31315,American)
print(s3.name)
print(s3.last_name)
print(s3.index_number)
print(s3.nationality)





