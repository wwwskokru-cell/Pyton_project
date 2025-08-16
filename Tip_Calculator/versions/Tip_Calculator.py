while True:
    try:
        order_amount = float(input("Enter the order amount: "))
        break
    except ValueError:
        print("Incorrect input, enter a number.")
    


while True:
    try:
        tips_percentage = int(input("How much of a tip do you want to leave?: "))
        break
    except ValueError:
        print("Incorrect input, enter a number.")

tips = order_amount / 100 * tips_percentage
print (f"Thanks, rhe tip was: {tips:.2f}")