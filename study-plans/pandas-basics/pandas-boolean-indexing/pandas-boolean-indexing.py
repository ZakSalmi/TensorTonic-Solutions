import pandas as pd

def boolean_filter(data: dict, column: str, threshold: float) -> dict:
    """
    Returns filtered_data as a dictionary of lists and count as an integer.
    """
    df = pd.DataFrame(data)
    return {"filtered_data": df[df[column] > threshold].to_dict("list"), "count": len(df[df[column] > threshold])}
