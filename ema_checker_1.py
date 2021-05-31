import pandas_ta as ta
import pandas as pd
import numpy as np

data = np.random.randint(2,9,(20))

data_list = data.tolist()
# print(data.tolist())
print(data_list)

df = pd.DataFrame(data, columns = ['numbers'])
# pd.options.display.float_format = '${:,.2f}'.format
# df['ema'] = df.ewm(span = 3).mean()
# df['ema'] = df['ema'].map('{:,.2f}'.format)
df['ema'] = ta.sma(df['numbers'], length = 9)
df['ema'] = df['ema'].map('{:,.2f}'.format)
print(df)
current_ema = df['ema'].iloc[-1]
print(current_ema)

