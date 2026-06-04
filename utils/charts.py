import plotly.express as px

def funding_chart(df):

    fig = px.histogram(
        df,
        x="Funding Amount (M USD)",
        title="Funding Distribution"
    )

    return fig


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


def industry_chart(df):

    data = (
        df.groupby("Industry")
        ["Funding Amount (M USD)"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        data,
        x="Industry",
        y="Funding Amount (M USD)",
        color="Industry"
    )

    return fig
