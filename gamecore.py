import streamlit as st
import pandas as pd
import numpy as np

# ヘッダー
st.title("ゲームスコア管理システム")

# ユーザー人数、ゲーム回数の入力
num_players = st.number_input("プレイヤーの人数を入力してください", min_value=1, value=1, step=1)
num_rounds = st.number_input("ゲームの回数を入力してください", min_value=1, value=1, step=1)

# マトリックスの入力フィールドを生成
if st.button("マトリックスを生成"):
    st.write("プレイヤー名を入力し、スコアを記録してください。")

    player_names = []
    scores = []

    # プレイヤー名とスコアの入力
    for i in range(num_players):
        row = []
        player_name = st.text_input(f"プレイヤー{i+1}の名前を入力してください", key=f"player_name_{i}")
        player_names.append(player_name)
        
        for j in range(num_rounds):
            score = st.number_input(f"{player_name}のラウンド{j+1}のスコア:", min_value=0, value=0, step=1, key=f"score_{i}_{j}")
            row.append(score)
        scores.append(row)

    # スコアをDataFrameに変換して表示
    if all(player_names):  # すべての名前が入力されているかを確認
        df_scores = pd.DataFrame(scores, index=player_names, columns=[f"ラウンド{j+1}" for j in range(num_rounds)])
        st.write("スコアマトリックス:")
        st.dataframe(df_scores)

        # 合計点を計算
        total_scores = df_scores.sum(axis=1)
        st.write("各プレイヤーの合計得点:")
        for player, total in total_scores.items():
            st.write(f"{player}: {total} 点")
    else:
        st.write("すべてのプレイヤー名を入力してください。")
