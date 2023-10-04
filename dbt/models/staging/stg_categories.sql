SELECT
	slug AS category_id,
	name AS category_name
FROM {{ source('json', 'categories') }}
