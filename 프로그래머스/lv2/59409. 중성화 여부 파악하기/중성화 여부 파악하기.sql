SELECT ANIMAL_ID, NAME, 
# CASE
#     WHEN SEX_UPON_INTAKE LIKE '%Neutered%' OR
#         SEX_UPON_INTAKE LIKE '%Spayed%' THEN 'O'
#     ELSE 'X'
IF(SEX_UPON_INTAKE LIKE '%Neutered%' OR SEX_UPON_INTAKE LIKE '%Spayed%','O','X') AS 중성화
# END AS 중성화
FROM ANIMAL_INS
ORDER BY ANIMAL_ID