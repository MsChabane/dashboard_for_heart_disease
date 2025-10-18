
from dash import Dash,html ,page_container,Input,Output,callback,State
import dash_bootstrap_components as dbc 

app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.JOURNAL, dbc.icons.FONT_AWESOME])
app.title = "Heart Disease Insights Dashboard"


app.layout = dbc.Container([
    html.H2(" Heart Disease Dashboard", className="text-center mt-3 mb-4"),
    dbc.Button(
        "show more",id='open-offcanvas',className="bg-transparent border border-1 border-primary text-primary"
    ),
    dbc.Offcanvas([
        dbc.Nav([
            dbc.NavLink(" Overview", href="/", active="exact"),
            
        ],className="d-flex flex-column justify-content-center gap-4"
        ,pills=True)
            
    ],id='offcanvas',className='bg-light'),

    
    

    page_container  
], fluid=True)

@app.callback(
    Output("offcanvas", "is_open"),
    Input("open-offcanvas", "n_clicks"),
    [State("offcanvas", "is_open")],
)
def toggle_offcanvas(n1, is_open):
    if n1:
        return not is_open
    return is_open


if __name__ == "__main__":
    app.run(debug=True)




