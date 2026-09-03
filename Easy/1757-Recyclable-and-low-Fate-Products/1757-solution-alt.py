#SQL to pySpark
#Without pandas dataframe
#Spark Session
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('pyspark_soln').getOrCreate()

# 1. Define data (Products table)
data = [(0,'Y','N'), (1,'Y','Y'),(2,'N','Y'),(3,'Y','Y'),(4,'N','N')]

# 2. Define schema types
from pyspark.sql.types import IntegerType, StringType, StructField, StructType
schema = StructType([StructField('product_id', IntegerType(), True),
                     StructField('low_fats', StringType(), True),
                     StructField('recyclable', StringType(), True)])


# 3. Create Spark dataframe
prod_sp_df = spark.createDataFrame(data, schema)
##display(prod_sp_df)

# 4. Filtered dataframe
prod_sp_df.createOrReplaceTempView('Products')
spark.sql('''
select product_id from products where low_fats="Y" and recyclable="Y";
''').show()

