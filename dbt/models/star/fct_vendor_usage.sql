WITH unnest_vendors AS (
	SELECT
		company_id,
		UNNEST(vendors, recursive := true)
	FROM {{ ref('stg_companies') }}
)

SELECT
	company_id,
	slug AS vendor_id
FROM unnest_vendors
