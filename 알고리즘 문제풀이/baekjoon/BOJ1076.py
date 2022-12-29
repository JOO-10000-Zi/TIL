import sys
sys.stdin = open("1076.txt")

color_ = {
    "black":"0",
    "brown":"1",	
    "red":"2",
    "orange":"3",
    "yellow":"4",
    "green":"5",
    "blue":"6",
    "violet":"7",
    "grey":"8",
    "white":'9'	
}

such = []
for _ in range(2):
    name = input()
    such.append(color_.get(name))
name1=input()

gob = int(color_.get(name1))

print(int(such[0]+such[1])*(10**gob))

