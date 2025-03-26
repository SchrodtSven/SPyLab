import geopandas as gpd
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
#plt.style.use('seaborn')

# zuordnung_plz_ort.csv

df = pd.read_json('data/nrw-plz.json')
print(df.results.iloc[0]['geometry'])

