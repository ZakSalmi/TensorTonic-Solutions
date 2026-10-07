import pandas as pd

def set_index_column(data: dict, index_col: str) -> dict:
    """
    Returns index_values and columns as lists, plus data as a dictionary of lists.
    """
    df = pd.DataFrame(data)
    index_values = df.loc[:, index_col].to_list()
    columns = [col for col in df.columns if col not in index_col]
    data = df[columns].to_dict("list")
    return {"index_values": index_values, "columns": columns, "data": data}
