with dim_d as (
    select *
    from {{ref("stg_staging__destination")}}
),

semifinal as(
    select 
    id,
    {{destination_name('destination')}} as destination
    from dim_d
),

final as (
    select 
    id, 
    destination 
    from semifinal  where destination is not null
    
)

select * from final