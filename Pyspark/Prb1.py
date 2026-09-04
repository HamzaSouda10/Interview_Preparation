# Initialize Spark session
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Spark Playground').getOrCreate()
df=spark.read.option("header",True).option("inferSchema",True).csv("/datasets/customers.csv")
df=df.filter((df['purchase_amount']>100) & (df['age']>=30))
df_result=df.select("customer_id","name","purchase_amount")
#Copy the starter code or load the file path available in the problem statement 

# Display the final DataFrame using the display() function.
display(df_result)