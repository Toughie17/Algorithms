-- 코드를 입력하세요
SELECT CART_ID
FROM CART_PRODUCTS
WHERE NAME LIKE 'Milk' and 
CART_ID in (
SELECT CART_ID FROM CART_PRODUCTS WHERE NAME LIKE 'Yogurt'
)
ORDER BY CART_ID;