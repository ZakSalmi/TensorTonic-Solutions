import pandas as pd

def select_column(data: dict, column: str) -> dict:
    """
    Returns a dictionary with values as a list and length as an integer.
    """
    df = pd.DataFrame(data)
    return {
        "values": df[column].tolist(),
        "length": len(df[column])
    }
