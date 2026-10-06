import pandas as pd

def select_columns(data: dict, columns: list) -> dict:
    """
    Returns a dictionary of value lists in the requested column order.
    """
    return pd.DataFrame(data).loc[:, columns].to_dict("list")
