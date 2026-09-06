# Initialize Spark session
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DateType
from pyspark.sql.functions import sum
spark = SparkSession.builder.appName('Spark Playground').getOrCreate()
schema=StructType([StructField("customer_id",IntegerType(),True), StructField("name",StringType(),True), StructField("product_id",IntegerType(),True), StructField("purchase_date",DateType(),True), StructField("purchase_amount",IntegerType(),True)])
df=spark.read.option("header",True).schema(schema).csv("/datasets/customer_purchases.csv")
df_result=df.groupBy("customer_id").agg(sum("purchase_amount").alias("total_purchase"))
df_result=df_result.orderBy("customer_id")

# Display the final DataFrame using the display() function.
display(df_result)