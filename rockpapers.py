import random

#to string
def to_string (hand: str) -> str:
    if hand == "r":
        return "Rock"
    elif hand == "p":
        return "Paper"
    elif hand == "s":
        return "Scissors"
    else:
        return "Wrong!"


#Read a user input and convert it into r,p,s
user_hand: str
u:str = input("Rock (r), Paper (p) or Scissors (s)?").lower()
if u.startswith("r"):
    user_hand ="r"
elif u.startswith("p"):
    user_hand ="p"
elif u.startswith("s"):
    user_hand ="s"
else:
    user_hand =""


#Randomly pick one of the strings ,r, p and s
computer_hand: str


    