import random

health_points_a = 10
range_a = 1
position_a = 1

health_points_b = 20
attack_b = random.randint(1,5)
range_b = 1
position_b = 1

def scenario(position):
    scenario = ["1","2","3","4","5","6","7","8","9"]
    row = ""
    for i in scenario:
        if i == position:
            row += "#"
        else:
            row += (i)

while health_points_a > 0 and health_points_b > 0:
    print("Health points Player", health_points_a)
    print("Health points Boss", health_points_b)
    gamerinput = input("Deseas moverte(m) o atacar(a): ")
    if gamerinput == "m":
        destiny = input("hacia donde? indica el numero: ")
        position_a = scenario(destiny)
    else:
        health_points_b-=random.randint(1,3)
    print(position_a)
if health_points_b <= 0:
    print("Ganaste")
else:
    print("Perdiste")



class Person:
  def __init__(self, type, character, ):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age) 




