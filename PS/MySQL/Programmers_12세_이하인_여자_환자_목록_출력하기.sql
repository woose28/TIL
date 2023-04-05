SELECT P.PT_NAME, P.PT_NO, P.GEND_CD, P.AGE, IF(P.TLNO IS NULL, 'NONE', P.TLNO) as TLNO FROM PATIENT as P WHERE P.AGE <= 12 AND P.GEND_CD = "W" ORDER BY P.AGE DESC, P.PT_NAME ASC