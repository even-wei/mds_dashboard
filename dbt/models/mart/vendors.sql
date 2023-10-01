select
	vendor_id,
	vendor_name,
	category_id
from {{ ref('stg_vendors') }}
