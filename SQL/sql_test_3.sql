-- What was the total sale of products (in $) of each Business Area in the first quarter of 2019?

SELECT * FROM `looqbox-challenge`.data_product_sales;
SELECT * FROM `looqbox-challenge`.data_store_cad;
SELECT * FROM `looqbox-challenge`.data_product;

SELECT 
    DPC.BUSINESS_NAME AS BUSINESS_NAME,
    CONCAT(
        '$',
        FORMAT(SUM(DPS.SALES_VALUE), 2)
    ) AS SALE_AMOUNT
FROM `looqbox-challenge`.data_product_sales DPS
	INNER JOIN `looqbox-challenge`.data_store_cad DPC
		ON DPS.STORE_CODE = DPC.STORE_CODE
	INNER JOIN `looqbox-challenge`.data_product DP
		ON DPS.PRODUCT_CODE = DP.PRODUCT_COD
WHERE DPS.DATE BETWEEN '2019-01-01' AND '2019-03-31'
GROUP BY DPC.BUSINESS_NAME
ORDER BY SALE_AMOUNT DESC
