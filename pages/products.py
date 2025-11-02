
import dash
from dash import html,dcc,Output,Input
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

dash.register_page(__name__, path="/")

df=pd.read_excel("business_data.xlsx", sheet_name="Products")

main_heading=html.Div(
                html.H1( "Product Details",
                    className="text-white",
                    style={
                        "fontSize": "22px",
                        "fontWeight": "bold",
                        "textAlign": "center",
                        "marginLeft": "-45px",
                        "padding": "15px 0"
                    }),
                style={    
                    "display": "flex",
                    "justifyContent": "center",
                    "alignItems": "center"
                })

bar_chart=px.bar(
    df,
    x=df["Product Name"],
    y=df["Revenue"],
    color="Product Name",
    title="Revenue by Product",
    template="plotly_dark"
)

bar_chart.update_layout(paper_bgcolor="rgba(0,0,0,0)", 
                        plot_bgcolor="rgba(0,0,0,0)",
                        xaxis_title="Products", 
                        yaxis_title="Total Revenue",
                        height=240,
                        margin=dict(l=50, r=20, t=40, b=40))


top_products = df.sort_values(by="Revenue", ascending=False).head(5)
horizontal_bar = px.bar(
    top_products,
    x="Revenue",
    y="Product Name",
    orientation="h",
    title="Top 5 Products by Revenue",
    text="Revenue",
    color="Revenue",
    color_continuous_scale="Sunset",
    template="plotly_dark"  
)
horizontal_bar.update_layout(
    yaxis=dict(categoryorder="total ascending"),
    xaxis_title="Revenue",
    yaxis_title="Products",
    title_x=0.5,
    paper_bgcolor="rgba(0,0,0,0)", 
    plot_bgcolor="rgba(0,0,0,0)",
    height=200, 
    margin=dict(l=20, r=20, t=50, b=50)
)

cards=dbc.Row([
        dbc.Col([
            dbc.Card(
                dbc.CardBody(
                    dcc.Graph(figure=bar_chart),
                    style={"padding":"0"},
                ),
                className="mt-2",
                style={"background":"linear-gradient(100deg,#325f8a,#08335e)",
                        "borderRadius": "10px",
                        "height":"240px",
                        "width": "650px",
                        "marginBottom":"8px"}
                    ),
            dbc.Card(
                dbc.CardBody(
                    dcc.Graph(figure=horizontal_bar),
                    style={"padding":"0"},
                ),
                style={"background":"linear-gradient(100deg,#325f8a,#08335e)",
                        "borderRadius": "10px",
                        "width": "650px",
                        "height":"240px"}
                    )
    ]),
        dbc.Col([
            html.H5("Select Year",className="mt-2 text-white",
            style={"fontSize":"17px","marginBottom":"5px"}),
            dcc.Dropdown(id="year_dropdown",
                        options=[{"label": str(y), "value": y} for y in df["Year"].unique()],
                        style={"width":"220px",
                               "marginBottom":"8px",
                                "backgroundColor": "#DFE1E3", 
                                "color": "black",
                                "borderRadius": "6px",
                                "boxShadow": "inset 0 2px 10px rgba(0,0,0,0.1),inset 0 -2px 10px rgba(0,0,0,0.1)"}),
            dbc.Card(
                dbc.CardBody([
                    html.H6("Key Metrics", 
                            className="text-center mb-2",
                            style={"fontSize":"20px","fontWeight":"bold", "color":"orange"}),
                    html.Hr(),
                    html.Div(
                        id="total_revenue",
                        className="text-white mt-4 mb-4"
                        ),
                    html.Hr(),
                    html.Div(
                        id="profit_margin",
                        className="text-white mt-4 mb-4"
                        ),
                    html.Hr(),
                    html.Div(
                        id="unit_sold",
                        className="text-white mt-4 mb-4"
                        )
        ]),style={"background":"linear-gradient(100deg, #08335e,#325f8a)",
                  "borderRadius": "10px",
                  "height":"418px",
                  "width":"220px"
                  })
    ])
],style={"marginLeft":"30px"})
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
    Output("total_revenue", "children"),
    Output("profit_margin", "children"),
    Output("unit_sold", "children"),
    Input("year_dropdown", "value")
)
def update_metrics(selected_year):
    if not selected_year:
        return 0,0,0

    filtered_df = df[df["Year"] == selected_year]

    total_revenue = filtered_df["Revenue"].sum()
    profit_margin = filtered_df["Profit Margin"].mean()*100
    total_units = filtered_df["Units Sold"].sum()
    

    total_revenue_div = html.Div([
        html.Span("• ", style={"fontSize": "20px", "marginRight": "8px", "verticalAlign": "middle"}),
        html.Span(f"{total_revenue:,.0f}", style={"fontSize": "24px", "fontWeight": "bold", "color": "#00ffcc"}),
        html.Span(" Pkr Total Revenue", style={"fontSize": "16px", "marginLeft": "5px"})
    ])

    profit_margin_div = html.Div([
        html.Span("• ", style={"fontSize": "20px", "marginRight": "8px", "verticalAlign": "middle"}),
        html.Span(f"{profit_margin:.2f}%", style={"fontSize": "24px", "fontWeight": "bold", "color": "#00ffcc"}),
        html.Span(" Profit Margin", style={"fontSize": "16px", "marginLeft": "5px"})
    ])

    unit_sold_div = html.Div([
        html.Span("• ", style={"fontSize": "20px", "marginRight": "8px", "verticalAlign": "middle"}),
        html.Span(f"{total_units:,}", style={"fontSize": "24px", "fontWeight": "bold", "color": "#00ffcc"}),
        html.Span(" Units Sold", style={"fontSize": "16px", "marginLeft": "5px"})
    ])

    return total_revenue_div, profit_margin_div, unit_sold_div