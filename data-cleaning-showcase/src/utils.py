from typing import Dict
import pandas as pd
import numpy as np

def profile(df: pd.DataFrame) -> Dict:
    return {
        "shape": df.shape,
        "dtypes": df.dtypes.astype(str).to_dict(),
        "null_counts": df.isna().sum().to_dict(),
        "duplicate_rows": int(df.duplicated().sum()),
        "sample": df.head(5).to_dict(orient="records"),
    }

def standardize_whitespace(df: pd.DataFrame) -> pd.DataFrame:
    for col in df.select_dtypes(include="object"):
        df[col] = df[col].astype(str).str.strip().str.replace(r"\s+", " ", regex=True)
    return df

def to_datetime_safe(series: pd.Series, errors: str = "coerce") -> pd.Series:
    return pd.to_datetime(series, errors=errors)

def cap_outliers(series: pd.Series, z: float = 3.0) -> pd.Series:
    m, s = series.mean(), series.std(ddof=0)
    lower, upper = m - z*s, m + z*s
    return series.clip(lower, upper)
