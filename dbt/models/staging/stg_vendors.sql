SELECT
	slug AS vendor_id,
	companyName AS vendor_name,
	categorySlug AS category_id
FROM {{ source('json', 'vendors') }}
