def generate_insights(df):

    insights = []

    top_industry = (
        df.groupby("Industry")
        ["Valuation (M USD)"]
        .sum()
        .idxmax()
    )

    insights.append(
        f"Top industry by valuation: {top_industry}"
    )

    top_region = (
        df.groupby("Region")
        ["Revenue (M USD)"]
        .sum()
        .idxmax()
    )

    insights.append(
        f"Top revenue region: {top_region}"
    )

    profitable = (
        df["Profitable"]
        .value_counts()
        .idxmax()
    )

    insights.append(
        f"Most startups are profitable: {profitable}"
    )

    return insights
