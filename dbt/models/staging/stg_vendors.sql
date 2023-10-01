select
	id as vendor_id,
	name as vendor_name,
	category_id
from {{ source('json', 'vendors') }}
