-- What sections do the 'BEBIDAS' and 'PADARIA' departments have?

SELECT * FROM `looqbox-challenge`.data_product;

SELECT DISTINCT 
	DEP_COD,
    DEP_NAME
FROM `looqbox-challenge`.data_product 
	ORDER BY DEP_COD;

-- BEBIDAS = 2 & PADARIA = 7

SELECT DISTINCT
	SECTION_COD,
    SECTION_NAME
FROM `looqbox-challenge`.data_product
	WHERE DEP_COD = 2 OR 7 
    ORDER BY SECTION_COD;
    
