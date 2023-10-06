SELECT
	vendor_id,
	vendor_name,
	category_id,
	business_model,
	count_likes
FROM {{ ref('stg_vendors') }}
