import requests
import numpy as nm
import pandas as pd
from flask import Flask, request
from flask import render_template

app = Flask(__name__)

# 検索処理


@app.route('/')
def index():
    return "Hello Flask"


@app.route("/rakutenapi", methods=['GET', 'POST'])
def form():

    #　データが送られてきたときの処理
    if request.method == 'POST':
        if request.form['keyword']:
            keyword = request.form['keyword']
            url = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20140222'
            appId = '1068276949878974132'

            payload = {
                'format': "json",
                'applicationId': appId,
                'keyword': keyword,
                'hits': 10,
                'sort': '+itemPrice',
                'page': 1
            }

            response = requests.get(url, params=payload)
            result = response.json()

            print("検索結果 =", )
            print('-'*40)

        # リスト作成
            item_key = ['itemName', 'itemPrice',
                        'shopName', 'postageFlag', 'itemUrl']
            item_list = []

            for i in range(0, len(result['Items'])):
                tmp_item = {}
                item = result['Items'][i]['Item']
                for key, value in item.items():
                    if key in item_key:
                        tmp_item[key] = value
                item_list.append(tmp_item.copy())

         # データフレームを作成
            items_df = pd.DataFrame(item_list)
            items_df = items_df.reindex(columns=['itemName', 'itemPrice',
                                                 'shopName', 'postageFlag', 'itemUrl'])
            items_df = items_df.rename(columns={'itemName': '商品名', 'itemPrice': '商品価格',
                                                'shopName': '店舗名', 'postageFlag': '出荷日時フラグ', 'itemUrl': '楽天へGO'})

            items_table = items_df.to_html(
                classes=["table", "table-bordered", "table-hover"])
        return render_template('rakutenapi.html', keyword=keyword, items_table=items_table)
    #  　初期表示
    else:
        return render_template("rakutenapi.html")


if __name__ == "__main__":
    app.run(port=12346, debug=True)
