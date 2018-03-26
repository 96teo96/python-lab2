from sys import argv
filename=argv[1]
txt=open(filename, "r")
print(filename)
lista=[]
lista = txt.readlines()
print("1-insert a new task")
print("2-remove a task")
print("3-show all existing task")
print("4-close the program")
a=0
while(a!=4):
    a = int(input())
    if(a==1):
        lista.append(input("inserisci una nuova task: "))
    if (a == 2):
        lista.remove(input("inserisci la task da rimuovere: ")+"\n")
    if (a == 3):
        #for i in lista:
        print(lista)
    if (a == 4):
        target=open(filename,"w")
        for i in lista:
            target.write(i+"\n")
        target.close()
