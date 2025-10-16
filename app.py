from dash import Dash,html 
import dash_bootstrap_components as dbc 

app = Dash(__name__,external_stylesheets=[dbc.themes.GRID])


app.layout=dbc.Container([
    html.H1("Hello Dash",className="text-center"),
    html.P("This is a simple Dash application using Bootstrap components.",className="lead "),
],className="p-0 m-0 vh-100 d-flex flex-column justify-content-center align-items-center ")

if __name__ =="__main__":
    app.run(debug=True)






