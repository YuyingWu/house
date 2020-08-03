import pandas as pd
import matplotlib.pyplot as plt

houses = pd.read_csv('./houses.csv')
houseData = houses[houses["district"].isna() == False][["district", "month_avg_price", "date"]]
print(houseData)

# houseData["date"] = pd.to_datetime(houseData["date"], format="%y-%m")

fig, ax = plt.subplots()

houseBinjiang = houseData[houseData["district"] == "滨江"]
houseXihu = houseData[houseData["district"] == "西湖"]

ax.plot(houseBinjiang["date"], houseBinjiang["month_avg_price"], color="b")
ax.plot(houseXihu["date"], houseXihu["month_avg_price"], color="r")

ax.set_title("Hangzhou")
ax.set_xlabel("Date")
ax.set_ylabel("Price / Month")

plt.show()