# redistimeseries-pandas

Build a redistimeseries stream and analyze the data using Python Pandas

## Introduction

Redistimeseries is a append only log or stream of millisecond precision
timestamps and associated samples.

The timeseries can have JSON as samples and this project aims to use
redisJSON, rediSearch and OHM to manipulate time series samples and
build analytics and visualization.

## What is redis timeseries?

Redis Timeseries is a stream of samples built with the Rax data structure
and so is quite efficient. Even with a million records, it still takes
very little time to add samples.

We can only add future samples from the last stored value. Redis is an
ideal choice for many things including timeseries and it offers a rich
ecosystem with redisearch and JSON and all that. Along with Python
Pandas it is even more interesting.

## What is Pandas?

Pandas stands for Python Data science. And Pandas is written by Wes
McKinney and is one of the most widely used data analysis toolkit in
Python with many concepts from the R programming language.

And  Python also offers rich visualization using the matplotlib toolkit.
Pandas offers the most powerful dataframe using which we can effectively
model data, embed series and do powerful math operations on them.

There is also the most excellent numpy's data manipulation library to
create equally spaced timestamps upto the granularity of milliseconds
which is what redistimeseries supports anyway.

A simple command like this will do for us.

```
import pandas as pd
import numpy as np

dt = pd.date_range(start='2022-1-1', end='2022-3-3', freq='ms');

```

Then based on these timestamps you can either create an np array or
something and build a series and go about your timeseries analytics.

## Why this repo?

This goes with the blog on redis time series and has the code samples
needed to follow along the article.

## Contact and support

For all patches, PR and bugs contact girish(at) spamcheetah.com

