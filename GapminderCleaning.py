# %% markdown
# # Data Cleaning - Gapminder dataset
# %% markdown
# ### This is a dataset pulled from gapminder
# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %%
gapminder = pd.read_csv('life_expectancy_years.csv')
# %% markdown
# ### The first thing is to do some exploratory analysis to have a general idea od the data
# %%
gapminder.head()
# %%
gapminder.shape
# %%
gapminder.info()
# %%
gapminder.columns
# %%
# As we can see, we have values stored as columns. The approach here is to transform the dataset to have a column called year|
# %%
gapminder_long = pd.melt(gapminder, id_vars = 'country', var_name = 'year', value_name = 'life_expectancy')
# %%
gapminder_long.head()
# %%
gapminder_long.shape
# %%
gapminder_long.dtypes
# %%
# As we can see, the column year is from object type. Let's change it to numeric so we can perform calculations later in
# the analysis.
gapminder_long['year'] = pd.to_numeric(gapminder_long['year'], errors = 'coerce')
# %%
gapminder_long.head(3)
# %%
gapminder_long.dtypes
# %%
gapminder_long.describe()
# %%
gapminder_long.drop_duplicates()
# %%
# As we can see, there are no duolicates. However, the minimum value for life expectancy (1.0 years) is concerning
# and needs to be investigate further.
# %%
col = gapminder_long['life_expectancy']
# %%
col.head()
# %%
col[np.abs(col)<20]
# %%
# We have 174 entries where life_expectancy is less than 20 years. In some cases we have life expectancy of less than 10 years.
# Since we are talking about 174 rows out of over 40,000, it's safe to drop them as outliers that don't make sense.
# %%
names = gapminder_long[gapminder_long['life_expectancy'] < 20].index
# %%
gapminder_long.drop(names, inplace=True)
# %%
gapminder_long.shape
# %%
gapminder_long = gapminder_long.reset_index(drop = True)
# %%
gapminder_long.head()
# %%
# Summary of what was done:
# 1. We delt with the issue of having values stored as columns
# 2. We changed the year column datatype from object to int64 (integer)
# 3. We verified that there are not duplicates
# 4. We eliminated outliers that didn't make sense
# %% markdown
# ### Now, we need to take care of the last step, which is to deal with missing data
# %%
# Let's have a general idea of how many missing values we are dealing with
# %%
gapminder_long.isnull().sum().sum()
# %%
gapminder_long.isnull().sum()
# %%
# We have a total of 516 missing values out of over 40,000 observations. They are all in the life_expectancy column.
# %%
516 * 100 / 40779
# %%
# It's just 1.27% of our data, so we can simply drop them
# %%
gapminder_long.dropna(subset = ['life_expectancy'], how = 'any', inplace=True)
# %%
gapminder_long.shape
# %%
gapminder_long.sample(30)
# %%
# To save the dataset for future analysis:
# %%
gapminder_long.to_csv('gapminder_clean.csv')
