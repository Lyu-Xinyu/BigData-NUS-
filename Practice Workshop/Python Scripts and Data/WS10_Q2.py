from pyspark.sql import SparkSession
import pyspark.sql.functions as F
from pyspark.sql.functions import col,sum,avg,max

spark = SparkSession.builder.appName('SparkExercise').getOrCreate()
my_data =[("James","Sales","SG",70000,34,10000),
   	    ("Michael","Sales","SG",66000,56,20000),
    	("Robert","Sales","MY",61000,30,23000),
    	("Maria","Finance","MY",60000,24,23000),
    	("Raman","Finance","USA",79000,40,24000),
    	("Scott","Finance","USA",63000,36,19000),
    	("Jen","Finance","UK",89000,53,15000),
    	("Jeff","Marketing","UK",70000,25,18000),
    	("Alice","Marketing","UK",78000,50,21000),
        ("Ada","IT","SG",83000,35,11000),
        ("Jackson","IT","MY",71000,30,21000),
        ("Cooper","IT","UK",91000,40,21000)]

my_schema = ["employee_name","department","state","salary","age","bonus"]
df = spark.createDataFrame(data=my_data, schema = my_schema )
df.show()
df.printSchema()
df.groupBy("department").min("salary").show()
df.groupBy("department").max("salary").show()
df.groupBy("department").avg("salary").show()