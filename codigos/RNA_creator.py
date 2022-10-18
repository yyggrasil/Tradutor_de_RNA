from random import randint

LENGHT = 10**23
nucleotides = ['G', 'C', 'A', 'U']
f = open('RNA.txt', 'a')
LENGHT = (LENGHT//3)*3

#create DNA file
for i in range(0,LENGHT):
    number = randint(0,3)
    f.write(nucleotides[number])