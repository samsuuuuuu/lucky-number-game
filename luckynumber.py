import random

def luckgame():
    luckynum=random.randint(1,50)

    while True:
        usernum=int(input("Enter the number: "))

        if usernum==luckynum:
            print("You Won, Game Over")
            break
        elif usernum<luckynum:
            print("Number Is Low")
        elif usernum>luckynum:
            print("Number Is High")
        
    print("Thankyou for playing")

luckgame()