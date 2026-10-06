import pandas as pd

def iloc_selection(data: dict, row: int, col: int) -> list:
    """
    Returns [element, row_values, col_values], with both value sequences as lists.
    """
    df = pd.DataFrame(data)
    element = df.iloc[row, col]
    row_v = df.iloc[row, :].tolist()
    col_v = df.iloc[:, col].tolist()
    return [element, row_v, col_v]
