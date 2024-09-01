import streamlit as st

# ヘッダー
st.title("ゲームスコア管理")

# ユーザー人数の入力
num_players = st.number_input("プレイヤーの人数を入力してください", min_value=1, value=1, step=1)

# プレイヤー名の入力を一括で行う
if 'players' not in st.session_state:
    st.session_state.players = []

if len(st.session_state.players) != num_players:
    st.session_state.players = [''] * num_players

if st.button("プレイヤー名を登録"):
    for i in range(num_players):
        player_name = st.text_input(f"プレイヤー{i+1}の名前を入力してください", key=f"player_{i}_name")
        st.session_state.players[i] = player_name

# スコア管理用のセッションステートの初期化
if 'scores' not in st.session_state:
    st.session_state.scores = {player: 0 for player in st.session_state.players}

# プレイヤー名が入力されている場合、得点を入力
if all(st.session_state.players):  # すべてのプレイヤー名が入力されているかを確認
    for player in st.session_state.players:
        score = st.number_input(f"{player}さんの今回の得点を入力してください", min_value=0, value=0, step=1, key=f"{player}_score")
        if st.button(f"{player}さんの得点を追加", key=f"{player}_button"):
            st.session_state.scores[player] += score

    # 合計得点の表示
    st.write("各プレイヤーの合計得点:")
    for player, total_score in st.session_state.scores.items():
        st.write(f"{player}: {total_score} 点")

    # スコアをリセットするボタン
    if st.button("スコアをリセット"):
        st.session_state.scores = {player: 0 for player in st.session_state.players}
else:
    st.write("すべてのプレイヤー名を入力してください。")