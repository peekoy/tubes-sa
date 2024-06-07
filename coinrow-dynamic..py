import tkinter as tk

def coin_row_problem(coins):
    n = len(coins)
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = coins[i]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]) + coins[i]

    return dp[0][n - 1], dp

def solve():
    num_coins = int(num_coins_entry.get())
    coins = [int(x) for x in coin_entries.get().split()]
    if len(coins) != num_coins:
        result_label.config(text="Error: Invalid input")
        return
    max_value, dp = coin_row_problem(coins)
    result_label.config(text=f"Maximum value: {max_value}\nDP Table:\n{dp}")

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