if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
import pandas as pd

@transformer
def transform(data, *args, **kwargs):
    
    prov = []

    for item in data['province']:
        if item not in prov:
            prov.append(item)
    
    df_prov = pd.DataFrame(enumerate(prov, start=1), columns=['id', 'province'])

    return df_prov


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
