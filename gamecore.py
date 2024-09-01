import streamlit as st
import pandas as pd
import numpy as np

# タイトルの設定
st.title("SHOOのゲーム部屋へようこそ")

# ステップ1: ユーザー人数と名前の入力
if 'step' not in st.session_state:
    st.session_state.step = 1
    st.session_state.players = []
    st.session_state.num_rounds = 0
    st.session_state.scores = None

if st.session_state.step == 1:
    st.header("ステップ1: ユーザー人数と名前の入力")
    
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
    st.header("ステップ2: ゲーム回数の入力")
    
    num_rounds = st.number_input("ゲームの回数を入力してください", min_value=1, value=1, step=1)
    st.session_state.num_rounds = num_rounds
    
    if num_rounds > 0:
        if st.button("マトリックスを生成"):
            st.session_state.step = 3

# ステップ3: スコアの簡易入力
if st.session_state.step == 3:
    st.header("ステップ3: スコアの入力")

    players = st.session_state.players
    num_rounds = st.session_state.num_rounds
    
    if st.session_state.scores is None:
        st.session_state.scores = pd.DataFrame(np.zeros((len(players), num_rounds), dtype=int), 
                                               index=players, 
                                               columns=[f"ラウンド{j+1}" for j in range(num_rounds)])
    
    # スコア入力用のテーブルを表示
    edited_scores = st.data_editor(st.session_state.scores, use_container_width=True)

    if st.button("採点"):
        # スコアを更新
        st.session_state.scores = edited_scores
        st.session_state.step = 4

# ステップ4: 採点結果の表示
if st.session_state.step == 4:
    st.header("ステップ4: 採点結果")
    
    df_scores = st.session_state.scores
    
    # 合計点を計算して表示
    total_scores = df_scores.sum(axis=1)
    st.write("各プレイヤーの合計得点:")
    for player, total in total_scores.items():
        st.write(f"{player}: {total} 点")
    
    if st.button("再スタート"):
        # セッションステートをリセット
        st.session_state.step = 1
        st.session_state.players = []
        st.session_state.num_rounds = 0
        st.session_state.scores = None
