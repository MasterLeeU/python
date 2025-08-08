# Blind Auction
# This program allows users to place bids on an item in a blind auction.
# The highest bidder wins the item.
# The program uses a dictionary to store the names and bids of the participants.
# The program continues to prompt for bids until the user decides to stop.
# The program then determines the highest bid and announces the winner.

print("\n" * 50)
print("Welcome to the Blind Auction!")
print("The highest bidder wins the item.")
print("Please enter your name and bid amount.")
print("Type 'stop' when you are finished bidding.")
print("\n" * 50)
bids = {}
bidding_finished = False
while not bidding_finished:
    name = input("Enter your name: ")
    bid = input("Enter your bid amount: $")
    bids[name] = bid
    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if should_continue == "no":
        bidding_finished = True
        print("\n" * 50)
        print("Bidding has ended.")
        print("The winner is:")
        highest_bidder = ""
        highest_bid = 0
        for bidder in bids:
            if int(bids[bidder]) > highest_bid:
                highest_bid = int(bids[bidder])
                highest_bidder = bidder

        print(f"{highest_bidder} with a bid of ${highest_bid}.")
    else:
        print("\n" * 50)
# The program continues to prompt for bids until the user decides to stop.
# The program then determines the highest bid and announces the winner.