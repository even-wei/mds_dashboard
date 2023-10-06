SELECT
	category_id,
	SUM(count_likes) AS count_likes
FROM {{ ref('fact_vendors') }}
GROUP BY category_id
ORDER BY count_likes DESC
