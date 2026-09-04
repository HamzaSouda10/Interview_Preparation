# Initialize Spark session
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, DoubleType, StringType, IntegerType
spark = SparkSession.builder.appName('Spark Playground').getOrCreate()
schema=StructType([StructField("customer_id",DoubleType(),True),StructField("name",StringType(),True),StructField("email",StringType(),True),StructField("age",IntegerType(),True)])
#Copy the starter code or load the file path available in the problem statement 
df=spark.read.schema(schema).option("header",True).csv("/datasets/customers_raw.csv")
df_result=df.filter((df['email'].isNotNull()) & (df['customer_id'].isNotNull()))
# Display the final DataFrame using the display() function.
display(df_result)