import pandas as pd
import matplotlib.pyplot as plt

# フォントの設定
plt.rcParams["font.family"] = "Yu Gothic"

df = pd.read_csv("sample_data.csv")
df["日付"] = pd.to_datetime(df["日付"])
print("読み込んだ件数:",len(df),"件")

#年月のカラムを追加する
df["年月"] = df["日付"].dt.strftime("%Y-%m")
print("期間:", df["日付"].min().date(),"~",df["日付"].max().date())
#月別の支出合計を計算
month_total = df.groupby("年月")["金額"].sum()
print("---月別支出合計---")
print(month_total)
print()

plt.figure(figsize = (9,5))
month_total.plot(kind = "bar")
plt.title("月別支出合計")
plt.xlabel("年月")
plt.ylabel("金額(円)")
plt.tight_layout()
plt.savefig("month_total.png")
plt.close()

#カテゴリ別の支出合計を計算
category_total = df.groupby("カテゴリ")["金額"].sum()
category_total = category_total.sort_values(ascending = False)
print("---カテゴリ別支出合計---")
print(category_total)
print()

plt.figure(figsize = (9,5))
category_total.plot(kind = "bar")
plt.title("カテゴリ別支出合計")
plt.xlabel("カテゴリ")
plt.ylabel("金額(円)")
plt.tight_layout()
plt.savefig("category_total.png")
plt.close()

#カテゴリ別の平均支出額
category_mean = df.groupby("カテゴリ")["金額"].mean()
category_mean = category_mean.sort_values(ascending = False)
print("---カテゴリ別1回あたりの平均支出額---")
print(category_mean)
print()

plt.figure(figsize = (9,5))
category_mean.plot(kind = "bar", color = "orange")
plt.title("カテゴリ別　平均支出額(1回あたり)")
plt.xlabel("カテゴリ")
plt.ylabel("平均金額(円)")
plt.tight_layout()
plt.savefig("category_mean.png")
plt.close()

print("グラフを3枚保存しました")
print("month_total.png")
print("category_total.png")
print("category_mean.png")