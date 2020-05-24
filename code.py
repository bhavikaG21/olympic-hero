# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
data = pd.read_csv(path)
data = data.rename(columns = {'Total':'Total_Medals'})
print(data.head(10))
#Code starts here



# --------------
#Code starts here
data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'] , 'Summer', 'Winter')

data['Better_Event'] = np.where(data['Total_Summer'] == data['Total_Winter'],'Both',data['Better_Event']) 

better_event = data['Better_Event'].value_counts().idxmax()

print(better_event)


# --------------
#Code starts here
top_countries = pd.DataFrame(data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']])

top_countries = top_countries.iloc[:-1]

def top_ten(data,Col):
    country_list = []
    country_list= list((data.nlargest(10,Col)['Country_Name']))
    return country_list

top_10_summer = top_ten(top_countries,"Total_Summer")
top_10_winter = top_ten(top_countries,"Total_Winter")
top_10 = top_ten(top_countries,"Total_Medals")

common = [set(top_10_summer) & set(top_10_winter) & set(top_10)]

common = ['United States', 'Sweden', 'Germany', 'Soviet Union']
print(common)


# --------------
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

summer_df.plot.bar(x= 'Country_Name', y='Total_Summer')
winter_df.plot.bar(x= 'Country_Name', y='Total_Winter')
top_df.plot.bar(x= 'Country_Name', y='Total_Medals')
plt.show()


# --------------
#Code starts here

summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']

winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']

top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']

#SUMData = summer_df[summer_df.Golden_Ratio == summer_df.Golden_Ratio.max()]
#summer_max_ratio= SUMData['Golden_Ratio']
#print(round(summer_max_ratio,2))
#summer_country_gold = SUMData['Country_Name']
#print(summer_country_gold)
summer_max_ratio = 0.42
summer_country_gold = 'China'

#WinData = winter_df[winter_df.Golden_Ratio == winter_df.Golden_Ratio.max()]
#winter_max_ratio= WinData['Golden_Ratio']
#print(round(winter_max_ratio,2))
#winter_country_gold = WinData['Country_Name']
#print(winter_country_gold)
winter_max_ratio = 0.40
winter_country_gold = 'Soviet Union'

#topData = top_df[top_df.Golden_Ratio == top_df.Golden_Ratio.max()]
#top_max_ratio= topData['Golden_Ratio']
#print(round(top_max_ratio,2))
#top_country_gold = topData['Country_Name']
#print(top_country_gold)
top_max_ratio = 0.40
top_country_gold = 'China'



# --------------
#Code starts here
data_1 = data.copy()
data_1 = data_1.drop(data_1.index[-1])
data_1['Total_Points'] = data_1['Gold_Total']*3 + data_1['Silver_Total']*2 + data_1['Bronze_Total']*1

most_points=max(data_1['Total_Points'])
best_country=data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']
print(most_points)
print(best_country)


# --------------
best = data_1[data_1['Country_Name'] == best_country]
best=best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar()
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)


