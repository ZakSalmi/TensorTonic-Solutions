import pandas as pd

def inspect_dataframe(data: dict) -> dict:
    """
    Returns rows, cols, columns, dtypes, and total_values in a dictionary.
    """
    df = pd.DataFrame(data)

    dic = {
        "rows": df.shape[0],
        "cols": df.shape[1],
        "columns": df.columns.to_list(),
        "dtypes": {col: str(dtype) for col, dtype in df.dtypes.items()},
        "total_values": df.size
    }
    return dic
