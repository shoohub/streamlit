import streamlit as st
import pandas as pd
import numpy as np

# ヘッダー
st.title("ゲームスコア管理システム")

# ユーザー人数、名前、ゲーム回数の入力
num_players = st.number_input("プレイヤーの人数を入力してください", min_value=1, value=1, step=1)
num_rounds = st.number_input("ゲームの回数を入力してください", min_value=1, value=1, step=1)

# プレイヤー名の入力
player_names = []
for i in range(num_players):
    player_name = st.text_input(f"プレイヤー{i+1}の名前を入力してください", key=f"player_{i}_name")
    player_names.append(player_name)

# プレイヤー名がすべて入力されたか確認
if all(player_names) and num_rounds > 0:
    # スコア用のマトリックスを作成
    scores = np.zeros((num_players, num_rounds), dtype=int)

    st.write("各ラウンドのスコアを入力してください:")

    # スコア入力
    for i in range(num_players):
        for j in range(num_rounds):
            scores[i, j] = st.number_input(f"{player_names[i]}さんのラウンド{j+1}のスコア:", min_value=0, value=0, step=1, key=f"score_{i}_{j}")

    # スコアをDataFrameに変換して表示
    df_scores = pd.DataFrame(scores, index=player_names, columns=[f"ラウンド{j+1}" for j in range(num_rounds)])
    st.write("スコアマトリックス:")
    st.dataframe(df_scores)

    # 合計点を計算
    total_scores = df_scores.sum(axis=1)
    st.write("各プレイヤーの合計得点:")
    for player, total in total_scores.items():
        st.write(f"{player}: {total} 点")
else:
    st.write("すべてのプレイヤー名とゲーム回数を入力してください。")
