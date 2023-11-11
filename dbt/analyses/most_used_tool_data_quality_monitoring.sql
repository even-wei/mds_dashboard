WITH
total_companies AS (
	SELECT
		COUNT(DISTINCT company_id) AS total_companies
	FROM {{ ref('fct_vendor_usage') }}
),
companies_per_vendor AS (
	SELECT
		vendor_id,
		COUNT(DISTINCT company_id) AS companies_per_vendor
	FROM {{ ref('fct_vendor_usage') }}
	GROUP BY vendor_id
)

SELECT
	cv.vendor_id,
	v.category_id,
	v.business_model,
	v.count_likes,
	cv.companies_per_vendor as num_compnay,
	(CAST(cv.companies_per_vendor AS DECIMAL) / tc.total_companies) * 100 AS num_company_in_percentage
FROM
	companies_per_vendor cv,
	total_companies tc
JOIN
	{{ ref('dim_vendors') }} v
ON
	cv.vendor_id = v.vendor_id
WHERE v.category_id = 'data-quality-monitoring'
ORDER BY num_compnay DESC
