def get_metrics(df):

    metrics = {
        "total_startups": len(df),

        "total_funding":
        df["Funding Amount (M USD)"].sum(),

        "total_valuation":
        df["Valuation (M USD)"].sum(),

        "total_revenue":
        df["Revenue (M USD)"].sum(),

        "avg_employees":
        round(df["Employees"].mean(), 2)
    }

    return metrics
