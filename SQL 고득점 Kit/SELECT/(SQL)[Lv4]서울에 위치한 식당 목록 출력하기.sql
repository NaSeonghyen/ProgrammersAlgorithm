SELECT A.REST_ID
      ,A.REST_NAME
      ,B.FOOD_TYPE
      ,B.FAVORITES
      ,B.ADDRESS
      ,ROUND(A.SCORE,2) AS SCORE
FROM (
        SELECT RR.REST_ID
              ,RI.REST_NAME
              ,AVG(RR.REVIEW_SCORE) AS SCORE
        FROM REST_REVIEW RR
        LEFT JOIN REST_INFO RI
               ON RR.REST_ID = RI.REST_ID
        GROUP BY RR.REST_ID,RI.REST_NAME
) A
LEFT JOIN REST_INFO B
       ON A.REST_ID = B.REST_ID
WHERE ADDRESS LIKE '서울%'
ORDER BY SCORE DESC, B.FAVORITES DESC