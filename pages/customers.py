import dash
from dash import html,dcc, Output, Input
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objects as go

dash.register_page(__name__, path="/customers")

df=pd.read_excel("business_data.xlsx", sheet_name="Customers")

main_heading=dbc.Card(
    dbc.CardBody(
        html.H1(
            "Customer Insights",
            className="text-white",
            style={
                "fontSize": "24px",
                "fontWeight": "bold",
                "textAlign": "center",
                "margin": "0"
            }
        )
    ),style={
        "background": "linear-gradient(100deg, #c9ad81, #e0931b, #c9ad81)",
        "borderRadius": "10px",
        "marginLeft": "30px",
        "marginBottom": "15px",
        "width": "835px",
    }
)

grouped = df.groupby(["Year", "Gender"])["Total Spent"].sum().reset_index()

male_data = grouped[grouped["Gender"] == "Male"]
female_data = grouped[grouped["Gender"] == "Female"]

line_fig = go.Figure()

line_fig.add_trace(go.Scatter(
    x=male_data["Year"],
    y=male_data["Total Spent"],
    mode="lines+markers",
    name="Male",
    line=dict(color="yellow", width=3),
    marker=dict(size=8, symbol="circle")
))

line_fig.add_trace(go.Scatter(
    x=female_data["Year"],
    y=female_data["Total Spent"],
    mode="lines+markers",
    name="Female",
    line=dict(color="red", width=3),
    marker=dict(size=8, symbol="circle")
))

line_fig.update_layout(
    title="Total Spending by Gender Over the Years",
    xaxis_title="Year",
    yaxis_title="Total Spent",
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    height=250,
    width=790,
    margin=dict(l=20, r=15, t=40, b=50),
    font=dict(color="white"),
    xaxis=dict(showgrid=False),
    yaxis=dict(showgrid=False),

    legend=dict(
        title="Gender",
        font=dict(size=12),
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1,
        bgcolor="rgba(0,0,0,0)"
    )
)
years=sorted(df["Year"].unique())
regions=sorted(df["Region"].unique())
max_spending = df["Total Spent"].max()


cards= dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H5("Select Year",className="text-white", style={"fontSize": "16px", "marginBottom":"10px"}),
            dcc.RadioItems(
                id="year_radio",
                value=years[0] if years else None,
                options=[{"label": year, "value": year} for year in years],
                labelStyle={
                    "display": "block",
                    "color": "white",  
                    "fontSize": "16px",
                    "marginBottom": "7px"
                },
                inputStyle={"marginRight": "12px"}
            )
        ],width="auto", style={"marginLeft": "10px", "marginTop": "15px"}
        ),
        dbc.Col([
            html.H5("Select Region",className="text-white", style={"fontSize": "16px", "marginBottom":"10px"}),
            dcc.RadioItems(
                id="region_radio",
                value=regions[0] if regions else None,
                options=[{"label": region, "value": region} for region in regions],
                labelStyle={
                    "display": "block",
                    "color": "white",  
                    "fontSize": "16px",
                    "marginBottom": "7px"
                },
                inputStyle={"marginRight": "12px"}
            )
        ],width="auto", style={"marginLeft": "20px", "marginTop": "15px"}
        ),
        dbc.Col(
            dbc.Card(
                dbc.CardBody(
                    dbc.Row([
                        dbc.Col([
                            html.H6(
                                "Avg. Loyalty Score",
                                className="text-white",
                                style={"fontSize": "16px"}
                            ),
                            dcc.Graph(
                                id="loyalty_gauge",
                                config={"displayModeBar": False}
                            )
                    ], width=6),
                        dbc.Col([
                            html.H6(
                                "Avg. Total Spending",
                                className="text-white",
                                style={"fontSize": "16px"}
                            ),
                            dcc.Graph(
                                id="spending_gauge",
                                config={"displayModeBar": False}
                            )
                    ], width=6),
                        ], className="g-0", justify="center",style={"marginLeft":"15px"}
                    )
                ),
            style={
                "background": "linear-gradient(100deg, #325f8a, #08335e)",
                "borderRadius": "10px",
                "width": "550px",
                "height": "180px",
                "marginLeft": "67px",
                "padding": "10px"
            }
        ), width="auto"
    )
    ],className="g-0", style={"marginBottom": "10px", "marginLeft": "30px"}
    ),
    dbc.Row([
        dbc.Col(
            dbc.Card(
                dbc.CardBody(
                    dcc.Graph(figure=line_fig,style={"padding":"0"}),
                ),
                style={
                    "background": "linear-gradient(100deg, #325f8a, #08335e)",
                    "borderRadius": "10px",
                    "width": "835px",
                    "height": "270px",
                }
            )
        )
    ],className="g-0", style={"marginLeft": "20px"}
    )
])

