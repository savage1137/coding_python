import pandas as pd
data1={
    "name":['Sayan','toufique','asa'],
    "roll":[137,165,131],
    "marks":[44,45,46]
}
data2={
    "name":['Sayan','toufique','asa'],
    "roll":[137,165,131],
    "attendance":["20%","50%","60%"]
}

df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)
merge=pd.merge(df1,df2,on=["roll","name"],how="outer")
print(merge)
