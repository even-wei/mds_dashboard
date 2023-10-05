WITH unnest_vendors AS (
	SELECT
		slug AS company_id,
		UNNEST(vendors, recursive := true)
	FROM {{ source('json', 'stacks') }}
)

SELECT
	company_id,
	slug AS vendor_id
FROM unnest_vendors