layout = html.Div([ 
                main_heading,
                cards
            ], style={
                    "marginLeft": "13rem",
                    "flexDirection": "column", 
                    "width": "calc(100% - 13rem)",
                    "backgroundColor": "transparent"
                  })

@dash.callback(
    [Output("loyalty_gauge", "figure"),
     Output("spending_gauge", "figure")],
    [Input("year_radio", "value"),
     Input("region_radio", "value")]
)
def update_gauges(selected_year, selected_region):
    if not selected_year or not selected_region:
        return dash.no_update, dash.no_update
    
    reference_df = df[(df["Year"] == 2022) & (df["Region"] == "East")]
    
    if reference_df.empty:
        ref_loyalty = 0
        ref_spending = 0
    else:
        ref_loyalty = reference_df["Loyalty Score"].mean()
        ref_spending = reference_df["Total Spent"].mean()

    filtered_df = df[(df["Year"] == selected_year) & (df["Region"] == selected_region)]

    if filtered_df.empty:
        avg_loyalty = 0
        avg_spending = 0
    else:
        avg_loyalty = filtered_df["Loyalty Score"].mean()
        avg_spending = filtered_df["Total Spent"].mean()

    loyalty_gauge_fig = go.Figure(go.Indicator(
    mode="gauge+number+delta",
    value=avg_loyalty,
    delta={'reference': ref_loyalty, 
           'increasing': {'color': "green"}, 
           'decreasing': {'color': "red"}, 
           'font': {'size': 14} },
    number={'suffix': "%", 'font': {'size': 22, 'color': 'white'}},
    gauge={
        'axis': {'range': [0, 100], 'visible': False},
        'bar': {'color': 'green', 'thickness': 1},
        'bgcolor': "#C1BFBF",
        'borderwidth': 0,
        'shape': "angular",
        # 'threshold': {'line': {'color': "white", 'width': 0}, 'thickness': 0.75, 'value': 25}
    }
))
    loyalty_gauge_fig.update_layout(
    paper_bgcolor="rgba(0,0,0,0)",
    height=140,
    width=220,
    margin=dict(l=20, r=20, t=8, b=20)
)
    
    spending_gauge_fig = go.Figure(go.Indicator(
    mode="gauge+number+delta",
    value=avg_spending,
    delta={'reference': ref_spending, 
           'increasing': {'color': "green"}, 
           'decreasing': {'color': "red"},
           'font': {'size': 14}},
    number={'suffix': "$", 'font': {'size': 22, 'color': 'white'}},
    gauge={
        'axis': {'range': [0, max(ref_spending, avg_spending) * 1.3], 'visible': False},
        'bar': {'color': 'orange', 'thickness': 1},
        'bgcolor': "#C1BFBF",
        'borderwidth': 0,
        'shape': "angular",
        # 'threshold': {'line': {'color': "white", 'width': 0}, 'thickness': 0.75, 'value': 55}
    }
))

    spending_gauge_fig.update_layout(
    paper_bgcolor="rgba(0,0,0,0)",
    height=140,
    width=220,
    margin=dict(l=20, r=20, t=8, b=20)
)

    return loyalty_gauge_fig, spending_gauge_fig