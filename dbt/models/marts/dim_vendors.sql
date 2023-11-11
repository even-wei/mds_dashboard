SELECT
	vendor_id,
	vendor_name,
	category_id,
	business_model,
	location,
	current_stage,
	rating,
	count_likes,
	created_at,
	updated_at
FROM {{ ref('stg_vendors') }}
