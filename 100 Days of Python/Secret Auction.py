
from auction_art import logo
print(logo)
new_bid = True
while new_bid:
    name = input("What is your name?: \n")
    price = int(input("What is your bid?: \n"))
    bids = {}
    bids[name] = price
    other_bidders = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    if other_bidders == "yes":
        print("\n" * 25)

# Integers are not subscriptable
    elif other_bidders == "no":
        new_bid = False
        print("\n" * 25)
        winning_bid = max(bids.values())
        winner_name = [name for name, bid in bids.items() if price == winning_bid][0]
        print(f"The winner is {winner_name} with a bid of {winning_bid}")

#                                     OR

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20)
