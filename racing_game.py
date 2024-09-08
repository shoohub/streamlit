"""６匹の海亀がレースをする！色を入力して遊びましょう！"""
import random
from turtle import Screen, Turtle

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(
    title="Make your bet", prompt="Witch turtle will win the race?Enter a color(enter red,green,light pink,green yellow,medium purple,light sky blue): ")

# 海亀の色を定義する
colors = ["red", "green", "light pink",
          "green yellow", "medium purple", "light sky blue"]
# 海亀のスタートラインを定義する
y_positions = [-70, -40, -10, 20, 50, 80]
# 6匹の海亀を生成する
all_turtles = []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    new_turtle.pendown()
    all_turtles.append(new_turtle)

# ユーザー入力させてからレースをONにする
if user_bet:
    is_race_on = True


while is_race_on:  # 全体のループ処理
    for turtle in all_turtles:  # 海亀リストの順番にサークルを回していく
        if turtle.xcor() > 230:  # ゴールに到着（画面に一番右側まで）したら、結果を出力し終了する
            winning_color = turtle.pencolor()
            if winning_color == user_bet:

                print(f"you have won!The {
                      winning_color} turtle is the winner!")
            else:
                print(f"you have lost!The {
                      winning_color} turtle is the winner!")
            is_race_on = False
        else:
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)


# 画面をクリックするまで閉じない
screen.exitonclick()
