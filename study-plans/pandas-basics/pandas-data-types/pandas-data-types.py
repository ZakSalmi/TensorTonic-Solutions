import pandas as pd

def data_types_overview(data: dict) -> dict:
    """
    Returns a dictionary with dtypes, type_counts, and num_columns.
    """
    df = pd.DataFrame(data)
    return {
        "dtypes": {col: str(dtype) for col, dtype in df.dtypes.items()},
        "type_counts": df.dtypes.astype(str).value_counts().to_dict(),
        "num_columns": len(df.columns)
    }
