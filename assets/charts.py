import plotly.express as px

def valuation_chart(df):

    fig = px.scatter(
        df,
        x="Revenue (M USD)",
        y="Valuation (M USD)",
        color="Industry",
        size="Employees",
        hover_name="Startup Name"
    )

    return fig
