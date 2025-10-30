from dash import html, dcc, register_page,callback,Input,Output,State
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go


register_page(__name__, path="/", name="Overview")

layout = dbc.Container([
    dcc.Location(id='url'),
    dbc.Row([
        dbc.Col(
        [   html.Div(dcc.Graph(id='total_patient_indicator' ),className="border-1 border rounded-3 p-1",)],width={"size": 3},),
        dbc.Col(
        [   html.Div( dcc.Graph( id='tatal_healthy_patient_indicator'),className="border-1 border rounded-3 p-1",)],width={"size": 3} ),
        dbc.Col(
        [   html.Div( dcc.Graph( id='tatal_unhealthy_patient_indicator'),className="border-1 border rounded-3 p-1")],width={"size": 3}),
    ],justify="center",className="gap-4 mb-4")
    ,
    dbc.Row([
        dbc.Col([html.Div(dcc.Graph(id='heart_dist'),className='p-1 border rounded mb-lg-0 mb-md-4 mb-sm-4 ')] ,lg={'size':6,"offset":0},md={'size':10,"offset":1},sm=12)
        ,
        dbc.Col(
            [  
                html.Div(
                    dcc.Graph(
                       id='age_dist'
                    ),className='p-1 border rounded mb-lg-0 mb-md-0  mb-sm-4 '
                )
            ],lg=3,sm=12,md=6
        ),
        dbc.Col(
            [
                html.Div(
                    dcc.Graph(id='cholosterol_dist')
                    ,className='p-1 border rounded'
                )
            ],lg=3,sm=12,md=6
        )
    ],className="mb-sm-4"),
    dbc.Row([
        dbc.Col(
            [html.Div( dcc.Graph(id='chest_pain_type_dist'),className='p-1 border rounded  mb-sm-4')],lg={'size':4,"offset":0},md={'size':10,"offset":1},sm=12)
        ,
        dbc.Col([
            html.Div(dcc.Graph(id='exercice_agina_dist'),className='p-1 border rounded mb-sm-4 '
            )
        ] ,lg=4,md=6,sm=12),
        dbc.Col([
            html.Div(dcc.Graph(id='sex_dist'),className='p-1 border rounded '
            )
        ] ,lg=4,md=6,sm=12)
        ],className="mb-4")
], fluid=True)  




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
    


@callback([
    Output('total_patient_indicator','figure'),
    Output('tatal_healthy_patient_indicator','figure'),
    Output('tatal_unhealthy_patient_indicator','figure'),
    Output('heart_dist','figure'),
    Output('age_dist','figure'),
    Output('cholosterol_dist','figure'),
    Output('chest_pain_type_dist','figure'),
    Output('exercice_agina_dist','figure'),
    Output('sex_dist','figure'),
    Input("url","pathname")
])
def initial(v):
    df = pd.read_csv('data/heart_disease_cleaned.csv')
    total_healthy_patient=df[df.heartdisease == "no"].shape[0]
    total_unhealthy_patient=df[df.heartdisease == "yes"].shape[0]
    fig_age= px.histogram(df, x='age', nbins=40, title='Age Distribution of Patients',template='simple_white',color_discrete_sequence=["rgba(47, 47, 226, 0.647)"])
    fig_age.update_layout( title_font=dict(size=18, color='gray'),yaxis={"title":""},xaxis={'title':""})

    chest_type_counts=df.chestpaintype.value_counts().reset_index()


    fig_chest=px.bar(chest_type_counts,x='chestpaintype',y='count',title="Chest type Distrebution", template='simple_white',color_discrete_sequence=["rgba(47, 47, 226, 0.647)"])
    fig_chest.update_layout( title_font=dict(size=18, color='gray'),yaxis={"title":""},xaxis={'title':""})

    fig_chol= px.histogram(df, x='cholesterol', nbins=40, title='Cholesterol Distrebution of Patients',template='simple_white',color_discrete_sequence=["rgba(47, 47, 226, 0.647)"])
    fig_chol.update_layout( title_font=dict(size=18, color='gray'),yaxis={"title":""},xaxis={'title':""})

    hd_count=df.heartdisease.value_counts().reset_index()
    fig_heart=px.pie(data_frame=hd_count,names='heartdisease',values="count",template='simple_white',hole=0.5,color_discrete_sequence=["#ee5050",'#a8e6a3'])
    fig_heart.update_layout(title={'text':'Heart Disease Distrebution',"font":{"size":18,"color":"gray"}}, )

    exercice_agina = df.exerciseangina.value_counts().reset_index()
    fig_exagina=px.pie(data_frame=exercice_agina,names='exerciseangina',values="count",template='simple_white',hole=0.5,color_discrete_sequence=['#a8e6a3',"#ec5a5a"])
    fig_exagina.update_layout(title={'text':'Exercise Angina Distrebution',"font":{"size":18,"color":"gray"}}, )
    sex_counts=df.sex.value_counts().reset_index()
    fig_sex=px.bar(sex_counts,x='sex',y='count',template='simple_white',color_discrete_sequence=["#a3dfe6"],width=400)
    fig_sex.update_layout(title={'text':'Sex Distrebution',"font":{"size":18,"color":"gray"}},yaxis={"title":''} ,xaxis={'title':''})
    return (
        make_indicator("Total Patient",df.shape[0]),
        make_indicator("Total Healthy Patient",total_healthy_patient),
        make_indicator('Total UnHealthy Patient',total_unhealthy_patient),
        fig_heart,
        fig_age,
        fig_chol,
        fig_chest,
        fig_exagina,
        fig_sex
    )