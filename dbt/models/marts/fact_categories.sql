SELECT
	category_id,
	category_name
FROM {{ ref('stg_categories') }}
