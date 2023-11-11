SELECT
	slug AS category_id,
	name AS category_name,
	shortDescription AS short_description,
	vendors
FROM {{ source('json', 'categories') }}
