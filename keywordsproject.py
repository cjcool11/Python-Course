bill = int(input("write your bill amount: "))
payamount = int(input("write how much you paid: "))


def dueamount(bill,payamount):    
    dueamount2 = bill - payamount
    return dueamount2

print(dueamount(bill,payamount))
