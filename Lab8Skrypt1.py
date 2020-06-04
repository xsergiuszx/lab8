import sys
x = 0
plik=open("dane.txt","w") 
while(x<1000):
    x = x+4
    x = str(x)
    plik.write(x)
    plik.write(" ")
    x = int(x)
else:
    print("Przekroczyles limit")
    plik.close()
