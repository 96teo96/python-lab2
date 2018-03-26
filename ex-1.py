print("1-insert a new task")
print("2-remove a task")
print("3-show all existing task")
print("4-close the program")
a=int(input())
lista=[]
while(a!=4):
    if(a==1):
        lista.append(input("inserisci una nuova task: "))
    if (a == 2):
        lista.remove(input("inserisci la task da rimuovere: "))
    if (a == 3):
        for i in lista:
            print(i)
    a=int(input())
