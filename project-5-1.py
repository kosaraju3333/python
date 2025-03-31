import sys, subprocess, os
print("********** Welcome to silent auction **********")

def winner(bidder_details): ## {"ram": 123, "krish": 456, "VK": 7867}
    top_bid=0
    winner=""
    for bidder in bidder_details:
        bidding_price=bidder_details[bidder]
        if bidding_price > top_bid:
            top_bid = bidding_price
            winner=bidder
    print(f"WINNER is: {winner}")

bidders_data={}
end_of_bidding=False

while not end_of_bidding:
    name=input("Enter your Name: ")
    bid_amount=int(input("Enter the bid amount: " ))
    bidders_data[name]=bid_amount
    bid_continue=input("Enter If you want to continue bid then enter YES if not enter NO: ").lower()
    if bid_continue == "no":
        winner(bidders_data)
        end_of_bidding=True
    elif bid_continue == "yes":
        os.system('clear')
print(bidders_data)