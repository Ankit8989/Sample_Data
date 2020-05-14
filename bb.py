import pandas as pd
from nsepy import get_history
from datetime import date
import scipy.stats as st

data_Sunpharm=get_history(symbol='RELIANCE', start=date(2020, 1, 1), end=date(2020,5, 11))


d=data_Sunpharm[['Close']]
d.mean()
a=data_Sunpharm.tail(7)
a[['Open','Close','Low','High']]
a_diff1=a['High']-a['Low']
a_diff1
a_diff2=a['Close']-a['Open']
a_diff2

d['Return']=d['Close'].pct_change()
sd=d['Return'].std()
sd_Close=d['Close'].std()
m=d['Return'].mean()
z=st.norm.ppf(.95)


last_vl=d['Close'].tail(1)
per_val=last_vl*z*sd

low_value=last_vl-per_val
High_value=last_vl+per_val

print("Low Value : ",low_value)
print("High Value: ",High_value)
