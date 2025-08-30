import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import numpy as np
import random

# -----------------------------------------------------------
# Sample pipeline data
# -----------------------------------------------------------
instructions = ["Fetch", "Decode", "Execute", "Memory", "WriteBack"]
time_cycles = list(range(1, 21))  # 20 cycles

# For simulation: random pipeline activity
def generate_pipeline_data(cycles=20, stages=5):
    stages_data = []
    for cycle in range(cycles):
        row = []
        for stage in instructions:
            # Randomly pick active stage or stall
            if random.random() < 0.2:
                row.append("Stall")
            else:
                row.append(stage)
        stages_data.append(row)
    return stages_data

pipeline_data = generate_pipeline_data()

# -----------------------------------------------------------
# Dash app
# -----------------------------------------------------------
app = dash.Dash(
    __name__,
    external_stylesheets=[
        "https://cdnjs.cloudflare.com/ajax/libs/bootswatch/5.3.0/darkly/bootstrap.min.css"
    ],
    suppress_callback_exceptions=True,
)

app.layout = html.Div(
    [
        html.H1("⚡ CPU Pipeline Analyzer", style={"textAlign": "center", "color": "cyan"}),

        # Pipeline Execution Heatmap
        html.Div([
            html.H3("Pipeline Execution Timeline"),
            dcc.Graph(id="pipeline-heatmap")
        ], style={"marginBottom": "50px"}),

        # CPI & IPC Graphs
        html.Div([
            html.H3("Performance Metrics"),
            dcc.Graph(id="cpi-graph"),
            dcc.Graph(id="ipc-graph")
        ]),

        # Update Interval
        dcc.Interval(id="interval", interval=1000, n_intervals=0)
    ],
    style={"padding": "20px"}
)

# -----------------------------------------------------------
# Callbacks
# -----------------------------------------------------------
@app.callback(
    Output("pipeline-heatmap", "figure"),
    Input("interval", "n_intervals")
)
def update_pipeline(n):
    global pipeline_data
    pipeline_data = generate_pipeline_data()  # regenerate each tick

    z = [[1 if stage != "Stall" else 0 for stage in row] for row in pipeline_data]
    text = pipeline_data

    fig = go.Figure(
        data=go.Heatmap(
            z=z,
            text=text,
            hoverinfo="text",
            colorscale=[[0, "red"], [1, "green"]],
            showscale=False
        )
    )
    fig.update_layout(
        title="Pipeline Execution (Green = Active, Red = Stall)",
        xaxis=dict(title="Pipeline Stage", tickmode="array", tickvals=list(range(len(instructions))), ticktext=instructions),
        yaxis=dict(title="Cycle", tickmode="array", tickvals=list(range(len(time_cycles))), ticktext=time_cycles[::-1], autorange="reversed"),
    )
    return fig


# Separate CPI & IPC callback
cpi_values, ipc_values = [], []

@app.callback(
    [Output("cpi-graph", "figure"), Output("ipc-graph", "figure")],
    Input("interval", "n_intervals")
)
def update_metrics(n):
    global cpi_values, ipc_values

    # Append new values
    cpi_values.append(np.random.uniform(0.8, 2.0))
    ipc_values.append(np.random.uniform(0.5, 1.5))

    if len(cpi_values) > 20:
        cpi_values.pop(0)
        ipc_values.pop(0)

    # CPI Graph
    fig_cpi = go.Figure()
    fig_cpi.add_trace(go.Scatter(y=cpi_values, mode="lines+markers", name="CPI"))
    fig_cpi.update_layout(title="Cycles Per Instruction (CPI)", xaxis_title="Time", yaxis_title="CPI")

    # IPC Graph
    fig_ipc = go.Figure()
    fig_ipc.add_trace(go.Scatter(y=ipc_values, mode="lines+markers", name="IPC"))
    fig_ipc.update_layout(title="Instructions Per Cycle (IPC)", xaxis_title="Time", yaxis_title="IPC")

    return fig_cpi, fig_ipc


# -----------------------------------------------------------
# Run app
# -----------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
