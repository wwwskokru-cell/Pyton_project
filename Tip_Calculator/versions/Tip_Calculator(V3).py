import csv
import os
import tkinter as tk
from tkinter import messagebox, ttk

def save_to_csv(final_score: dict, filename: str = "results.csv") -> None:
    # Создаем папку, если она не существует
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    file_exists = os.path.exists(filename)
    need_header = (not file_exists) or (os.path.getsize(filename) == 0)
    
    try:
        with open(filename, "a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["order_amount", "tips_percentage", "tip", "total"],
                delimiter=";"
            )
            if need_header:
                writer.writeheader()
            writer.writerow(final_score)
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось сохранить результат: {e}")

def calculate_tip(order_amount: float, tips_percentage: int) -> dict:
    tip = order_amount / 100 * tips_percentage
    return {
        'tip': tip,
        'total': tip + order_amount,
        'tips_percentage': tips_percentage,
        'order_amount': order_amount
    }

def calculate():
    try:
        # Получаем значения из полей ввода
        order_amount = float(entry_order.get())
        tips_percentage = int(entry_tip.get())
        
        # Проверяем корректность введенных данных
        if order_amount <= 0:
            messagebox.showerror("Ошибка", "Сумма заказа должна быть положительным числом")
            return
            
        if not 0 <= tips_percentage <= 100:
            messagebox.showerror("Ошибка", "Процент чаевых должен быть между 0 и 100")
            return
            
        # Вычисляем результат
        result = calculate_tip(order_amount, tips_percentage)
        
        # Обновляем метку с результатом
        result_text = f"Сумма заказа: ₽{result['order_amount']:.2f}\n"
        result_text += f"Чаевые ({result['tips_percentage']}%): ₽{result['tip']:.2f}\n"
        result_text += f"Общая сумма: ₽{result['total']:.2f}"
        
        label_result.config(text=result_text)
        
        # Показываем кнопку для разделения счета
        btn_split.pack(pady=5)
        
        # Сохраняем результат для возможного разделения
        global current_result
        current_result = result
        
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите корректные числовые значения")

def split_bill():
    # Создаем новое окно для разделения счета
    split_window = tk.Toplevel(root)
    split_window.title("Разделить счет")
    split_window.geometry("300x150")
    
    tk.Label(split_window, text="На сколько человек разделить счет?").pack(pady=10)
    
    entry_persons = tk.Entry(split_window)
    entry_persons.pack(pady=5)
    
    def calculate_split():
        try:
            persons = int(entry_persons.get())
            if persons <= 0:
                messagebox.showerror("Ошибка", "Количество человек должно быть положительным числом")
                return
                
            amount_per_person = current_result['total'] / persons
            messagebox.showinfo("Результат", f"С каждого: ₽{amount_per_person:.2f}")
            split_window.destroy()
            
        except ValueError:
            messagebox.showerror("Ошибка", "Пожалуйста, введите корректное число")
    
    tk.Button(split_window, text="Рассчитать", command=calculate_split).pack(pady=10)

# Создаем главное окно
root = tk.Tk()
root.title("🧮 Калькулятор чаевых")
root.geometry("400x350")

# Переменная для хранения текущего результата
current_result = None

# Создаем и размещаем элементы интерфейса
frame = ttk.Frame(root, padding="20")
frame.pack(fill=tk.BOTH, expand=True)

tk.Label(frame, text="Сумма заказа (₽):", font=("Arial", 12)).pack(pady=5)
entry_order = tk.Entry(frame, font=("Arial", 12))
entry_order.pack(pady=5)

tk.Label(frame, text="Процент чаевых (%):", font=("Arial", 12)).pack(pady=5)
entry_tip = tk.Entry(frame, font=("Arial", 12))
entry_tip.pack(pady=5)

btn_calculate = tk.Button(frame, text="Рассчитать", command=calculate, 
                         bg="#4CAF50", fg="white", font=("Arial", 12))
btn_calculate.pack(pady=15)

label_result = tk.Label(frame, text="", font=("Arial", 12), justify=tk.LEFT)
label_result.pack(pady=10)

btn_split = tk.Button(frame, text="Разделить счет", command=split_bill,
                     bg="#2196F3", fg="white", font=("Arial", 10))

# Запускаем главный цикл
root.mainloop()