SELECT
	vendor_id,
	vendor_name,
	category_id
FROM {{ ref('stg_vendors') }}
