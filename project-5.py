import sys, subprocess, os
print("********** Welcome to silent auction **********")
bid_details={}
def bid_info():
    name=input("Enter your Name: ")
    bid_amount=int(input("Enter the bid amount: " ))
    ### Declare an empty dictionary and append bid details to it
    bid_details[name]=bid_amount
    ### Other way  of declare an empty dictionary and append bid details to it
    #bid_details= {name: bid_amount}


bid_info()
bid_continue=True
while bid_continue:
    proceed=input("Enter If you want to continue bid then enter YES if not enter NO: ")
    if proceed == "YES" or proceed == "yes" or proceed == "Yes":
        subprocess.run('clear')
        bid_info()
    elif proceed == "NO" or proceed == "no" or proceed == "No":
        winner = max(bid_details, key=bid_details.get)
        print(f"*** WINNER is:  {winner} ***")
        bid_continue=False
    else:
        print("Enter correct input YES/Yes/yes or NO/No/no")
        bid_continue=False
print(bid_details)


