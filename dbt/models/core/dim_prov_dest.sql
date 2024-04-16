with dim_prov as (
    select * 
    from {{ref("stg_staging__provinces_destinations")}}
),

final as (
    select 
    id,
    {{ province_name('province')}} as province
    from dim_prov
)

select * from final