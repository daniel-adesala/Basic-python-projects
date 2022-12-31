


continue_ = "yes"
name_bid = {}
while continue_ == "yes":
   
    name = input("What is your name?: \n")
    bid_price = int(input("What is your bid?: \n$"))
    name_bid[name] = bid_price

    continue_ = input("Is there any other bidder?: (yes or no) ").lower()

#highest bidder

def highest_bidder():
    highest_bid = 0
    for name_ in name_bid:
        bid_amount = name_bid[name_]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = name_

    print(f"The winner is {winner}, with a bid of ${highest_bid}")

highest_bidder()
