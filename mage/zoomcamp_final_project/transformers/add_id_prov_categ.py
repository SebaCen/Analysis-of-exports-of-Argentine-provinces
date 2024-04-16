if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, dim_categ, dim_prov, *args, **kwargs):
    
    id_categ = []
    id_prov = []

    for item in data['category']:
        for n, categ in enumerate(dim_categ['category']):
            if item == categ:
                item = dim_categ.loc[n, 'id']
                id_categ.append(item)
    data['id_category'] = id_categ

    for item in data['province']:
        for n, prov in enumerate(dim_prov['province']):
            if item == prov:
                id_dim = dim_prov.loc[n, 'id']
                id_prov.append(id_dim)
    data['id_province'] = id_prov

    data = data[['indice_tiempo', 'id_category', 'id_province', 'value']]

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
