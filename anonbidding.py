import os
def clear_console():
    os.system('cls')
bids = {}
maxbidamount = 0
end = False
while(end == False):
    name = input("What's your name? ")
    bid_amount = int(input("What's your bid amount? $"))
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.")
    bids[name] = bid_amount
    if bid_amount > maxbidamount:
        maxbidname = name
        maxbidamount = bid_amount
    if other_bidders == "no":
        end = True
    else:
        clear_console()
print(f"The winner is {maxbidname} with a bid of {maxbidamount}$")