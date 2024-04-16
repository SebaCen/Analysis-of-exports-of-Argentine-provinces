{{
    config(
        materialized='table'
    )
}}

with destinations as(
    select * from {{ref("dim_destinations")}}
),

provinces as (
    select * from {{ref("dim_prov_dest")}}
),

export as (
    select* from {{ref("stg_staging__exportaciones_destinos")}}
)

select 
    {{ dbt_utils.generate_surrogate_key(['provinces.province', 'export.indice_tiempo', 'destinations.destination']) }} as id,
    EXTRACT(YEAR FROM (cast(export.indice_tiempo as date))) AS anio,
    provinces.province,
    destinations.destination,
    ROUND(CAST(export.value AS FLOAT64), 1) AS quantity
from export
inner join destinations
on destinations.id=export.id_destination
inner join provinces
on provinces.id=export.id_province
order by anio asc
