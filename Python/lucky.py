import random
team = [  'Hashir','Balaj','Zeeshan','Umer Hassan','Mursaleen']

first = random.randint(0,4)
x = team.pop(first)

print('Lucky Draw Winner 50% OFF',x)

second = random.randint(0,3)
y = team.pop(second)

print('Lucky Draw Winner 25% OFF',y)

third = random.randint(0,2)

z = team.pop(third)

print('Lucky Draw Winner 15% OFF',z)
