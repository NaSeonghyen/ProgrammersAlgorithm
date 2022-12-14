SELECT A.CART_ID
FROM(
    SELECT CART_ID
    FROM CART_PRODUCTS
    WHERE NAME IN('Yogurt')
    GROUP BY CART_ID
    HAVING COUNT(*) >= 1
) A
INNER JOIN (
    SELECT CART_ID
    FROM CART_PRODUCTS
    WHERE NAME IN('Milk')
    GROUP BY CART_ID
    HAVING COUNT(*) >= 1
) B ON A.CART_ID = B.CART_ID
ORDER BY A.CART_ID