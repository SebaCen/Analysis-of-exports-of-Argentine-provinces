
with stg_dim as (
    select *
    from {{ ref("stg_staging__provinces") }}
),

final as (
    select 
    id,
    {{ province_name('province') }} as province
    from stg_dim
)

select * from final


