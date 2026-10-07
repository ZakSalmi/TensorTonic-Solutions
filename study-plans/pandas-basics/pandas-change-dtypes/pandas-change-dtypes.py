import pandas as pd

def change_dtype(data: dict, column: str, target_type: str) -> list:
    """
    Returns [dtypes_before, dtypes_after], both dictionaries of column names to dtype strings.
    """
    df = pd.DataFrame(data)
    before = df.dtypes.astype(str).to_dict()
    df = df.astype({column:target_type})
    after = df.dtypes.astype(str).to_dict()
    return [before, after]
