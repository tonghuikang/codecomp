# Big data reference

(To be moved to another repository. I should make it a standard toolset)

Refer to methyldragon for a compiled snippets for [numpy]([https://github.com/methylDragon/python-data-tools-reference/blob/master/Numpy/01%20Numpy%20Basics.md](https://github.com/methylDragon/python-data-tools-reference/blob/master/Numpy/01 Numpy Basics.md)) and [pandas]([https://github.com/methylDragon/python-data-tools-reference/blob/master/Pandas/01%20Pandas%20Basics.md](https://github.com/methylDragon/python-data-tools-reference/blob/master/Pandas/01 Pandas Basics.md)).

Here I document some snippets and comments that were useful for my internship.



A `pd.Series` is not a `pd.DataFrame`. A Series is a column, while a DataFrame is a table. Each of them have different functions.



## Reading and writing

Here we explain how to write a csv file


```python
pd.read_csv(csv_filepath)
```

If the csv has an index

```python
pd.read_csv(csv_filepath, index_col=0)
```

You should not save the DataFrame with an index unless specifically required.

```python
df.to_csv(index=False)
```



## Datetime manipulation 

Consider Python in-built datetime object.

Parsing time

Usually time objects are saved as string in the csv files in varying formats. Does the dataframe parse time from string by default.

To parse time, please use

```
df["time"]
```

Issues with tz-aware. (Depending on pandas version?)

Sometimes the data have the timezone info but you want to remove it.
```

```


Converting epoch time to standard time. Sometimes to minimise memory storage and improve performance time may be presented in the form of an integer. You need to be able to convert it both ways.

The difference between datetime and duration.




