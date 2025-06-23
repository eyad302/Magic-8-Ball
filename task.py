import random

reponses=[
    "yes,definitly!",
    "no,not now.",
    "Ask again later",
    "it is certien",
    "very doubtful"
    "outlook is good",
    "better not tell you now",
    "comcentrarte and ask again"
]
def get_random():
    return random.choice(reponses)
def get_user_guess():
    while True:
        try:
            guess=int(input("Enter your guess (1-100)"))
            if 1<=guess<=100:
                return guess
            else:
                print("pls enter a num between 1 and 100")
        except ValueError:
            print("invalid input")
def main():
    get_user_guess()
    x=get_random()
    print (x)
main()