if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
import pandas as pd

@transformer
def transform(data, *args, **kwargs):
    
    categ = []

    for item in data['category']:
        if item not in categ:
            categ.append(item)
    
    df_categ = pd.DataFrame(enumerate(categ, start=1), columns=['id', 'category'])

    return df_categ

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
