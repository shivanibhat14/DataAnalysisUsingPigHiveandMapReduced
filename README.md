# DataAnalysisUsingPig,HiveandMapReduced
Stack exchange comprises of Q&A posted by communities majorly stack overflow. Data from stack exchange manifests questions posted from diverse fields. Others read, comment and score the questions posted. 
Link to stack exchange data: 
Queries are run at the link provided to retrieve files (.csv) . We can only fetch 50K rows at a time. The assignment required me to retrive around 2 lakh rows, for which I ran 4 queries with respect to VIEWCOUNT.
 
Step 1:
Data Retrival:


1) select top 50000 * from posts where posts.ViewCount > 28574 order by posts.ViewCount DESC 

2) select top 50000 * from posts where posts.ViewCount <= 86658 order by posts.ViewCount DESC 

3) select top 50000 * from posts where posts.ViewCount <= 51008 order by posts.ViewCount DESC 

4) select top 50000 * from posts where posts.ViewCount <= 36583 order by posts.ViewCount DESC 

On running of the above queries, 4 CSV files worth of data was downloaded. This data is ready for further processing.

Step 2:
Load data using PIG:


Data downloaded contains multiple collumns with somme messy data which requires cleaning before uploading it to HDFS to run queries.
CleanData.py file is run to clean the body of the file containing delimiters which otheriwse throws errors while loading the file to PIG. The regular expressions should be removed. After cleaning, The four csv files are loaded using PIG and concatinated using UNION function. For further handling, the dataset is restricted to only few required  columns and the columns which do not contain NULL values. The data is now loaded to HDFS for precessing with HIVE

Step 3:
Querying with HIVE:


After the data is loaded to HDFS, queries provided are run to retrieve the posts and users. CREATE hive queries are used here. 


The tasks mentioned above were run on GCP console by creating a daatproc or cluster with a master node and reducer nodes. asia-east region was used to create the cluster as it was closer to India

Reference: 

Stackoverflow: https://stackoverflow.com/


GitHub for data cleaning: https://github.com/arunabellgutteramesh/PigHiveOnStackExchangeData/blob/master/code/ETL/fetchValidRecords.pig
