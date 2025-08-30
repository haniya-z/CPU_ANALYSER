import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import numpy as np

# Dash App
app = dash.Dash(__name__, external_stylesheets=[
    "https://cdnjs.cloudflare.com/ajax/libs/bootswatch/5.3.0/darkly/bootstrap.min.css"
])

# Data simulation
cpi_values = list(np.random.uniform(0.8, 2.0, size=20))
ipc_values = list(np.random.uniform(0.5, 1.5, size=20))

# Layout
app.layout = html.Div(
    style={"padding": "20px"},
    children=[
        html.H1(
            "🚀 CPU Pipeline Performance Dashboard",
            style={"textAlign": "center", "color": "#00e5ff", "marginBottom": "20px"}
        ),

        html.Div(
            style={"display": "flex", "justifyContent": "center", "gap": "20px", "marginBottom": "30px"},
            children=[
                html.Div(
                    className="card text-center p-3 shadow",
                    style={"flex": "1", "backgroundColor": "#1a1a2e", "borderRadius": "15px"},
                    children=[
                        html.H4("CPI (Cycles Per Instruction)", style={"color": "#00ff99"}),
                        dcc.Graph(id="cpi-graph", config={"displayModeBar": False})
                    ],
                ),
                html.Div(
                    className="card text-center p-3 shadow",
                    style={"flex": "1", "backgroundColor": "#1a1a2e", "borderRadius": "15px"},
                    children=[
                        html.H4("IPC (Instructions Per Cycle)", style={"color": "#ffcc00"}),
                        dcc.Graph(id="ipc-graph", config={"displayModeBar": False})
                    ],
                ),
            ]
        ),

        html.Div(
            className="card text-center p-3 shadow",
            style={"backgroundColor": "#16213e", "borderRadius": "15px", "padding": "20px"},
            children=[
                html.H4("📊 Live Pipeline Execution Overview", style={"color": "#ff4c60"}),
                html.P("Pipeline stages visualization will be integrated here", style={"color": "#ddd"}),
                html.Div(
                    "⚡ Coming Soon: Real-time pipeline stage heatmap",
                    style={"color": "#aaa", "fontStyle": "italic"}
                )
            ]
        ),

        dcc.Interval(id="interval-component", interval=1000, n_intervals=0)
    ]
)


# Callbacks
@app.callback(
    [Output("cpi-graph", "figure"), Output("ipc-graph", "figure")],
    [Input("interval-component", "n_intervals")]
)
def update_performance(n):
    new_cpi = np.random.uniform(0.8, 2.0)
    new_ipc = np.random.uniform(0.5, 1.5)

    cpi_values.append(new_cpi)
    ipc_values.append(new_ipc)

    if len(cpi_values) > 20:
        cpi_values.pop(0)
        ipc_values.pop(0)

    fig_cpi = go.Figure()
    fig_cpi.add_trace(go.Scatter(y=cpi_values, mode="lines+markers", line=dict(color="#00ff99")))
    fig_cpi.update_layout(
        template="plotly_dark", margin=dict(l=30, r=30, t=50, b=30),
        xaxis_title="Time", yaxis_title="CPI"
    )

    fig_ipc = go.Figure()
    fig_ipc.add_trace(go.Scatter(y=ipc_values, mode="lines+markers", line=dict(color="#ffcc00")))
    fig_ipc.update_layout(
        template="plotly_dark", margin=dict(l=30, r=30, t=50, b=30),
        xaxis_title="Time", yaxis_title="IPC"
    )

    return fig_cpi, fig_ipc


if __name__ == "__main__":
    app.run(debug=True)
