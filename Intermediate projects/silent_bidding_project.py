import os
print("*******Welcome to silent auction program********")

bidding_dict={}

#func to check the winner
def check_winner(bidder_details):
    highest_price = 0
    winner=""
    for bidder in bidding_dict: #anil:10000, ajay:20000, anu:30000
        bidding_price=bidding_dict[bidder] #10000, 20000
        bidding_price = int(bidding_price)
        if bidding_price > highest_price:
            highest_price = bidding_price
            winner=bidder
    print(f"The winner is {winner} with the bid of {highest_price}")


bidding = True
while bidding:
    name = input("Enter your name:")
    bid = input("Enter your bid:")
    bidding_dict[name]=bid
    any_other_bidders = input("Are there any other bidders(Y/N)?:").lower()
    if any_other_bidders == "n":
        bidding = False
        print(bidding_dict)
        check_winner(bidding_dict)
    elif any_other_bidders == "y":
        os.system('cls')







