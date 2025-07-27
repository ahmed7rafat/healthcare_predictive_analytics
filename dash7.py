import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px
from dash.dependencies import Input, Output
import os

# Use relative path for cross-device compatibility
data_path = os.path.join(os.path.dirname(__file__), 'cleaned_healthcare_data.csv')
df = pd.read_csv(data_path)

def init_dashboard(flask_app):
    dash_app = dash.Dash(
        __name__,
        server=flask_app,
        url_base_pathname='/dash/',
    )

    dash_app.title = "Healthcare Stroke Dashboard"

    dash_app.layout = html.Div(style={'backgroundColor': '#111111', 'padding': '20px'}, children=[
        html.H1("Stroke Risk Dashboard", style={'textAlign': 'center', 'color': '#00BFFF'}),
        html.Div([
            html.Div([
                html.Label("Gender", style={'color': 'white'}),
                dcc.Dropdown(
                    id='gender-filter',
                    options=[{'label': g, 'value': g} for g in df['gender'].unique()],
                    value='Male',
                    clearable=False
                )
            ], style={'width': '30%', 'display': 'inline-block', 'paddingRight': '20px'}),

            html.Div([
                html.Label("Residence Type", style={'color': 'white'}),
                dcc.RadioItems(
                    id='residence-filter',
                    options=[{'label': r, 'value': r} for r in df['Residence_type'].unique()],
                    value='Urban',
                    labelStyle={'display': 'inline-block', 'color': 'white', 'marginRight': '10px'}
                )
            ], style={'width': '30%', 'display': 'inline-block'}),

            html.Div([
                html.Label("Age Range", style={'color': 'white'}),
                dcc.RangeSlider(
                    id='age-slider',
                    min=int(df['age'].min()),
                    max=int(df['age'].max()),
                    step=1,
                    value=[20, 80],
                    marks={i: str(i) for i in range(0, 101, 10)},
                    tooltip={'placement': 'bottom', 'always_visible': False}
                )
            ], style={'width': '90%', 'marginTop': '30px'})
        ]),

        html.Div([
            html.Label("Smoking Status", style={'color': 'white', 'marginTop': '30px'}),
            dcc.Tabs(
                id='smoking-tabs',
                value='never smoked',
                children=[
                    dcc.Tab(
                        label=s, value=s,
                        style={
                            'backgroundColor': '#1e1e1e',
                            'color': '#cccccc',
                            'border': '1px solid #444'
                        },
                        selected_style={
                            'backgroundColor': '#0d1117',
                            'color': '#00BFFF',
                            'border': '1px solid #00BFFF',
                            'fontWeight': 'bold'
                        }
                    )
                    for s in df['smoking_status'].dropna().unique()
                ]
            )
        ], style={'marginTop': '20px'}),

        html.Div([
            html.Div([dcc.Graph(id='age-stroke-chart')], style={'width': '48%', 'display': 'inline-block'}),
            html.Div([dcc.Graph(id='smoking-stroke-chart')], style={'width': '48%', 'display': 'inline-block', 'float': 'right'}),
        ], style={'marginTop': '30px'}),

        html.Div([
            html.Div([dcc.Graph(id='bmi-glucose-chart')], style={'width': '48%', 'display': 'inline-block'}),
            html.Div([dcc.Graph(id='age-distribution-chart')], style={'width': '48%', 'display': 'inline-block', 'float': 'right'}),
        ], style={'marginTop': '30px'})
    ])

    @dash_app.callback(
        [Output('age-stroke-chart', 'figure'),
         Output('smoking-stroke-chart', 'figure'),
         Output('bmi-glucose-chart', 'figure'),
         Output('age-distribution-chart', 'figure')],
        [Input('gender-filter', 'value'),
         Input('residence-filter', 'value'),
         Input('age-slider', 'value'),
         Input('smoking-tabs', 'value')]
    )
    def update_graphs(gender, residence, age_range, smoking_status):
        filtered_df = df[
            (df['gender'] == gender) &
            (df['Residence_type'] == residence) &
            (df['age'] >= age_range[0]) &
            (df['age'] <= age_range[1]) &
            (df['smoking_status'] == smoking_status)
        ]

        fig1 = px.histogram(filtered_df, x='age', color='stroke', title='Stroke by Age', nbins=30,
                            color_discrete_map={0: '#1f77b4', 1: '#d62728'})
        fig2 = px.histogram(filtered_df, x='smoking_status', color='stroke', title='Smoking Status vs Stroke',
                            barmode='group', color_discrete_map={0: '#00cc96', 1: '#ff6692'})
        fig3 = px.scatter(filtered_df, x='bmi', y='avg_glucose_level', color='stroke',
                          title='BMI vs Glucose Level', color_discrete_map={0: '#636efa', 1: '#ef553b'})
        stroke_only = filtered_df[filtered_df['stroke'] == 1]
        fig4 = px.histogram(stroke_only, x='age', title='Age Distribution of Stroke Cases', nbins=30,
                            color_discrete_sequence=['#AB63FA'])

        for fig in [fig1, fig2, fig3, fig4]:
            fig.update_layout(template='plotly_dark', plot_bgcolor='#111111')

        return fig1, fig2, fig3, fig4

    return dash_app
