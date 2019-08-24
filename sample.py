from pyspark import *
from pyspark.sql import *
from pyspark.sql.types import *

conf = SparkConf()
sc = SparkContext.getOrCreate(conf=conf)
spark = SparkSession(sc)

test_scheme = StructType({
  StructField("id", IntegerType()),
  StructField("name", StringType()),
})

test_list = [
  (1, "spade"),
  (2, "hurt"),
  (3, "club"),
  (4, "diamond")
]

df = spark.createDataFrame(test_list, test_scheme)
df.show()
