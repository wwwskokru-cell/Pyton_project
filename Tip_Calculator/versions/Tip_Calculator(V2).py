import csv
import os

def save_to_csv(final_score: dict, filename: str = "Tip_Calculator/results.csv") -> None:
    file_exists = os.path.exists(filename)
    need_header = (not file_exists) or (os.path.getsize(filename) == 0)
    try:
        with open( filename, "a", newline="", encoding="utf-8" ) as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["order_amount", "tips_percentage", "tip", "total"],
                delimiter=";"
            )
            if need_header:
                writer.writeheader()
            writer.writerow(final_score)
    except Exception as e:
        print(f"Error saving to CSV: {e}")



def calculator_tip (order_amount: float, tips_percentage: int) -> dict:
    tip = order_amount / 100 * tips_percentage
    return {
        'tip' : tip,
        'total' : tip + order_amount,
        'tips_percentage' : tips_percentage,
        'order_amount' : order_amount
    }


def data_entry():
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
            print("Incorrect input, enter a number between 0 and 100.")
    return order_amount, tips_percentage
     

def result():
    order_amount, tips_percentage = data_entry()
    final_score = calculator_tip(order_amount, tips_percentage)
    return final_score


def text_output(final_score):
    print('\n'+'-'*50)
    print(f"Order amount: ₽{final_score['order_amount']:.2f}") 
    print(f"Tip({final_score['tips_percentage']}%): ₽{final_score['tip']:.2f}")
    print(f"Total amount: ₽{final_score['total']:.2f}")
    print('-'*50)


def main():
    final_score = result()
    text_output(final_score)
    while True:
        splitting_the_account = input("Do you want to split the bill? Y/N: ").lower().strip()
        if splitting_the_account == "n":
            break
        elif splitting_the_account == "y":
            while True:
                try:
                    number_of_persons = int(input("How many people should the bill be divided into?: "))
                    if number_of_persons <= 0: raise ValueError
                    break
                except ValueError: 
                    print("Error: Enter a positive integer greater than 0.")
            total = final_score['total'] / number_of_persons
            print('\n'+'-'*50)
            print(f"Account for 1 person: ₽{total:.2f}")
            break
        else:
            print("Error, enter Y/N")
    save_to_csv(final_score)

if __name__ == "__main__":
    main()