WITH
total_companies AS (
	SELECT
		COUNT(DISTINCT company_id) AS total_companies
	FROM {{ ref('fact_company_vendor') }}
),
companies_per_vendor AS (
	SELECT
		vendor_id,
		COUNT(DISTINCT company_id) AS companies_per_vendor
	FROM {{ ref('fact_company_vendor') }}
	GROUP BY vendor_id
)

SELECT
	cv.vendor_id,
	cv.companies_per_vendor as num_compnay,
	(CAST(cv.companies_per_vendor AS DECIMAL) / tc.total_companies) * 100 AS num_company_in_percentage
FROM
	companies_per_vendor cv,
	total_companies tc
ORDER BY num_compnay DESC
