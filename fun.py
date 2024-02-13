import plotly.express as px
import plotly.graph_objects as go

def draw_boxplot(data_frame , x_column, y_column, title=''):
    fig = go.Figure()

    fig.add_trace(go.Box(x=data_frame[x_column], y=data_frame[y_column], name=y_column, boxpoints='all'))

    fig.update_layout(title=title, xaxis_title=x_column, yaxis_title=y_column, template='plotly_white')
    fig.show()
