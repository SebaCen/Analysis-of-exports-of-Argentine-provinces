if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
import pandas as pd
from pandas import DataFrame


def extract_destinations(df):
    
    dest_sep = set()
    destinations = []

    for item in df:
        parts = item.split('_')
        for n, word in enumerate(parts):
            if word == 'total':
                dest_sep.add('_'.join(parts[:n]))

    for string in df:
        for parts in dest_sep:
            if parts in string:
                string = string.replace(parts + '_', '' )  # Reemplazar la parte por un string vacío
                destinations.append(string)
    
    df_out = pd.DataFrame({'destinations' : destinations})

    return df_out

def extract_provinces(destinations, df):
    
    provinces = []
    
    for string in df:
        for parts in destinations:
            if parts in string:
                string = string.replace( '_' + parts, '')  # Reemplazar la parte por un string vacío
        provinces.append(string)
    
    df_out = pd.DataFrame({'provinces' : provinces})

    return df_out

@transformer
def transform(data, *args, **kwargs):
    
    data_mel = pd.melt(data, id_vars=['indice_tiempo'], var_name='province_dest', value_name='value')
    data_dest = extract_destinations(data_mel['province_dest'])
    data_prov = extract_provinces(data_dest['destinations'], data_mel['province_dest'])
    data = pd.concat([data_mel, data_dest, data_prov], axis=1)
    data = data[['indice_tiempo', 'provinces', 'destinations', 'value']]
    
    return data

@test
def test_output(output, *args) -> DataFrame:
    """
    Template code for testing the output of the block.
    """
    assert isinstance(output, DataFrame), 'The output is not a DataFrame'

