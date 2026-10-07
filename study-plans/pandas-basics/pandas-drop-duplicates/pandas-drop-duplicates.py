import pandas as pd

def drop_duplicates(data: dict) -> list:
    """
    Returns [rows_before, rows_after, cleaned_data], with integer counts and a dictionary of lists.
    """
    df = pd.DataFrame(data)
    before = len(df)
    df = df.drop_duplicates()
    after = len(df)
    return [before, after, df.to_dict("list")]
