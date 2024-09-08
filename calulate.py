import streamlit as st

# ヘッダー
st.title("SHOOの計算機")

# 数値の入力
num1 = st.number_input("最初の数値を入力してください", value=0)
num2 = st.number_input("次の数値を入力してください", value=0)

# 演算の選択
operation = st.selectbox("演算を選んでください", ("加算", "減算", "乗算", "除算"))

# 計算と結果の表示
if operation == "加算":
    result = num1 + num2
    st.write(f"結果: {num1} + {num2} = {result}")
elif operation == "減算":
    result = num1 - num2
    st.write(f"結果: {num1} - {num2} = {result}")
elif operation == "乗算":
    result = num1 * num2
    st.write(f"結果: {num1} * {num2} = {result}")
elif operation == "除算":
    if num2 != 0:
        result = num1 / num2
        st.write(f"結果: {num1} / {num2} = {result}")
    else:
        st.write("エラー: 0で割ることはできません。")
