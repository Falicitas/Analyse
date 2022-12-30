from main import *

para_data = currency_data[currency_data["Date"] == "3/17/2022"][["Currency Code", "Currency Name", "Exchange Rate"]] 
merged_data = pd.merge(survey_data, para_data, left_on="Currency", right_on="Currency Code", how="outer", sort=False)
real_data = merged_data[merged_data["ConvertedToDollar"] < 1000000.000]

grouped_columns = np.array(real_data.iloc[:, np.where(real_data.columns.str.startswith("DevType") == True)[0][1:]].columns)
grouped_columns = np.delete(grouped_columns, -8)
grouped_columns = np.append(grouped_columns, ["ConvertedToDollar"])

for i in grouped_columns:
    plt.figure(figsize=(15,10))
    circle = plt.Circle((0,0),0.5,color = "white")
    plt.pie(np.array(real_data[real_data[i] == 1]["Age"].value_counts(normalize=True).values[:5]), labels = np.array(real_data[real_data[i] == 1]["Age"].value_counts(normalize=True).index[:5]), colors = ["red","green","blue","cyan", "yellow"], autopct='%.2f')
    p = plt.gcf()
    p.gca().add_artist(circle)
    plt.title("{} age distribution".format(i[8:]))
    plt.show()