select
	stack_id,
	stack_name,
	vendor_id
from {{ ref('stg_stacks') }}
