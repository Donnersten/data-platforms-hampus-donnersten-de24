
--- a) Find out how many data engineer programs have been applied and which schools have applied them along
SELECT
    *
FROM
    it_educations
WHERE
    LOWER(utbildningsnamn) LIKE 'data eng%';


---   b) Find out number of data engineer programs that got approved.
SELECT
    COUNT(*),
    beslut
FROM
    it_educations
WHERE
    LOWER(utbildningsnamn) LIKE 'data eng%'
GROUP BY
    beslut;


--- c) Count number of approved programs in each of the education categories (utbildningsområde)

SELECT
    COUNT(*),
    beslut,
    utbildningsområde
FROM
    myh_2024
WHERE
    beslut = 'Beviljad'
GROUP BY
    beslut,
    utbildningsområde;

--- d) Count nubmer of approved programs for each municipality (kommun).

SELECT
    COUNT(*),
    beslut,
    kommun
FROM
    myh_2024
WHERE
    beslut = 'Beviljad'
GROUP BY
    beslut,
    kommun;


--- e) Calculate the percentage of approved programs within each education category.
SELECT
    utbildningsområde,
    Count(beslut),
    round(COUNT(CASE WHEN beslut = 'Beviljad' THEN 1 END) * 100.0 / COUNT(*),2) AS procent_OK,
    round(COUNT(CASE WHEN beslut != 'Beviljad' THEN 1 END) * 100.0 / COUNT(*),2) AS procent_avslag
FROM
    myh_2024
GROUP BY
    utbildningsområde;