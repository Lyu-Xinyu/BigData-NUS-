import pdb

############
# Exercise
############
# Q1 This question is test your understanding of Python Basics.
#   a) What is 8 to the power 4?
x = lambda a : a**4
print(x(8))
#   b) Split this string “Split this string”
my_string = "Split this string"
print(my_string.split())
#   c) Given the variables: planet = “Earth”, diameter = 12742, use .format() to print the following string “The diameter of Earth is 12742 kilometers.”
planet = "Earth"
diameter = 12742
print('The diameter of {} is {} kilometers.'.format(planet,diameter))
#   d) Given the name list, use indexing to grab word “target”, the_list = [1,2,[3,4],[5,[100,200,['target']],23,11],1,7]
the_list = [1,2,[3,4],[5,[100,200,['target']],23,11],1,7]
print(the_list[3][1][2])
#   e) Given this nest dictionary grab the work “hello”. The_dic = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
The_dic = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
print(The_dic.get('k1')[3].get('tricky')[3].get('target')[3])
#   f) Create a basic function that returns True if the word 'elephant' is contained in the input string.
#   Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization.
def contains_elephant(string):
    return 'elephant' in string.lower()
#   g) Create a function that counts the number of times the word "elephant" occurs in a string. Again ignore edge cases.
def count_elephants(string):
    return string.lower().count("elephant")

# Q2 This question is test your understanding of PySpark operations on DataFrame.
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

# a) Create a PySpark DataFrame based on the given RDD.
my_schema = ["employee_name","department","state","salary","age","bonus"]
df = spark.createDataFrame(data=my_data, schema = my_schema )
# b) Show data and print schema
df.show()
df.printSchema()
# c) Run groupBy() on “department” columns. Calculate aggregates like minimum, maximum, average, total salary for each group using min(), max(), avg() and sum() aggregate functions respectively.
df.groupBy("department").min("salary").show()
df.groupBy("department").max("salary").show()
df.groupBy("department").avg("salary").show()
# d) Run groupBy() on “country” columns. Calculate aggregates like minimum, maximum, average, total salary for each group using min(), max(), avg() and sum() aggregate functions respectively.
df.groupBy("country").min("salary").show()
df.groupBy("country").max("salary").show()
df.groupBy("country").avg("salary").show()