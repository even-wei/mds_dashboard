SELECT
	slug AS company_id,
	companyName AS company_name,
	description,
	url,
	companyLogo AS log_url,
	verified,
	vendors
FROM {{ source('json', 'stacks') }}
