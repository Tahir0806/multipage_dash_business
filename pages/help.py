import dash
from dash import html

dash.register_page(__name__, path="/help")

layout = html.Div([
    html.H1(
        "Still Need Help?",
        className="text-white",
        style={
            "fontSize": "40px",
            "fontWeight": "bold",
            "textAlign": "center",
            "margin": "0",
            "padding": "15px 0"
        }
    ),

    html.Div([
        html.Div([
            html.Div([
                html.I(className="fa-solid fa-envelope"),
            ], className="icon-circle", style={"backgroundColor": "#3b82f6"}),  # blue circle
            html.P("support@yourcompany.com", className="text-white")
        ], className="contact-item"),

        html.Div([
            html.Div([
                html.I(className="fa-solid fa-phone"),
            ], className="icon-circle", style={"backgroundColor": "#22c55e"}),  # green circle
            html.P("+92 300 1234567", className="text-white")
        ], className="contact-item"),

        html.Div([
            html.Div([
                html.I(className="fa-solid fa-location-dot"),
            ], className="icon-circle", style={"backgroundColor": "#f97316"}),  # orange circle
            html.P("123 Business Street, Lahore, Pakistan", className="text-white")
        ], className="contact-item"),
    ], 
    style={
        "display": "flex",
        "flexDirection": "column",
        "alignItems": "center",
        "gap": "20px",
        "padding": "30px"
    })
],
style={
    "marginLeft": "13rem",
    "width": "calc(100% - 13rem)",
    "backgroundColor": "transparent"
})
