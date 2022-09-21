SELECT *
FROM (
    SELECT AO.ANIMAL_ID, AO.NAME
    FROM ANIMAL_OUTS AO
    LEFT JOIN ANIMAL_INS AI
           ON AO.ANIMAL_ID = AI.ANIMAL_ID
    WHERE AI.ANIMAL_ID IS NOT NULL
    ORDER BY AO.DATETIME - AI.DATETIME DESC
)
WHERE ROWNUM <= 2