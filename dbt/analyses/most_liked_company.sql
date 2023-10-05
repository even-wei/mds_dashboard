SELECT
	*
FROM {{ ref('fact_vendors') }}
ORDER BY count_likes DESC
