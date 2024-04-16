if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
import pandas as pd
from pandas import DataFrame

@transformer
def transform(data, *args, **kwargs):
    
    destinations = []

    for item in data['destinations']:
        if item not in destinations:
            destinations.append(item)
    
    df_dest = pd.DataFrame(enumerate(destinations, start=1), columns=['id', 'destination'])
    
    return df_dest


@test
def test_output(output, *args) -> DataFrame:
    """
    Template code for testing the output of the block.
    """
    assert isinstance(output, DataFrame), 'The output is not a DataFrame'