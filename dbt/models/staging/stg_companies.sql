SELECT
	slug AS company_id,
	companyName AS company_name,
	description,
	url,
	verified
FROM {{ source('json', 'stacks') }}
