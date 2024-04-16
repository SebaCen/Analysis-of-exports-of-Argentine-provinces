with stg_cat as (
    select *
    from {{ ref("stg_staging__category") }}
),

semifinal as (
    select
    id,
    {{ category_name('category')}} as category
    from stg_cat 
), 

final as (
    select * 
    from semifinal where category is not NULL
)

select * from final