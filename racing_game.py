import random
import time

import streamlit as st

# タイトルと説明
st.title('亀のレース！')
st.write('どの色の亀が勝つか予想して、レースの結果を見てみましょう！')

# 亀の色を定義（画像ファイル名と対応）
colors = ["red", "green"]
turtle_images = {
    "red": "red.png",
    "green": "green.png",
    # "blue": "blue_turtle.png",
    # "yellow": "yellow_turtle.png",
    # "purple": "purple_turtle.png",
    # "orange": "orange_turtle.png"
}

# ユーザーに色を入力させる
user_bet = st.text_input("どの亀が勝つか予想して色を入力してください (red, green, blue, yellow, purple, orange):")

# 亀の進行状況を保存するリスト（初期位置は0）
turtle_progress = {color: 0 for color in colors}

# レースが始まるボタン
if st.button("レース開始！"):
    if user_bet not in colors:
        st.error("無効な色が選ばれました。正しい色を選んでください。")
    else:
        st.write(f"あなたの選んだ亀の色: {user_bet}")

        # レイアウト設定
        turtle_cols = st.columns(6)  # 6列で亀を表示する

        # 各亀の初期画像を表示
        turtle_elements = {}
        for idx, color in enumerate(colors):
            with turtle_cols[idx]:
                turtle_elements[color] = st.image(turtle_images[color], width=100)

        # レースが終了するまで進行
        race_ongoing = True
        while race_ongoing:
            for turtle in colors:
                # 各亀がランダムな距離を進む
                turtle_progress[turtle] += random.randint(1, 10)
                if turtle_progress[turtle] >= 100:  # 100がゴール
                    turtle_progress[turtle] = 100
                    race_ongoing = False
                    winning_color = turtle
                    break

                # 亀の位置を動的に更新
                position_percentage = turtle_progress[turtle] / 100
                turtle_cols[colors.index(turtle)].empty()  # 古い画像を消す
                turtle_cols[colors.index(turtle)].image(turtle_images[turtle], width=100)

            # 少し遅延を入れて動きをシミュレーション
            time.sleep(0.3)

        # 勝者の発表
        if winning_color == user_bet:
            st.success(f"おめでとうございます！{winning_color}の亀が勝ちました！")
        else:
            st.warning(f"残念！{winning_color}の亀が勝ちました！")
