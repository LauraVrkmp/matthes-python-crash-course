from random import randint

series = [4, 3, 0, 8, 3, 7, 6, 2, 7, 1, 'l', 'o', 'q', 'v', 'o']

winning = ""
for i in range(4):
    pick = series[randint(0, len(series) - 1)]
    winning += str(pick)

print(f"Any ticket matching the 4 numbers or letters {winning} wins a prize!")