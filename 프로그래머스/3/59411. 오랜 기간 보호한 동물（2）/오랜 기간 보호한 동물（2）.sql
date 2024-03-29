-- SELECT A.ANIMAL_ID, A.NAME

-- FROM ANIMAL_INS A
-- JOIN ANIMAL_OUTS B
-- ON A.ANIMAL_ID = B.ANIMAL_ID
-- ORDER BY (B.DATETIME - A.DATETIME) DESC
-- FETCH FIRST 2 ROWS ONLY;

SELECT 
TEMP.ANIMAL_ID,
TEMP.NAME

FROM ( 
    SELECT 
    A.ANIMAL_ID,
    A.NAME,
    (B.DATETIME - A.DATETIME) PROTECT
    
    FROM ANIMAL_INS A
    JOIN ANIMAL_OUTS B
    ON A.ANIMAL_ID = B.ANIMAL_ID
    ORDER BY PROTECT DESC
) TEMP

WHERE ROWNUM <=2;