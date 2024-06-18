WITH monthly_commits AS (
  SELECT
    strftime('%Y-%m', date) AS month,
    COUNT(*) AS commit_count
  FROM commits
  -- FROM {{ source('raw_data', 'commits') }}
  GROUP BY month
)

SELECT * FROM monthly_commits

