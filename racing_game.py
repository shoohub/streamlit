import random
import time

import streamlit as st

# タイトルと説明
st.title('海亀レース！')
st.write('どの色の海亀が勝つか予想して、レースの結果を見てみましょう！')

# ユーザーに色を入力させる
user_bet = st.text_input("どの海亀が勝つか予想して色を入力してください (red, green, blue, yellow, purple, orange):")

# 海亀の色を定義する
colors = ["red", "green", "blue", "yellow", "purple", "orange"]
# 海亀の進行状況を保存するリスト
turtle_progress = {color: 0 for color in colors}

# レースが始まるボタン
if st.button("レース開始！"):
    if user_bet not in colors:
        st.error("無効な色が選ばれました。正しい色を選んでください。")
    else:
        st.write(f"あなたの選んだ海亀の色: {user_bet}")

        # 各海亀のプログレスバーを作成
        progress_bars = {color: st.progress(0) for color in colors}

        # レースが終了するまで進行
        race_ongoing = True
        while race_ongoing:
            for turtle in colors:
                # 各海亀がランダムな距離を進む
                turtle_progress[turtle] += random.randint(1, 10)
                if turtle_progress[turtle] >= 100:
                    turtle_progress[turtle] = 100  # 最大100に制限
                    race_ongoing = False
                    winning_color = turtle
                    break

                # プログレスバーを更新
                progress_bars[turtle].progress(turtle_progress[turtle])

            # レースの進行を見やすくするためのスリープ
            time.sleep(0.1)

        # 勝者の発表
        if winning_color == user_bet:
            st.success(f"おめでとうございます！{winning_color}の海亀が勝ちました！")
        else:
            st.warning(f"残念！{winning_color}の海亀が勝ちました！")
