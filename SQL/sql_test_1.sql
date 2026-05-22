SELECT * FROM `looqbox-challenge`.data_product;

-- What are the 10 most expensive products in the company?

SELECT DISTINCT 
    PRODUCT_NAME, 
    PRODUCT_VAL 
FROM `looqbox-challenge`.data_product 
	WHERE PRODUCT_COD IS NOT NULL 
	ORDER BY PRODUCT_VAL DESC LIMIT 10 ;
    

