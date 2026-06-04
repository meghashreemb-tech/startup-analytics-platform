def filter_by_industry(df, industry):

    return df[
        df["Industry"] == industry
    ]


def filter_by_region(df, region):

    return df[
        df["Region"] == region
    ]
