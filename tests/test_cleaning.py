import pandas as pd
from ml_code.data_cleaning import clean_data

def test_clean_data_removes_nans():
    df = pd.DataFrame({"age": [25, None, -5]})
    result = clean_data(df)
    assert len(result) == 1
