from datetime import datetime, date
from pyspark.sql import Row

import os 

os.environ["PYARROW_IGNORE_TIMEZONE"] = "1"
from pyspark import pandas  as ps

df = ps.DataFrame([
     Row(a=1, b=2., c='String1', d= date(2000, 1, 1), e=datetime(2000, 1, 1, 12, 0)),
     Row(a=1, b=2., c='String2', d= date(2000, 2, 1), e=datetime(2000, 1, 2, 12, 0)),
     Row(a=1, b=2., c='String3', d= date(2000, 3, 1), e=datetime(2000, 1, 3, 12, 0))

])

print(df)