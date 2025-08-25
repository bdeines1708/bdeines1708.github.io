import pandas as pd

def assert_non_null(df: pd.DataFrame, cols):
    for c in cols:
        assert df[c].isna().sum() == 0, f"Nulls found in {c}"

def assert_value_range(df: pd.DataFrame, col, low=None, high=None):
    if low is not None:
        assert (df[col] >= low).all(), f"{col} has values below {low}"
    if high is not None:
        assert (df[col] <= high).all(), f"{col} has values above {high}"

def assert_unique(df: pd.DataFrame, cols):
    assert not df.duplicated(subset=cols).any(), f"Duplicates on {cols}"
