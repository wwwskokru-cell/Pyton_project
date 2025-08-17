def Calculator_Tip (order_amount: float, tips_percentage: int) -> dict:
    tip = order_amount / 100 * tips_percentage
    return {
        'tip' : tip,
        'total' : tip + order_amount,
        'tips_percentage' : tips_percentage,
        'order_amount' : order_amount
    }
def main():
    print("🧮 Tip Calculator")

    while True:
        try:
            order_amount = float(input("Enter the order amount: "))
            if order_amount <= 0: raise ValueError
            break
        except ValueError:
            print("Incorrect input, enter a number.")
    
    while True:
        try:
            tips_percentage = int(input("How much of a tip do you want to leave?: "))
            if not 0 <= tips_percentage <= 100: raise ValueError
            break
        except ValueError:
            print("Incorrect input, enter a number.")

    result = Calculator_Tip(order_amount, tips_percentage)
    print('\n'+'-'*50)
    print(f"Order amount: + ₽{result['order_amount']:.2f}") 
    print(f"Tip({result['tips_percentage']}%): ₽{result['tip']:.2f}")
    print(f"Total amount: ₽{result['total']:.2f}")
    print('-'*50)

if __name__ == "__main__":
    main()