from random import randrange
start = int(input("Enter start"))
end = int(input("Enter end"))
sysRand = randrange(start, end)
print(sysRand)
a = 1
while a<10:
    userGuess = int(input("Guess the number generated by system"))
    a +=1
    if userGuess not in range(start,end):
        print("please guess in defined range")
        continue
    else:
        if userGuess > sysRand:
            print("It is larger")
            continue
        elif userGuess < sysRand:
            print("It is smaller")
            continue
        else:
            print("congratulations!!!!!!!!!!!")
            break
