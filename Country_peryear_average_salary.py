from main import *

para_data = currency_data[currency_data["Date"] == "3/17/2022"][["Currency Code", "Currency Name", "Exchange Rate"]] 
merged_data = pd.merge(survey_data, para_data, left_on="Currency", right_on="Currency Code", how="outer", sort=False)
# merged_data.info()
merged_data[(~merged_data["Currency"].isna()) & (merged_data["Currency Code"].isna())].index
def conversion(index):
    if (merged_data.loc[index, "CompFreq"] == "Weekly"):
        merged_data.loc[index, "ConvertedToDollar"] = merged_data.loc[index, "CompTotal"] * 52 * merged_data.loc[index, "Exchange Rate"]
    elif (merged_data.loc[index, "CompFreq"] == "Monthly"):
        merged_data.loc[index, "ConvertedToDollar"] = merged_data.loc[index, "CompTotal"] * 12 * merged_data.loc[index, "Exchange Rate"]
    elif (merged_data.loc[index, "CompFreq"] == "Yearly"):
        merged_data.loc[index, "ConvertedToDollar"] = merged_data.loc[index, "CompTotal"] * 1 * merged_data.loc[index, "Exchange Rate"]
    
for i in merged_data.index:
    conversion(i)
plt.figure(figsize=(15, 15))
plt.plot(survey_data[["Country", "CompTotal"]].groupby("Country").agg(np.mean).sort_values(by="CompTotal", ascending=False)[:50])
plt.xticks(rotation=90)
plt.show()
real_data = merged_data[merged_data["ConvertedToDollar"] < 1000000.000]
real_data.drop(real_data[real_data["DevType"].str.count(";") > 6].index, axis=0, inplace=True)
real_data.drop(real_data[real_data["DevType"].isna()].index, inplace=True)
country_df = real_data[["Country", "ConvertedToDollar"]].groupby("Country").agg(np.mean).sort_values("ConvertedToDollar", ascending=False)
plt.figure(figsize=(10, 10))
plt.title("Salaries by Country in Dollars($)")
sns.barplot(y=country_df.index[:20], x=country_df["ConvertedToDollar"][:20], palette="Greens_r")
plt.show()