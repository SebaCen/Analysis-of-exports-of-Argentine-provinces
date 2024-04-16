with 

source as (

    select * from {{ source('staging', 'provinces_destinations') }}

),

renamed as (

    select
        id,
        province

    from source

)

select * from renamed
