import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://looqbox-challenge:looq-challenge@35.199.115.174:3306/looqbox-challenge"
)

def retrieve_data(product_code=None, store_code=None, date=None):

    query = """
        SELECT 
        
            DPS.STORE_CODE,
            DPC.STORE_NAME,

            DPS.PRODUCT_CODE,
            DP.PRODUCT_NAME,

            DPS.DATE,

            DPS.SALES_VALUE,
            DPS.SALES_QTY

        FROM `looqbox-challenge`.data_product_sales DPS

        INNER JOIN `looqbox-challenge`.data_store_cad DPC
            ON DPS.STORE_CODE = DPC.STORE_CODE

        INNER JOIN `looqbox-challenge`.data_product DP
            ON DPS.PRODUCT_CODE = DP.PRODUCT_COD

        WHERE 1=1
    """

    params = ()

    if product_code is not None:
        query += " AND DPS.PRODUCT_CODE = %s"
        params += (product_code,)

    if store_code is not None:
        query += " AND DPS.STORE_CODE = %s"
        params += (store_code,)

    if date is not None:
        query += " AND DPS.DATE BETWEEN %s AND %s"
        params += (date[0], date[1])

    query += " ORDER BY DPS.DATE"

    df = pd.read_sql(query, engine, params=params)

    return df


my_data = retrieve_data(
    product_code=18,
    store_code=1,
    date=["2019-01-01", "2019-03-31"]
)

print(my_data.head())
