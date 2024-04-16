{{
    config(
        materialized='table'
    )
}}

with categories as (
    select *
    from {{ref("dim_categories")}}
),
provinces as (
    select *
    from {{ref("dim_provinces_cat")}}
),
export as (
    select * 
    from {{ ref("stg_staging__exportaciones_categoria")}}
)

select 

    {{ dbt_utils.generate_surrogate_key(['prov.province', 'export.indice_tiempo', 'cat.category']) }} as id,
    EXTRACT(YEAR FROM (cast(export.indice_tiempo as date))) AS anio,
    cat.category,
    prov.province,
    ROUND(CAST(export.value AS FLOAT64), 1) AS value
from export
join categories as cat
on cat.id=export.id_category
join provinces as prov
on prov.id=export.id_province
order by anio asc



-- dbt build --select <model_name> '{ 'is_test_run' : 'false' }' 
{% if var('is_test_run', default=true) %}

limit 100

{% endif %}
