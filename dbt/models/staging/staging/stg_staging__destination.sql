with 

source as (

    select * from {{ source('staging', 'destination') }}

),

renamed as (

    select
        id,
        destination

    from source

)

select * from renamed
