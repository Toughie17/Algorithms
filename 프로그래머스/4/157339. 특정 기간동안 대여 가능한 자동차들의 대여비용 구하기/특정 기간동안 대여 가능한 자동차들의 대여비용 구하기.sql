-- select 
-- c.car_id, c.car_type, (c.daily_fee*((100-d.DISCOUNT_RATE)/100))*30 as fee
-- from (
--     SELECT a.car_id, a.car_type, a.daily_fee
--     from CAR_RENTAL_COMPANY_CAR a
--     where a.car_id not in (
--     select car_id from CAR_RENTAL_COMPANY_RENTAL_HISTORY
--     where to_char(START_DATE, 'YYYYMMDD') <= '20221130' and to_char(END_DATE, 'YYYYMMDD') >= '20221101'
--     )
--     and a.CAR_TYPE in ('세단','SUV') 
-- ) c

-- ,CAR_RENTAL_COMPANY_DISCOUNT_PLAN d
-- where c.CAR_TYPE = d.CAR_TYPE
-- and d.DURATION_TYPE LIKE '30%'

-- and (c.daily_fee*((100-d.DISCOUNT_RATE)/100))*30 BETWEEN 500000 and 2000000

-- order by 3 desc, 2, 1 desc

    
WITH CAR AS (
SELECT
    CAR_ID, CAR_TYPE, DAILY_FEE
    FROM CAR_RENTAL_COMPANY_CAR 
    WHERE CAR_ID NOT IN (
    SELECT CAR_ID FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY 
        WHERE TO_CHAR(START_DATE,'YYYY-MM-DD') <= '2022-11-30'
        AND TO_CHAR(END_DATE, 'YYYY-MM-DD') >='2022-11-01'
    )
    AND CAR_TYPE IN ('세단', 'SUV')
)

SELECT 
    C.CAR_ID,
    C.CAR_TYPE, 
    ROUND(C.DAILY_FEE * 30 * (1-(P.DISCOUNT_RATE/100))) FEE
FROM CAR C
JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN P
ON C.CAR_TYPE = P.CAR_TYPE
WHERE P.DURATION_TYPE = '30일 이상' 
AND ROUND(C.DAILY_FEE * 30 * (1-(P.DISCOUNT_RATE/100))) >= 500000 
AND ROUND(C.DAILY_FEE * 30 * (1-(P.DISCOUNT_RATE/100))) < 2000000
ORDER BY FEE DESC, C.CAR_TYPE ASC, C.CAR_ID DESC;