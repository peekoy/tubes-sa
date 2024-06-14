import tkinter as tk
from tkinter import messagebox
import time
from itertools import combinations

def is_valid_combination(comb):
    for i in range(len(comb) - 1):
        if comb[i] + 1 == comb[i + 1]:
            return False
    return True

def coin_row_exhaustive_search(coins):
    n = len(coins)
    max_sum = 0
    best_combination = []
    all_combinations = []

    for r in range(n + 1):
        for comb in combinations(range(n), r):
            if is_valid_combination(comb):
                current_sum = sum(coins[i] for i in comb)
                all_combinations.append([coins[i] for i in comb])
                if current_sum > max_sum:
                    max_sum = current_sum
                    best_combination = comb

    taken_coins = [coins[i] for i in best_combination]
    return max_sum, taken_coins, all_combinations

def solve():
    try:
        coin_values = list(map(int, entry.get().split()))
        if not coin_values:
            raise ValueError("Empty input")
    except ValueError:
        messagebox.showerror("Error", "Silakan masukkan nilai koin yang valid (pisahkan dengan spasi).")
        return

    start_time = time.time()
    max_sum, taken_coins, all_combinations = coin_row_exhaustive_search(coin_values)
    end_time = time.time()

    elapsed_time = end_time - start_time

    result_text = f"Total maksimal yang bisa diambil: {max_sum}\n"
    result_text += f"Koin yang diambil: {taken_coins}\n"
    result_text += f"Waktu eksekusi: {elapsed_time:.6f} detik\n"
    result_text += "Semua kombinasi koin yang mungkin diambil:\n"
    for comb in all_combinations:
        result_text += f"{comb}\n"
    print(f"{elapsed_time:.6f}")
    result_label.config(text=result_text)

root = tk.Tk()
root.title("Coin Row Problem")

label = tk.Label(root, text="Masukkan nilai koin (pisahkan dengan spasi):")
label.pack()

entry = tk.Entry(root, width=50)
entry.pack()

solve_button = tk.Button(root, text="Solve", command=solve)
solve_button.pack()

result_label = tk.Label(root, text="", justify=tk.LEFT)
result_label.pack()

root.mainloop()
