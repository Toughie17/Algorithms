-- 코드를 입력하세요
SELECT T.FLAVOR

FROM (
SELECT 
F.FLAVOR,
ROW_NUMBER() OVER (ORDER BY F.TOTAL_ORDER + J.TOTAL_ORDER DESC) RN
FROM
FIRST_HALF F
JOIN JULY J
ON F.FLAVOR = J.FLAVOR
ORDER BY RN DESC) T

WHERE T.RN <= 3