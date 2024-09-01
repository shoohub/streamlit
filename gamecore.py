import streamlit as st
import pandas as pd
import numpy as np

# ステップ1: ユーザー人数と名前の入力
if 'step' not in st.session_state:
    st.session_state.step = 1
    st.session_state.players = []
    st.session_state.scores = None

if st.session_state.step == 1:
    st.title("ステップ1: ユーザー人数と名前の入力")
    
    num_players = st.number_input("プレイヤーの人数を入力してください", min_value=1, value=1, step=1)
    
    st.session_state.players = []
    for i in range(num_players):
        player_name = st.text_input(f"プレイヤー{i+1}の名前を入力してください", key=f"player_name_{i}")
        st.session_state.players.append(player_name)
    
    if all(st.session_state.players):  # すべての名前が入力されたか確認
        if st.button("次へ"):
            st.session_state.step = 2

# ステップ2: ゲーム回数の入力
if st.session_state.step == 2:
    st.title("ステップ2: ゲーム回数の入力")
    
    num_rounds = st.number_input("ゲームの回数を入力してください", min_value=1, value=1, step=1)
    st.session_state.num_rounds = num_rounds
    
    if num_rounds > 0:
        if st.button("マトリックスを生成"):
            st.session_state.step = 3

# ステップ3: スコアの入力
if st.session_state.step == 3:
    st.title("ステップ3: スコアの入力")
    
    players = st.session_state.players
    num_rounds = st.session_state.num_rounds
    
    scores = np.zeros((len(players), num_rounds), dtype=int)
    st.session_state.scores = scores
    
    for i, player in enumerate(players):
        for j in range(num_rounds):
            scores[i, j] = st.number_input(f"{player}のラウンド{j+1}のスコア:", min_value=0, value=0, step=1, key=f"score_{i}_{j}")
    
    # スコアをDataFrameに変換して表示
    df_scores = pd.DataFrame(st.session_state.scores, index=players, columns=[f"ラウンド{j+1}" for j in range(num_rounds)])
    st.write("スコアマトリックス:")
    st.dataframe(df_scores)
    
    if st.button("採点"):
        st.session_state.step = 4

# ステップ4: 採点結果の表示
if st.session_state.step == 4:
    st.title("ステップ4: 採点結果")
    
    players = st.session_state.players
    df_scores = pd.DataFrame(st.session_state.scores, index=players, columns=[f"ラウンド{j+1}" for j in range(st.session_state.num_rounds)])
    
    # 合計点を計算して表示
    total_scores = df_scores.sum(axis=1)
    st.write("各プレイヤーの合計得点:")
    for player, total in total_scores.items():
        st.write(f"{player}: {total} 点")
    
    if st.button("再スタート"):
        st.session_state.step = 1
