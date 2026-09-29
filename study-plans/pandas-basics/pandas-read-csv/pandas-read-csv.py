import pandas as pd

def create_dataframe(data: dict) -> dict:
    """
    Returns a dictionary with data, shape [rows, columns], and ordered column names.
    """
    df = pd.DataFrame(data)
    dic = {"data": data, "shape": list(df.shape), "columns": df.columns.to_list()}
    return dic
