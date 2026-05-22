import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://looqbox-challenge:looq-challenge@35.199.115.174:3306/looqbox-challenge"
)

query = "SELECT * FROM data_product_sales LIMIT 10"

df = pd.read_sql(query, engine)

print(df.head())