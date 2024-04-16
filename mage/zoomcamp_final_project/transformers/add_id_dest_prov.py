if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
import pandas as pd
from pandas import DataFrame

@transformer
def transform(dim_prov, dim_dest, data, *args, **kwargs):
    
    id_dest = []
    id_prov = []

    for item in data['destinations']:
        for n, dest in enumerate(dim_dest['destination']):
            if item == dest:
                item = dim_dest.loc[n, 'id']
                id_dest.append(item)
    data['id_destination'] = id_dest

    for item in data['provinces']:
        for n, prov in enumerate(dim_prov['province']):
            if item == prov:
                id_dim = dim_prov.loc[n, 'id']
                id_prov.append(id_dim)
    data['id_province'] = id_prov

    data = data[['indice_tiempo', 'id_province', 'id_destination', 'value']]

    return data

@test
def test_output(output, *args) -> DataFrame:
    """
    Template code for testing the output of the block.
    """
    assert isinstance(output, DataFrame), 'The output is not a DataFrame'


