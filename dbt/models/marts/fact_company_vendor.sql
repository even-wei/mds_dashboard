SELECT
	company_id,
	vendor_id
FROM {{ ref('stg_company_vendor') }}
