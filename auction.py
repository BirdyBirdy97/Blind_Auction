from clear import clear
from art import logo

print(logo)
print("Welcome to the secret silent auction.")

bidder_dict = {}
count = 0

#Getting the highest bid and name pair

def highest_bid(recorded_bid):
    top_bid = 0
    winner = ""
    for bidder in recorded_bid:
        if top_bid < recorded_bid[bidder]:
            top_bid = recorded_bid[bidder]
            winner = bidder

    print(f"\nThe winner is {winner} with a bid of {top_bid}$. Congratulations!")
  
while count < 1:
#Questions
    name = input("\nWhat is your name?\n")
    bid = int(input("\nWhat are you willing to pay?\n$"))
    others = input("\nAre there others who want to bid? Yes/No\n").lower()

    bidder_dict[name] = bid

#Continue options
    next = 0
    while next == 0:
        if others == "no":
            count = 1
            next = 1
            highest_bid(bidder_dict)
        elif others == "yes":
            count = 0
            clear()
            print(logo)
            print("Welcome to the secret silent auction.")
            next = 1
        else:
            print("\nInvalid entry.")
            others = input("Are there others who want to bid? Yes/No\n").lower()
