WITH TEMP AS (
SELECT C.CAR_TYPE, C.DAILY_FEE, H.HISTORY_ID, 
    DATEDIFF(H.END_DATE, H.START_DATE) + 1 AS PERIOD,
    CASE 
        WHEN DATEDIFF(H.END_DATE, H.START_DATE) + 1 >= 90 THEN '90일 이상'
        WHEN DATEDIFF(H.END_DATE, H.START_DATE) + 1 >= 30 THEN '30일 이상'
        WHEN DATEDIFF(H.END_DATE, H.START_DATE) + 1 >= 7 THEN '7일 이상'
        ELSE 'X'
    END AS DURATION_TYPE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY H
INNER JOIN CAR_RENTAL_COMPANY_CAR C
ON H.CAR_ID = C.CAR_ID
WHERE C.CAR_TYPE = '트럭'
)

SELECT TEMP.HISTORY_ID, 
ROUND(
    TEMP.DAILY_FEE * TEMP.PERIOD * 
    (100 - IFNULL(P.DISCOUNT_RATE,0)) / 100
    ) AS FEE
FROM TEMP
LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN P
ON TEMP.CAR_TYPE = P.CAR_TYPE
AND TEMP.DURATION_TYPE = P.DURATION_TYPE
ORDER BY FEE DESC, HISTORY_ID DESC;