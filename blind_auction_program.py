import os
from blind_auction_art import logo
print(logo)
print("Welcome to the secret auction program")

# bidder_name = input("What is your name?:\n")
# bidder_price = int(input("What is your bid price?:\n₦"))

bidders_log = {}
is_bidding = True

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ''
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is{winner} with a bid of ₦{highest_bid}")
while is_bidding:
    bidder_name = input("What is your name?\n")
    bidder_price = int(input("What is your bid price?\n₦"))
    bidders_log[bidder_name] = bidder_price
    request = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    os.system('cls')
    if(request == 'no'):
        is_bidding = False
        find_highest_bidder(bidders_log)
