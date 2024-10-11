import random
team = [ 'Ali', 'Hashir','Balaj','Zeeshan','Umer Hassan','Mursaleen']

first = random.randint(0,6)
x = team.pop(first)

print('Lucky Draw Winner 50% OFF',x)

second = random.randint(0,5)
y = team.pop(second)

print('Lucky Draw Winner 25% OFF',y)

third = random.randint(0,4)

z = team.pop(third)

print('Lucky Draw Winner 15% OFF',z)
