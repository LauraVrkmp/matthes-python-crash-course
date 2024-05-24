import plotly.express as px

from die import Die

die_1 = Die()
die_2 = Die()

results = []

results = [die_1.roll() + die_2.roll() for roll_num in range(50000)]

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(1, max_result+1)

frequencies = [results.count(value) for value in poss_results]

title = "Results of Rolling Two D6's 50,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)
fig.write_html('first_figure.html', auto_open=True)