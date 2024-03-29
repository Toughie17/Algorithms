-- -- 코드를 입력하세요
-- SELECT 
--     AP.APNT_NO, P.PT_NAME, AP.PT_NO, AP.MCDP_CD, D.DR_NAME,
--     AP.APNT_YMD
-- FROM 
--     APPOINTMENT AP
-- JOIN DOCTOR D
--     ON AP.MDDR_ID = D.DR_ID
-- JOIN PATIENT P
--     ON AP.PT_NO = P.PT_NO
-- WHERE 
--     TO_CHAR(AP.apnt_ymd,'YYYYMMDD') = '20220413'
--     AND AP.APNT_CNCL_YN = 'N'
--     AND AP.MCDP_CD = 'CS'
-- ORDER BY 
--     APNT_NO ASC;

SELECT 
      B.APNT_NO
    , A.PT_NAME
    , A.PT_NO
    , B.MCDP_CD
    , C.DR_NAME
    , B.APNT_YMD
FROM PATIENT A, APPOINTMENT B, DOCTOR C
WHERE A.PT_NO = B.PT_NO
AND C.DR_ID = B.MDDR_ID
AND B.MCDP_CD = 'CS'
AND TO_CHAR(B.APNT_YMD, 'YYYY-MM-DD') = '2022-04-13'
AND B.APNT_CNCL_YN = 'N'
ORDER BY B.APNT_YMD
;