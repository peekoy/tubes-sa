import tkinter as tk
from tkinter import messagebox
import time

def coin_row_dynamic(coins):
    n = len(coins)
    if n == 0:
        return 0, []
    if n == 1:
        return coins[0], [coins[0]]
    
    dp = [0] * (n + 1)
    dp[1] = coins[0]
    
    for i in range(2, n + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + coins[i - 1])
    
    max_sum = dp[n]
    
    taken_coins = []
    i = n
    while i >= 1:
        if dp[i] == dp[i - 1]:
            i -= 1
        else:
            taken_coins.append(coins[i - 1])
            i -= 2
    
    taken_coins.reverse()
    
    combinations = generate_combinations(coins, dp)
    
    return max_sum, taken_coins, combinations

def generate_combinations(coins, dp):
    n = len(coins)
    combinations = []
    
    def backtrack(index, current_comb):
        if index >= n:
            combinations.append(current_comb[:])
            return
        if index < n and (index == 0 or dp[index] != dp[index - 1]):
            current_comb.append(coins[index])
            backtrack(index + 2, current_comb)
            current_comb.pop()
        backtrack(index + 1, current_comb)
    
    backtrack(0, [])
    return combinations

def solve():
    try:
        coin_values = list(map(int, entry.get().split()))
        if not coin_values:
            raise ValueError("Empty input")
    except ValueError:
        messagebox.showerror("Error", "Silakan masukkan nilai koin yang valid (pisahkan dengan spasi).")
        return

    start_time = time.time()
    max_sum, taken_coins, combinations = coin_row_dynamic(coin_values)
    end_time = time.time()

    elapsed_time = end_time - start_time

    result_text = f"Total maksimal yang bisa diambil: {max_sum}\n"
    result_text += f"Koin yang diambil: {taken_coins}\n"
    result_text += f"Waktu eksekusi: {elapsed_time:.6f} detik\n"
    result_text += "Semua kombinasi koin yang mungkin diambil:\n"
    for comb in combinations:
        result_text += f"{comb}\n"

    result_label.config(text=result_text)

# Setup GUI
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
