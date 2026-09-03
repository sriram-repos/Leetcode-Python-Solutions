#----------------------------------------#
#Leetcode 1757 solution using PySpark
#SQL to pySpark
#----------------------------------------#

# 1. Define data (Products table)
import pandas as pd
data = [(0,'Y','N'), (1,'Y','Y'),(2,'N','Y'),(3,'Y','Y'),(4,'N','N')]

# 2. Define schema types
products = pd.DataFrame(data, columns=['product_id', 'low_fats', 'recyclable']).astype(
    {'product_id': 'int64', 'low_fats': 'category', 'recyclable': 'category'})

#Spark Session
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()

# 3. Create Spark dataframe
prod_sp_df = spark.createDataFrame(products)
##display(prod_sp_df)

# 4. Filtered dataframe
prod_sp_df.createOrReplaceTempView('Products')
spark.sql('''
select product_id from products where low_fats="Y" and recyclable="Y";
''').show()
