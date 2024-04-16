if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
import pandas as pd
from pandas import DataFrame

@transformer
def transform(data, *args, **kwargs):
   
    provinces = []

    for item in data['provinces']:
        if item not in provinces:
            provinces.append(item)
    
    df_prov = pd.DataFrame(enumerate(provinces, start=1), columns=['id', 'province'])
    
    return df_prov


@test
def test_output(output, *args) -> DataFrame:
    """
    Template code for testing the output of the block.
    """
    assert isinstance(output, DataFrame), 'The output is not a DataFrame'
