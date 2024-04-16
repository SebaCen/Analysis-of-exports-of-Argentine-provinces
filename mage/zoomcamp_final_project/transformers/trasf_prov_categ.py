if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
import pandas as pd


def extract_category(df):
    
    categ = []
    
    for item in df['province_cat']:
        parts = item.split('_')
        for word in parts:
            if word == 'total':
                parts[-1] = 'total'
        categ.append(parts[-1])
        
    df_out = pd.DataFrame({'category': categ})
   
    return df_out


def extract_provinces(df):
    
    prov_sep = []
    prov_united = []
    
    for item in df['province_cat']:
        parts = item.split('_')
        for n, word in enumerate(parts):
            if word == 'total':
                parts = parts[:n+1]
        prov_sep.append(parts[:-1])
    
    for item in prov_sep:
        pro = '_'.join(item)
        prov_united.append(pro)
        if prov_united == '':
            prov_united = 'total'

    df_out = pd.DataFrame({'province' : prov_united})
    
    return df_out

@transformer
def transform(data, *args, **kwargs):
    
    data_melted = pd.melt(data, id_vars=['indice_tiempo'], var_name='province_cat', value_name='value')
    df_categ = extract_category(data_melted)
    df_prov = extract_provinces(data_melted)
    data_melted = pd.concat([data_melted, df_categ, df_prov], axis=1)
    data = data_melted[['indice_tiempo', 'category', 'province', 'value']]
    
    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'