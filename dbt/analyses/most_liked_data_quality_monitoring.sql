SELECT
	v.*
FROM {{ ref('fact_vendors') }} v
JOIN {{ ref('fact_categories') }} c
ON v.category_id = c.category_id
WHERE v.category_id = 'data-quality-monitoring'
ORDER BY count_likes DESC
