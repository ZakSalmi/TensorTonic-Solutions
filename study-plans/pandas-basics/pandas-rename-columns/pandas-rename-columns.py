import pandas as pd

def rename_columns(data: dict, rename_map: dict) -> dict:
    """
    Returns a dictionary mapping renamed column names to their value lists.
    """
    return pd.DataFrame(data).rename(columns=rename_map).to_dict("list")
