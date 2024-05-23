def primo(num):
    for i in range (2,num):
        if num % i == 0:
            print("No es un numero primo")
            return False
        else:
            print("es un numero primo")
            return True

num=int(input("Digita un numero mayor a 2: "))
primo(num)