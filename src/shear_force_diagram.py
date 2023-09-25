import plotly as py
import plotly.graph_objs as go #Import graph objects

py.offline.init_notebook_mode(connected=True)

def gen(x, shear_force, span):
    # Define the layout object
    layout = go.Layout(
        title={'text': 'Shear Force Diagram'},
        yaxis=dict(
            title='Shear Force {kN}'
        ),
        xaxis=dict(
            title='Distance {m}',
            range=[-1, span+1]
        ),
        showlegend=False,
    )

    line = go.Scatter(
        x=x,
        y=sum(shear_force),
        mode='lines',
        name='Shear Force',
        fill='tonexty',
        line_color='green',
        fillcolor='rgba(0,255,0,0.1)'
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