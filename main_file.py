from dash import Dash, html, dcc
import dash
import dash_bootstrap_components as dbc

app = Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.CYBORG, dbc.icons.FONT_AWESOME],
    suppress_callback_exceptions=True
)
server = app.server

sidebar = html.Div(
    [
        html.P("Welcome Tahir!", className="lead", style={"textAlign": "center"}),
        html.Hr(style={"borderTop": "2px solid white"}),

        dbc.Nav(
            [
                dbc.NavLink([html.I(className="fa-solid fa-box fa-xs me-2"),
                             "Products"], href="/", active="exact"),
                dbc.NavLink([html.I(className="fa-solid fa-chart-simple fa-xs me-2"), 
                            "Sales"], href="/sales", active="exact"),
                dbc.NavLink([html.I(className="fa-solid fa-user fa-xs me-2"),
                             "Customers"], href="/customers", active="exact"),
                dbc.NavLink([html.I(className="fa-solid fa-circle-info fa-xs me-2"),
                             "Help Center"], href="/help", active="exact")
            ],
            vertical=True,
            pills=True,
        ),

        html.Div([
                html.Img(
                    src="assets/myphoto.jpg",
                    style={
                        "width": "40px",
                        "height": "40px",
                        "borderRadius": "50%",
                        "objectFit": "cover",
                        "objectPosition": "center", 
                        "imageRendering": "high-quality",
                        "marginRight": "15px",
                        "marginBottom": "8px"
                    },
                ),
                html.Span(
                    "Tahir M.",
                    style={
                        "fontSize": "14px",
                        "color": "white",
                        "fontWeight": "bold",
                        "alignSelf": "center"
                    },
                )
            ],
            style={
                "position": "absolute",
                "bottom": "20px", 
                "marginLeft": "33%",
                "transform": "translateX(-50%)",
                "textAlign": "center",
                "display": "flex",
                "alignItems": "center", 
                "justifyContent": "center",
                "textAlign": "center"
            },
        )
    ],
    style={
        "position": "fixed",
        "top": 0,
        "left": 0,
        "bottom": 0,
        "width": "12rem",
        "padding": "3rem 1rem",
        "background": "linear-gradient(100deg, #08335e,#325f8a)",
        "color": "white",
        "borderTopRightRadius": "20px",
        "borderBottomRightRadius": "20px"
    }
)

app.layout = html.Div([
    sidebar,
    dcc.Location(id="url"),
    dash.page_container
], style={
    "backgroundColor": "#213852",
    "minHeight": "100vh",
    "padding": "20px",
    "margin": "0",
    "overflowX": "hidden"
})

if __name__ == "__main__":
    app.run(debug=True)
