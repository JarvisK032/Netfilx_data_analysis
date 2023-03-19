#%%

import pandas as pd
import altair as alt

# Load the dataset
netflix_data = pd.read_csv('netflix_titles.csv')

netflix_data.columns
#%%
# Question 1: What is TV shows release in 2021 and their duration?

# Filter the data to only include TV shows released in 2021
tv_data = netflix_data[(netflix_data['type'] == 'TV Show') & (netflix_data['release_year'] == 2021)]

# Create a chart showing the duration of TV shows released in 2021
chart = alt.Chart(tv_data).mark_bar().encode(
    x='duration',
    y=alt.Y('title', sort='-x'),
    tooltip=['title', 'duration']
).properties(
    title='TV Shows Released on Netflix in 2021 and Their Duration',
    width=600
)
chart



#%%

# Question 2: What is the number of movies released in each year from 2000 from 2021?

# Filter the data to only include movies
movies_data = netflix_data[netflix_data['type'] == 'Movie']

# Count the number of movies released each year from 2018 to 2021
movies_by_year = movies_data['release_year'].value_counts().sort_index().reset_index().rename(columns={'index': 'year', 'release_year': 'count'})
movies_by_year = movies_by_year[movies_by_year['year'] >= 2000]

# Create a chart showing the number of movies released in each year
chart = alt.Chart(movies_by_year).mark_bar().encode(
    x='year:O',
    y='count',
    tooltip=['year', 'count']
).properties(
    title='Number of Movies Released on Netflix by Year',
    width=600
)
chart


# %%
# Question 3: What is the number of TV shows released in each year from 2000 from 2021?

# Filter the data to only include TV Shows
TV_Show_data = netflix_data[netflix_data['type'] == 'TV Show']

# Count the number of movies released each year from 2018 to 2021
TV_Shows_by_year = TV_Show_data['release_year'].value_counts().sort_index().reset_index().rename(columns={'index': 'year', 'release_year': 'count'})
TV_Shows_by_year = TV_Shows_by_year[TV_Shows_by_year['year'] >= 2000]

# Create a chart showing the number of movies released in each year
chart = alt.Chart(TV_Shows_by_year).mark_bar().encode(
    x='year:O',
    y='count',
    tooltip=['year', 'count']
).properties(
    title='Number of Movies Released on Netflix by Year',
    width=600
)
chart
# %%

#Question 4: What is the top 10 countries with the highest count of TV shows produced?

# Filter the data to only include TV shows
tv_data = netflix_data[netflix_data['type'] == 'TV Show']

# Count the number of TV shows produced in each country
tv_by_country = tv_data['country'].value_counts().reset_index().rename(columns={'index': 'country', 'country': 'count'})

# Select only the top 10 countries with the highest count
tv_by_country = tv_by_country.head(10)

# Create a chart showing the number of TV shows produced in each country
chart = alt.Chart(tv_by_country).mark_bar().encode(
    x=alt.X('country:N', sort='-y'),
    y='count',
    tooltip=['country', 'count']
).properties(
    title='Top 10 Countries with the Most TV Shows Produced',
    width=500
).configure_axisX(
    labelAngle=-45
)

chart


# %%
#Question 5: What is the top 10 countries with the highest count of movies produced?

# Filter the data to only include movies
movies_data = netflix_data[netflix_data['type'] == 'Movie']

# Count the number of movies produced in each country
movies_by_country = movies_data['country'].value_counts().reset_index().rename(columns={'index': 'country', 'country': 'count'})

# Select only the top 10 countries with the highest count
movies_by_country = movies_by_country.head(10)

# Create a chart showing the number of movies produced in each country
chart = alt.Chart(movies_by_country).mark_bar().encode(
    x=alt.X('country:N', sort='-y'),
    y='count',
    tooltip=['country', 'count']
).properties(
    title='Top 10 Countries with the Most Movies Produced',
    width=500
).configure_axisX(
    labelAngle=-45
)

chart
# %%
