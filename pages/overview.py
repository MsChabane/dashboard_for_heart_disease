from dash import html, dcc, register_page
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go


register_page(__name__, path="/", name="Overview")
df = pd.read_csv('data/heart_disease_cleaned.csv')
total_healthy_patient=df[df.heartdisease == 0].shape[0]
total_unhealthy_patient=df[df.heartdisease == 1].shape[0]

fig_age= px.histogram(df, x='age', nbins=40, title='Age Distribution of Patients',template='simple_white',color_discrete_sequence=["rgba(47, 47, 226, 0.647)"])
fig_age.update_layout( title_font=dict(size=18, color='gray'),yaxis={"title":""},xaxis={'title':{'font':{"color":"gray"}}})

chest_type_counts=df.chestpaintype.value_counts().reset_index()

fig_chest=px.bar(chest_type_counts,x='chestpaintype',y='count',title="Chest type Distrebution", template='simple_white',color_discrete_sequence=["rgba(47, 47, 226, 0.647)"])
fig_chest.update_layout( title_font=dict(size=18, color='gray'),yaxis={"title":""},xaxis={'title':{'font':{"color":"gray"}}})

fig_chol= px.histogram(df, x='cholesterol', nbins=40, title='Cholesterol Distrebution of Patients',template='simple_white',color_discrete_sequence=["rgba(47, 47, 226, 0.647)"])
fig_chol.update_layout( title_font=dict(size=18, color='gray'),yaxis={"title":""},xaxis={'title':{'font':{"color":"gray"}}})

hd_count=df.heartdisease.value_counts().reset_index()
fig_heart=px.pie(data_frame=hd_count,names='heartdisease',values="count",template='simple_white',hole=0.5,color_discrete_sequence=['#f7a8a8','#a8e6a3'])
fig_heart.update_layout(title={'text':'Heart Disease Distrebution',"font":{"size":18,"color":"gray"}}, )

def make_indicator(title, value):
    fig= go.Figure(go.Indicator(
        mode="number",
        value=value,
        title={"text": title, "font": {"size": 18,"color":'gray'}},
        number={"font":{'size':40}},
    ))
    fig.update_layout(
        height=175, 
        template='simple_white',
        paper_bgcolor='hsla(0, 0%, 100%, 0)',
        plot_bgcolor='hsla(0, 0%, 100%, 0)'
    )
    return fig
    

def make_card(title, content):
    return dbc.Col(
        [   html.Div(
                dcc.Graph(
                    figure=make_indicator(title, content)
                ),className="border-1 border rounded-3 p-1"
            )
        ],width={"size": 3}
    )


layout = dbc.Container([
    dbc.Row([
       make_card('Total patients',df.shape[0]),
       make_card('Healthy patient',total_healthy_patient),
       make_card('Unhealthy patient',total_unhealthy_patient),
    ],justify="center",className="gap-4 mb-4")
    ,
    dbc.Row([
        dbc.Col([
            html.Div(

                dcc.Graph(
                    figure=fig_heart
                ),className='p-1 border rounded mb-md-3'
            )
        ] ,lg={'size':6,"offset":0},md={'size':10,"offset":1},sm=12)
        ,
        dbc.Col(
            [  
                html.Div(
                    dcc.Graph(
                        figure=fig_age
                    ),className='p-1 border rounded'
                )
            ],lg=3,sm=12,md=6
        ),
        dbc.Col(
            [
                html.Div(
                    dcc.Graph(figure=fig_chol)
                    ,className='p-1 border rounded'
                )
            ],lg=3,sm=12,md=6
        )
    ],className="mb-4 "),
    dbc.Row([
        dbc.Col(
            [
                html.Div(
                    dcc.Graph(figure=fig_chest)
                    ,className='p-1 border rounded'
                )
            ],width=5
            )
        ],className="mb-4")
], fluid=True)  
