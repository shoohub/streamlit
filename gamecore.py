import streamlit as st

# ヘッダー
st.title("ゲームスコア管理")

# ユーザー人数の入力
num_players = st.number_input("プレイヤーの人数を入力してください", min_value=1, value=1, step=1)

# ユーザー名の入力
if 'players' not in st.session_state:
    st.session_state.players = []

if len(st.session_state.players) != num_players:
    st.session_state.players = [st.text_input(f"プレイヤー{i+1}の名前を入力してください") for i in range(num_players)]

# スコア管理用のセッションステートの初期化
if 'scores' not in st.session_state:
    st.session_state.scores = {player: 0 for player in st.session_state.players}

# 各プレイヤーの得点を入力
for player in st.session_state.players:
    if player:  # プレイヤー名が入力されている場合のみ表示
        score = st.number_input(f"{player}さんの今回の得点を入力してください", min_value=0, value=0, step=1, key=player)
        if st.button(f"{player}さんの得点を追加", key=f"{player}_button"):
            st.session_state.scores[player] += score

# 合計得点の表示
st.write("各プレイヤーの合計得点:")
for player, total_score in st.session_state.scores.items():
    if player:  # プレイヤー名が入力されている場合のみ表示
        st.write(f"{player}: {total_score} 点")

# もう一度プレイするためにリセットするボタン
if st.button("スコアをリセット"):
    st.session_state.scores = {player: 0 for player in st.session_state.players}
