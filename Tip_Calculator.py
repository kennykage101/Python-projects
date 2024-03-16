bill = input("What is the total bill?: ")
bill_int = float(bill)
tip = input("What percentage tip would you like to give?: ")
tip_int = int(tip)
ppl_share = input("How many people to split the bill?: ")
ppl_share_int = int(ppl_share)
percentage_tip = tip_int / 100
total_bill = bill_int * (1 + percentage_tip)
split_bill = total_bill / ppl_share_int
round_split_bill = round(split_bill, 2)
print(f"Each person should pay: ₦{round_split_bill}")
