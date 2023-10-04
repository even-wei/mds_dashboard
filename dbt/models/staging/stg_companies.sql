select
	slug as company_id,
	companyName as company_name,
	description,
	url,
	verified
from {{ source('json', 'stacks') }}
