import pandas as pd

def handle_missing(data: dict, fill_value: float) -> dict:
    """
    Returns null_counts as a dictionary of integers and cleaned_data as a dictionary of lists.
    """
    df = pd.DataFrame(data)
    return {
        "null_counts": {col:null_count for col,null_count in zip(df.columns, df.isna().sum())},
        "cleaned_data": df.fillna(fill_value).to_dict("list")
    }
