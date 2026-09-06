
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when
from pyspark.sql import Window as W

spark = SparkSession.builder.appName('Spark Playground').getOrCreate()

# Assume the dataframes employees, payroll are already initialized.

# Write the logic and display the final dataframe

df=employees.join(payroll,on="employee_id",how="inner")
df=df.withColumn("pay",when(col("hours_worked")<=40,col("hours_worked")*col("hourly_rate")).otherwise(40*col("hourly_rate")+(col("hours_worked")-40)*col("hourly_rate")*1.5))
df_result=df.select("employee_id","name","position","pay")

display(df_result)
    