select
	slug as category_id,
	name as category_name
from {{ source('json', 'categories') }}
