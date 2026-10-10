import pandas as pd

def groupby_basics(data: dict, group_col: str, value_col: str) -> dict:
    """
    Returns sum, mean, and count dictionaries keyed by group label.
    """
    df = pd.DataFrame(data).groupby(group_col)
    return {
        'sum': df[value_col].sum().to_dict(),
        'mean': df[value_col].mean().to_dict(),
        'count': df[value_col].count().to_dict()
    }
    
