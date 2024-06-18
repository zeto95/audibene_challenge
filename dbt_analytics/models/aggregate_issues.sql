WITH monthly_issues AS (
    SELECT
        strftime('%Y-%m', created_at) AS month,
        COUNT(*) AS issue_count
    FROM issues
    -- FROM {{ source('raw_data', 'issues') }}
    GROUP BY month
)

SELECT * FROM monthly_issues
