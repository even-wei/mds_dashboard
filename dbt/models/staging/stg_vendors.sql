select
	slug as vendor_id,
	companyName as vendor_name,
	categorySlug as category_id
from {{ source('json', 'vendors') }}
