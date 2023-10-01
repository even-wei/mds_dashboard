select
	id as stack_id,
	name as stack_name,
	vendor_id
from {{ source('json', 'stacks') }}
