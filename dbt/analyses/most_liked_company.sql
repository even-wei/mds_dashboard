SELECT
	*
FROM {{ ref('dim_vendors') }}
ORDER BY count_likes DESC
