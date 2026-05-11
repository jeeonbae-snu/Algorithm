SELECT CAR_ID, 
       CASE 
           WHEN MAX(
               CASE 
                   WHEN '20221016' >= STR_TO_DATE(START_DATE, '%Y-%m-%d') 
                        AND '20221016' <= STR_TO_DATE(END_DATE, '%Y-%m-%d') 
                   THEN 1 
                   ELSE 0 
               END
           ) = 1
           THEN '대여중'
           ELSE '대여 가능'
       END AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
ORDER BY CAR_ID DESC;