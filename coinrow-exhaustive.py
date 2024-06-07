import tkinter as tk

def coin_row_problem(coins):
    n = len(coins)
    max_value = 0
    max_combination = []

    def exhaustive_search(i, current_value, current_combination):
        nonlocal max_value, max_combination
        if i >= n:
            if current_value > max_value:
                max_value = current_value
                max_combination = current_combination[:]
            return
        exhaustive_search(i + 2, current_value + coins[i], current_combination + [coins[i]])
        exhaustive_search(i + 1, current_value, current_combination)

    exhaustive_search(0, 0, [])
    return max_value, max_combination

def solve():
    num_coins = int(num_coins_entry.get())
    coins = [int(x) for x in coin_entries.get().split()]
    if len(coins)!= num_coins:
        result_label.config(text="Error: Invalid input")
        return
    max_value, max_combination = coin_row_problem(coins)
    result_label.config(text=f"Maximum value: {max_value}\nCombination: {max_combination}")

root = tk.Tk()
root.title("Coin Row Problem")

num_coins_label = tk.Label(root, text="Enter number of coins:")
num_coins_label.pack()

num_coins_entry = tk.Entry(root, width=10)
num_coins_entry.pack()

coin_label = tk.Label(root, text="Enter coin values (separated by spaces):")
coin_label.pack()

coin_entries = tk.Entry(root, width=50)
coin_entries.pack()

solve_button = tk.Button(root, text="Solve", command=solve)
solve_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()