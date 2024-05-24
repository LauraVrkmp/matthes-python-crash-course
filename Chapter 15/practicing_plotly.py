import plotly.graph_objects as go

from random_walk import RandomWalk

rw = RandomWalk(5000)
rw.fill_walk()

# Create the scatter plot
fig = go.Figure()

# Add scatter trace for the random walk points
fig.add_trace(go.Scattergl(
    x=rw.x_values, y=rw.y_values,
    mode='markers',
    marker=dict(
        size=3,
        color=list(range(rw.num_points)),
        colorscale='Blues',
        showscale=False
    )
))

# Add scatter traces for the starting and ending points
fig.add_trace(go.Scatter(
    x=[rw.x_values[0]], y=[rw.y_values[0]],
    mode='markers',
    marker=dict(
        size=10,
        color='green'
    ),
    name='Start'
))

fig.add_trace(go.Scatter(
    x=[rw.x_values[-1]], y=[rw.y_values[-1]],
    mode='markers',
    marker=dict(
        size=10,
        color='red'
    ),
    name='End'
))

fig.write_html('Chapter 15/first_figure.html', auto_open=True)