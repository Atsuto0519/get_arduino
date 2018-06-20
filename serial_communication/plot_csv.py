import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

openfile = '2018-06-20_1.csv'
savefig = '2018-06-20_1.png'

df = pd.read_csv(openfile)

# time列で重複した行を、初めの行のみにたたみ込む
# df_zip = df.drop_duplicates(subset="time")
df_zip = df
df_zip.time = pd.to_datetime(df_zip.time)
df_zip.temperature = df_zip.temperature.convert_objects(convert_numeric=True)

mean = df_zip['temperature'].mean()
var = df_zip['temperature'].var(ddof=False)

df_zip = df_zip.set_index('time')

df_zip.plot()
plt.grid()
# 1σ（全体の68%）が収まるようにしてみた
plt.ylim(mean-0.5*var, mean+0.5*var)
plt.savefig(savefig)

print(df_zip)
