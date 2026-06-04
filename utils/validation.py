def validate_dataframe(df):

    required_columns = [
        "Startup Name",
        "Industry",
        "Funding Amount (M USD)",
        "Valuation (M USD)",
        "Revenue (M USD)"
    ]

    missing = []

    for col in required_columns:

        if col not in df.columns:
            missing.append(col)

    return missing
