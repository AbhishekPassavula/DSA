def calcualate_investment(deposit_cash,intrest,months):
    amount=deposit_cash
    i=1
    while(i<=months):
        amount=amount+(amount*(intrest/100)/12)
        i+=1
    
    return "{:.2f}".format(amount)

if __name__=="__main__":
    deposit_cash=int(input("Enter CD's purchase value ($):"))
    intrest = float(input("Enter CD's annual percentage yield (%):"))
    months  = int(input("Enter CD's investment term (months):"))

    print(f"Your CD is worth ${calcualate_investment(deposit_cash,intrest,months)} at the end of the {months} months term")