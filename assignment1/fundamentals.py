import certifi
import ssl
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import geopy.geocoders
import geopy.location
from geopy.geocoders import Nominatim

article_info_df = pd.read_csv("articleInfo.csv")
author_info_df = pd.read_csv("authorInfo.csv")

#SECTION ONE

merge_df = pd.merge(article_info_df, author_info_df, on='Article No.')
merge_df = merge_df.fillna(0)

fig, ax = plt.subplots(2, 1)

#1
merge_df["Year"].value_counts().plot(title="Articles Published by Year",ax=ax[0], kind="line", ylabel="Number of Publications")

#2
df = merge_df.groupby(["Year"]).sum(numeric_only=True)
df.plot(title= "Number of Citations by Year", ax=ax[1], y="Citation", use_index=True, ylabel="Number of Citations")

#3
ctx = ssl.create_default_context(cafile=certifi.where())
geopy.geocoders.options.default_ssl_context = ctx
geolocator = Nominatim(scheme='http',user_agent="jake_mmml_app")
long, lat = [], []
for country in merge_df["Country"]:
    location = geolocator.geocode(country)
    long.append(location.longitude)
    lat.append(location.latitude)
plt.plot(x=long, y=lat)
plt.show()


#4
