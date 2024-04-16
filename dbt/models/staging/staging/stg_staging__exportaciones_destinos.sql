with 

source as (

    select * from {{ source('staging', 'exportaciones_destinos') }}

),

renamed as (

    select
        indice_tiempo,
        id_province,
        id_destination,
        value

    from source

)

select * from renamed

-- dbt build --select <model_name> '{ 'is_test_run' : 'false' }' 
/*{% if var('is_test_run', default=true) %}

limit 100

{% endif %}
*/