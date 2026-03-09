-- 1. total number of jobs
SELECT COUNT(*) AS total_jobs
FROM jobs;

-- 2. average salary by experience level
SELECT
    experience_label,
    ROUND(AVG(salary_in_usd), 2) AS avg_salary_usd
FROM jobs
GROUP BY experience_label
ORDER BY avg_salary_usd DESC;

-- 3. top 10 highest paying job titles
SELECT
    job_title,
    ROUND(AVG(salary_in_usd), 2) AS avg_salary_usd,
    COUNT(*) AS job_count
FROM jobs
GROUP BY job_title
HAVING COUNT(*) >= 5
ORDER BY avg_salary_usd DESC
LIMIT 10;

-- 4. remote work distribution
SELECT
    remote_ratio,
    COUNT(*) AS job_count
FROM jobs
GROUP BY remote_ratio
ORDER BY remote_ratio;

-- 5. top 10 company locations by number of jobs
SELECT
    company_location,
    COUNT(*) AS job_count
FROM jobs
GROUP BY company_location
ORDER BY job_count DESC
LIMIT 10;

-- 6. average salary by company size
SELECT
    company_size,
    ROUND(AVG(salary_in_usd), 2) AS avg_salary_usd,
    COUNT(*) AS job_count
FROM jobs
GROUP BY company_size
ORDER BY avg_salary_usd DESC;

-- 7. employment type distribution
SELECT
    employment_type,
    COUNT(*) AS job_count
FROM jobs
GROUP BY employment_type
ORDER BY job_count DESC;

-- 8. salary trend by work year
SELECT
    work_year,
    ROUND(AVG(salary_in_usd), 2) AS avg_salary_usd,
    COUNT(*) AS job_count
FROM jobs
GROUP BY work_year
ORDER BY work_year;

-- 9. top 10 most common job titles
SELECT
    job_title,
    COUNT(*) AS job_count
FROM jobs
GROUP BY job_title
ORDER BY job_count DESC
LIMIT 10;

-- 10. average salary by remote ratio
SELECT
    remote_ratio,
    ROUND(AVG(salary_in_usd), 2) AS avg_salary_usd,
    COUNT(*) AS job_count
FROM jobs
GROUP BY remote_ratio
ORDER BY remote_ratio;