# docker-pyspark-try
## How To Try
at local computer

```
$ docker-compose up -d spark-master
$ docker exec -it spark-master bash
```

at docker container on local computer

```
# cd home
# python setup.py install
# python sample.py
```


## How to try jupyter notebok
at local computer

```
$ docker-compose up -d jupyter
```

Access to `http://localhost:8890` from web browser.

Login password for jupyter notebook is `12345678`.

Click `new` button and paste bellow script.


```
from pyspark import *
from pyspark.sql import *
from pyspark.sql.types import *

conf = SparkConf()
sc = SparkContext.getOrCreate(conf=conf)
sqlContext = SQLContext(sc)


df = sqlContext.read.format('com.databricks.spark.csv') \
    .options(header='true', inferschema='true') \
    .load('/home/jovyan/work/sample.csv') # this is your csv file

df.where('id < 3').show()
```

Click 'Run' button.
