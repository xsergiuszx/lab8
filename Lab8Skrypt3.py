import sys
i = 0
with open("text.txt", "w") as plik:
    while(i!=5):
        dane =sys.stdin.readline()
        plik.write(dane)
        i = i+1
with open("text.txt", "r") as plik:
    for linia in plik: 
        print(linia, end="") 
