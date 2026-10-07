import pandas as pd

def reset_index_demo(data: dict, index_col: str) -> list:
    """
    Returns [columns_before_reset, columns_after_reset], both lists of strings.
    """
    df = pd.DataFrame(data).set_index(index_col)
    before = df.columns.tolist()
    df = df.reset_index()
    after = df.columns.tolist()
    return [before, after]
