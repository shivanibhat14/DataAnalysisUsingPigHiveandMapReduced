#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import re

filename=pd.read_csv("QueryResults.csv")
data=pd.DataFrame(filename)

data['Body'] = data['Body'].apply(body: re.sub('<.*?>|\\t*\\r*\\n*\\s+',' ',body));
data['Title'] = data['Title'].apply(title: re.sub('<.*?>|\\t*\\r*\\n*\\s+',' ',title));
data.to_csv("QueryResultsClean.csv")

#This code was run for all the csv files and the cleaned data was stored respectively for appending.
