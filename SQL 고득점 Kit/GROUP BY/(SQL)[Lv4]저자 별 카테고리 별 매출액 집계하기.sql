SELECT A.AUTHOR_ID
      ,A.AUTHOR_NAME
      ,B.CATEGORY
      ,SUM(B.PRICE * BS.SALES) AS TOTAL_SALES
FROM BOOK_SALES BS
LEFT JOIN BOOK B
       ON BS.BOOK_ID = B.BOOK_ID
LEFT JOIN AUTHOR A
       ON B.AUTHOR_ID = A.AUTHOR_ID
WHERE SUBSTR(TO_CHAR(BS.SALES_DATE,'YYYYMMDD'),0,6) = '202201'
GROUP BY A.AUTHOR_ID, A.AUTHOR_NAME, B.CATEGORY
ORDER BY A.AUTHOR_ID, B.CATEGORY DESC