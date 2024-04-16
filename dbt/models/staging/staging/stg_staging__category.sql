with 

source as (

    select * from {{ source('staging', 'category') }}

),

renamed as (

    select
        id,
        category

    from source

)

select * from renamed
