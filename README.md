# expense-analysis

pandas・matplotlibを使った支出データ分析(個人情報を含まないダミーデータで作成)

## ファイル構成

| ファイル名 | 役割 |
|---|---|
| `sample_data.csv` | 分析用のダミー支出データ(270件) |
| `data_analysis.py` | `sample_data.csv` を読み込み、月別・カテゴリ別に集計してグラフを出力するスクリプト |

実際の自分の支出データは個人情報のため含めておらず、上記のダミーデータで動作確認できるようにしています。

## 実行方法

```bash
pip install pandas matplotlib
python3 data_analysis.py
```

実行すると、以下の3枚のグラフがフォルダ内に保存されます。

- `month_total.png` — 月別支出合計
- `category_total.png` — カテゴリ別支出合計
- `category_mean.png` — カテゴリ別の平均支出額(1回あたり)

## 使用技術

- Python
- pandas(CSV読み込み・集計)
- matplotlib(グラフ描画)
