from dash import html, dcc, register_page,callback,Input,Output,State
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go


register_page(__name__, path="/demographic", name="Demographic")

layout = dbc.Container([
    dcc.Location(id='url'),
    dbc.Row([
        dbc.Col([html.Div(dcc.Graph(id='age_sex_hds_fig'),className='p-1 border rounded mb-lg-0 mb-md-4 mb-sm-4')] ,lg={'size':6,"offset":0},md={'size':10,"offset":1},sm=12)
        ,
        dbc.Col(
            [  
                html.Div(
                    dcc.Graph(
                       id='age_by_sex_fig'
                    ),className='p-1 border rounded mb-lg-0 mb-md-0  mb-sm-4 '
                )
            ],lg=3,sm=12,md=6
        ),
        dbc.Col(
            [
                html.Div(
                    dcc.Graph(id='age_by_heards_fig')
                    ,className='p-1 border rounded'
                )
            ],lg=3,sm=12,md=6
        )
    ],className="mb-sm-4"),
   dbc.Row([
        dbc.Col(
            [html.Div( dcc.Graph(id='count_sex_by_hds'),className='p-1 border rounded  mb-sm-4')],lg={'size':4,"offset":0},md={'size':10,"offset":1},sm=12)
        ,
        dbc.Col(
            [html.Div( dcc.Graph(id='age_sex_hds_dist'),className='p-1 border rounded  mb-sm-4')],lg={'size':4,"offset":0},md={'size':10,"offset":1},sm=12)
        ,
        dbc.Col(
            [html.Div( dcc.Graph(id='sex_hds_dist'),className='p-1 border rounded  mb-sm-4')],lg={'size':4,"offset":0},md={'size':10,"offset":1},sm=12)
        ,

      ],className="mb-4")
], fluid=True)  







@callback([
    Output('age_sex_hds_fig','figure'),
    Output('age_by_sex_fig','figure'),
    Output('age_by_heards_fig','figure'),
    Output('count_sex_by_hds','figure'),
    Output('age_sex_hds_dist','figure'),
    Output('sex_hds_dist','figure'),
    
    Input("url","pathname")
])
def initial(v):
    df = pd.read_csv('data/heart_disease_cleaned.csv')
    heartdsBySex=df.pivot_table(index='heartdisease',columns='sex',aggfunc='size')
    fig_heartdsBySex=px.imshow(heartdsBySex,text_auto=True,color_continuous_scale='Blues',title='Sex count by heartdisease'
        )
    fig_heartdsBySex.update_layout(coloraxis_showscale=False,title_font=dict(size=18, color='gray'),yaxis={"title":""},xaxis={'title':""})
    
    age_by_sex=px.box(df,y='age',color='sex',template='simple_white',color_discrete_sequence=["#a3e4e6","#f9a8a8"],title='Age by sex')
    age_by_sex.update_layout( title_font=dict(size=18, color='gray'),yaxis={"title":""},xaxis={'title':""})
    
    age_by_heards=px.box(df,y='age',color='heartdisease',template='simple_white',color_discrete_sequence=["#a3e6bc","#e33030"],title='Age by heartdisease')
    age_by_heards.update_layout( title_font=dict(size=18, color='gray'),yaxis={"title":""},xaxis={'title':""})
    
    dist_age_by_hds=px.histogram(df,x='age',color='heartdisease',template='simple_white',color_discrete_sequence=["#a3e6bc","#e33030"],title='Distrebution of Age by heartdisease')
    dist_age_by_hds.update_layout( title_font=dict(size=18, color='gray'),yaxis={"title":""},xaxis={'title':""})
    
    sex_hds_fig= px.bar(df,x='sex',color='heartdisease',barmode='group',color_discrete_sequence=["#a3e6bc","#e33030"],template='simple_white',title='Distrebution of Sex by heartdisease')
    sex_hds_fig.update_layout( title_font=dict(size=18, color='gray'),yaxis={"title":""},xaxis={'title':""})
    
    age_violin_=px.violin(df,x='sex',y='age',color='heartdisease',color_discrete_sequence=["#a3e6bc","#e33030"],template='simple_white',title='Distrebution of age by sex and heartdisease')
    age_violin_.update_layout( title_font=dict(size=18, color='gray'),yaxis={"title":""},xaxis={'title':""})
    
    return (
            dist_age_by_hds,
            age_by_sex,
            age_by_heards,
            fig_heartdsBySex,
            age_violin_,
            sex_hds_fig
    )
