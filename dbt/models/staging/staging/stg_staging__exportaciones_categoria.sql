with 

source as (

    select * from {{ source('staging', 'exportaciones_categoria') }}

),

renamed as (

    select
        indice_tiempo,
        id_category,
        id_province,
        value

    from source

)

select * from renamed
/*
-- dbt build --select <model_name> '{ 'is_test_run' : 'false' }' 
{% if var('is_test_run', default=true) %}

limit 100

{% endif %}
*/