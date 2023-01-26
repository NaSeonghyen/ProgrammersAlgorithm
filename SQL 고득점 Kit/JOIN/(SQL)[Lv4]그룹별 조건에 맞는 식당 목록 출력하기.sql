SELECT A.MEMBER_NAME
      ,B.REVIEW_TEXT
      ,TO_CHAR(B.REVIEW_DATE,'YYYY-MM-DD')
FROM (

        SELECT MP.MEMBER_ID
              ,MP.MEMBER_NAME
              ,COUNT(MP.MEMBER_ID) AS CNT
        FROM MEMBER_PROFILE MP
        LEFT JOIN REST_REVIEW RR
               ON MP.MEMBER_ID = RR.MEMBER_ID
        GROUP BY MP.MEMBER_ID,MP.MEMBER_NAME
        HAVING COUNT(MP.MEMBER_ID) = (SELECT MAX(X.CNT)
                                        FROM(
                                            SELECT MP.MEMBER_ID
                                                  ,MP.MEMBER_NAME
                                                  ,COUNT(MP.MEMBER_ID) AS CNT
                                            FROM MEMBER_PROFILE MP
                                            LEFT JOIN REST_REVIEW RR
                                                   ON MP.MEMBER_ID = RR.MEMBER_ID
                                            GROUP BY MP.MEMBER_ID,MP.MEMBER_NAME
                                            ) X)
    ) A
LEFT JOIN REST_REVIEW B
       ON A.MEMBER_ID = B.MEMBER_ID
ORDER BY B.REVIEW_DATE, B.REVIEW_TEXT