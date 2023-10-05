SELECT
	slug AS vendor_id,
	companyName AS vendor_name,
	categorySlug AS category_id,
	businessModel AS business_model,
	countLikes AS count_likes
FROM {{ source('json', 'vendors') }}
