# Variable Assignment
# variable can not start with number or special characters
print("Variable Assignment: ")
x = 2
print("x is {} ".format(x))
# String
print("String:")
my_str = 'my string'
my_str2 = "what's this?"
print(my_str)
print(my_str2)
# printing
num = 5
name = "Fan"
print('My number is: {one}, and my name is {two}'.format(one=num,two=name))
print('My number is: {}, and my name is {}'.format(num,name))
# Lists
my_list = ['a','b','c','d']
my_list.append('e')
print(my_list)
my_list[0] = 'new'
print(my_list)
nest_list = [1,2,3,[3,5,['target']]]
print(nest_list[3][2][0])
# Dictionaries
my_dic = {'k1':'val1','k2':'val2'}
print(my_dic['k1'])
# Tuple, tuple is immutable
my_tup = (1,2,3,4)

# if statements
if 1 < 2:
    print('correct')
if 1 < 2:
    print('correct')
else:
    print('wrong')
if 1 == 2:
    print("first")
elif 3 == 3:
    print("middle")
else:
    print('last')

# for loops
seq = [1,2,3,4,5]
for item in seq:
    print(item)

# While loops
i = 1
while i< 5:
    print('i is :{}'.format(i))
    i = i+1

# functions
def my_func(param1 = 'default'):
    """Dosstring goes here"""
    print(param1)

my_func()
my_func('new param')

# functions: Lambda expression
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

# methods
my_string = 'Welcome to PyCharm course'
print(my_string.lower())
print(my_string.upper())
print(my_string.split())

###########
# Spark DataFrame Basics
###########
from pyspark.sql import SparkSession

# Start the SparkSession
spark = SparkSession.builder.appName("Basics Stats").getOrCreate()
# Read people.json file
df = spark.read.json(r'C:\Users\27425\Desktop\Big Data\Practice Workshop\Python Scripts and Data\BasicStats\people.json')
# showing data
df.show()
# print schema
df.printSchema()
df.columns
df.describe()
# Retrieve data
df['age']
df.select('age').show()
# Returns list of Row objects
df.head(2)
# Return multiple columns
df.select(['age','name']).show()
# Adding a new column with a simple copy
df.withColumn('newage',df['age']).show()
df.withColumnRenamed('name','given_name').show()
df.withColumn('doubleage',df['age']*2).show()


############
# Groupby and Aggregate Operations
############
from pyspark.sql import SparkSession
# Start Spark Session
spark = SparkSession.builder.appName("groupbyagg").getOrCreate()
# Read sales data
df = spark.read.csv(r'C:\Users\27425\Desktop\Big Data\Practice Workshop\Python Scripts and Data\BasicStats\sales_info.csv',inferSchema=True,header=True)
df.printSchema()
df.show()
# Group by company
df.groupBy("Company")
# Returns a GroupedData object, off of which you can all various methods
# Mean
df.groupBy("Company").mean().show()
# Count
df.groupBy("Company").count().show()
# Max
df.groupBy("Company").max().show()
# Min
df.groupBy("Company").min().show()
# Order by sales ascending
df.orderBy("Sales").show()
# Descending call off the column itself.
df.orderBy(df["Sales"].desc()).show()


############
# Missing Data
############
from pyspark.sql import SparkSession
# Start SparkSession
spark = SparkSession.builder.appName("missingdata").getOrCreate()
df = spark.read.csv(r"C:\Users\27425\Desktop\Big Data\Practice Workshop\Python Scripts and Data\BasicStats\ContainsNull.csv",header=True,inferSchema=True)
df.show()
# Drop any row that contains missing data
df.na.drop().show()
# Has to have at least 2 NON-null values
df.na.drop(thresh=2).show()
# Drop row “Sales” contains missing data
df.na.drop(subset=["Sales"]).show()
# Drop any row contains missing data
df.na.drop(how='any').show()
# Drop those rows contains missing data for all columns
df.na.drop(how='all').show()

# Fill missing data point
# Fill missing data with “NEW VALUE” for string data type only
df.na.fill('NEW VALUE').show()
# Fill missing data with 0 for numeric data type only
df.na.fill(0).show()
# Fill missing data in row “Name” with “No Name”
df.na.fill('No Name',subset=['Name']).show()
# Fill values with mean value for column “Sales”
import pyspark.sql.functions as F
mean_val = df.select(F.mean(df['Sales'])).collect()
# Weird nested formatting of Row object!
mean_val[0][0]
mean_sales = mean_val[0][0]
df.na.fill(mean_sales,["Sales"]).show()


