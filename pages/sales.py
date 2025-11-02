import dash
import pandas as pd
from dash import html, dcc, Output, Input
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

dash.register_page(__name__, path="/sales")

df = pd.read_excel("business_data.xlsx", sheet_name="Sales")

main_heading=dbc.Card(
    dbc.CardBody(
        html.H1(
            "Overall Sales Performance",
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
        "marginBottom": "30px",
        "width": "835px",
    },
)

years = sorted(df["Year"].unique())

year_dropdown = dcc.Dropdown(
    id="year_dropdown",
    options=[{"label": y, "value": y} for y in years],
    style={
        "width": "180px",
        "borderRadius": "6px",
        "color": "black",
        "marginBottom": "10px",
        "marginLeft": "15px"
    }
)

def make_pie(percent, color):
    fig = go.Figure(
        go.Pie(
            values=[percent, 100 - percent],
            hole=0.75,
            marker_colors=[color, "rgba(255,255,255,0.1)"],
            textinfo="none"
        )
    )
    fig.update_layout(showlegend=False, 
                      margin=dict(t=0, b=0, l=0, r=0), 
                      height=130,
                      paper_bgcolor="rgba(0,0,0,0)",
                      plot_bgcolor="rgba(0,0,0,0)",
                  )
    return fig

sales_max = df.groupby("Year")["Total Sales"].sum().max() if not df.empty else 1
profit_max = df.groupby("Year")["Profit"].sum().max() if not df.empty else 1
orders_max = df.groupby("Year")["Units Sold"].sum().max() if not df.empty else 1
aov_max = (df.groupby("Year")["Total Sales"].sum() / df.groupby("Year")["Units Sold"].sum()).max() if not df.empty else 1

fig_sales = make_pie(0, "#007BFF")
fig_profit = make_pie(0, "#28A745")
fig_aov = make_pie(0, "#17A2B8")
fig_orders = make_pie(0, "#FFC107")

card_style = {
    "background": "linear-gradient(100deg,#325f8a,#08335e)",
    "borderRadius": "30px",
    "padding": "15px",
    "height": "190px",
    "marginBottom": "20px"
}

cards = dbc.Row([
    dbc.Col([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    dcc.Graph(
                        id="sales_pie",
                        figure=fig_sales,
                        config={"displayModeBar": False},
                        style={"height": "120px", "margin": "0"}
                    ),
                    html.Div(
                        id="total_sales",
                        children="-",
                        style={
                            "position": "absolute",
                            "top": "42%",
                            "left": "50%",
                            "transform": "translate(-50%, -50%)",
                            "fontSize": "14px",
                            "fontWeight": "bold",
                            "color": "white",
                            "textAlign": "center",
                        },
                    ),
                    html.Div(
                        "Sales",
                        style={
                            "textAlign": "left",
                            "color": "#E0E0E0",
                            "fontSize": "18px",
                            "fontWeight": "bold",
                            "fontStyle": "italic"
                        },
                    ),
                ], style={"position": "relative"})
            ]),
            style=card_style
        ),
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    dcc.Graph(
                        id="profit_pie",
                        figure=fig_profit,
                        config={"displayModeBar": False},
                        style={"height": "120px", "margin": "0"}
                    ),
                    html.Div(
                        id="total_profit",
                        children="-",
                        style={
                            "position": "absolute",
                            "top": "42%",
                            "left": "50%",
                            "transform": "translate(-50%, -50%)",
                            "fontSize": "14px",
                            "fontWeight": "bold",
                            "color": "white",
                            "textAlign": "center",
                        },
                    ),
                    html.Div(
                        "Profit",
                        style={
                            "textAlign": "left",
                            "color": "#E0E0E0",
                            "fontSize": "18px",
                            "fontWeight": "bold",
                            "fontStyle": "italic"
                        },
                    ),
                ], style={"position": "relative"})
            ]),
            style=card_style
        )
    ],style={"marginLeft": "30px"}, width=5),

    dbc.Col([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    dcc.Graph(
                        id="aov_pie",
                        figure=fig_aov,
                        config={"displayModeBar": False},
                        style={"height": "120px", "margin": "0"}
                    ),
                    html.Div(
                        id="avg_order_value",
                        children="-",
                        style={
                            "position": "absolute",
                            "top": "42%",
                            "left": "50%",
                            "transform": "translate(-50%, -50%)",
                            "fontSize": "16px",
                            "fontWeight": "bold",
                            "color": "white",
                            "textAlign": "center",
                        },
                    ),
                    html.Div(
                        "Avg Order Value",
                        style={
                            "textAlign": "left",
                            "color": "#E0E0E0",
                            "fontSize": "18px",
                            "fontWeight": "bold",
                            "fontStyle": "italic"
                        },
                    ),
                ], style={"position": "relative"})
            ]),
            style=card_style
        ),
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    dcc.Graph(
                        id="orders_pie",
                        figure=fig_orders,
                        config={"displayModeBar": False},
                        style={"height": "120px", "margin": "0"}
                    ),
                    html.Div(
                        id="total_orders",
                        children="-",
                        style={
                            "position": "absolute",
                            "top": "42%",
                            "left": "50%",
                            "transform": "translate(-50%, -50%)",
                            "fontSize": "22px",
                            "fontWeight": "bold",
                            "color": "white",
                            "textAlign": "center",
                        },
                    ),
                    html.Div(
                        "Units Sold",
                        style={
                            "textAlign": "left",
                            "color": "#E0E0E0",
                            "fontSize": "18px",
                            "fontWeight": "bold",
                            "fontStyle": "italic"
                        },
                    ),
                ], style={"position": "relative"})
            ]),
            style=card_style
        )
    ], width=5)
])

layout = html.Div(
    [
        main_heading,
        year_dropdown,
        cards
    ],
    style={
        "marginLeft": "13rem",
        "width": "calc(100% - 13rem)",
        "backgroundColor": "transparent",
    },
)

@dash.callback(
    [
        Output("total_sales", "children"),
        Output("total_profit", "children"),
        Output("avg_order_value", "children"),
        Output("total_orders", "children"),
        Output("sales_pie", "figure"),
        Output("profit_pie", "figure"),
        Output("aov_pie", "figure"),
        Output("orders_pie", "figure"),
    ],
    [Input("year_dropdown", "value")]
)
def update_kpi_cards(selected_year):
    filtered_df = df[df["Year"] == selected_year]

    total_sales = filtered_df["Total Sales"].sum() if not filtered_df.empty else 0
    total_profit = filtered_df["Profit"].sum() if not filtered_df.empty else 0
    total_units_sold = filtered_df["Units Sold"].sum() if not filtered_df.empty else 0
    avg_order_value = total_sales / total_units_sold if total_units_sold > 0 else 0

    sales_text = f"${total_sales:,.0f}"
    profit_text = f"${total_profit:,.0f}"
    aov_text = f"${avg_order_value:,.0f}"
    orders_text = f"{total_units_sold:,}"

    pct_sales = (total_sales / sales_max) * 100 if sales_max else 0
    pct_profit = (total_profit / profit_max) * 100 if profit_max else 0
    pct_aov = (avg_order_value / aov_max) * 100 if aov_max else 0
    pct_orders = (total_units_sold / orders_max) * 100 if orders_max else 0

    fig_sales = make_pie(pct_sales, "#9900FF")
    fig_profit = make_pie(pct_profit, "#28A745")
    fig_aov = make_pie(pct_aov, "#17A2B8")
    fig_orders = make_pie(pct_orders, "#FFC107")

    return sales_text, profit_text, aov_text, orders_text, fig_sales, fig_profit, fig_aov, fig_orders