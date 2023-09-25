import plotly as py
import plotly.graph_objs as go #Import graph objects

py.offline.init_notebook_mode(connected=True)

def gen(x, bending_moments, span):
    # Define the layout object
    layout = go.Layout(
        title={'text': 'Bending Moment Diagram'},
        yaxis=dict(
            title='Bending Moment {kNm}',
            autorange='reversed'
        ),
        xaxis=dict(
            title='Distance {m}',
            range=[-1, span+1]
        ),
        showlegend=False,
    )

    line = go.Scatter(
        x=x,
        y=sum(bending_moments),
        mode='lines',
        name='Bending Moment',
        fill='tonexty',
        line_color='red',
        fillcolor='rgba(255,0,0,0.1)'
    )

    axis = go.Scatter(
        x=[0, span],
        y=[0,0],
        mode='lines',
        line_color='black'
    )

    # Generate and view figure
    fig = go.Figure(data=[line,axis], layout=layout)
    py.offline.iplot(fig)