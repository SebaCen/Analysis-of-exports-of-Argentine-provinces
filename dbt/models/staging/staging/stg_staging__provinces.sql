with 

source as (

    select * from {{ source('staging', 'provinces') }}

),

renamed as (

    select
        id,
        province

    from source

)

select * from renamed
