SELECT
	company_id,
	company_name
FROM {{ ref('stg_companies') }}
