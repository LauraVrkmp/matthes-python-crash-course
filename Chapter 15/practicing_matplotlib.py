from die import Die
import matplotlib.pyplot as plt

die_1 = Die()
die_2 = Die()

results = []

results = [die_1.roll() + die_2.roll() for roll_num in range(50000)]

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(1, max_result+1)

frequencies = [results.count(value) for value in poss_results]
options = [value for value in range(1, max_result+1)]

fig, ax = plt.subplots()

ax.bar(options, frequencies)
plt.xticks(options)
ax.set_ylabel('Frequencies')
ax.set_title("Result of rolling two dice 50,000 times")

plt.show()