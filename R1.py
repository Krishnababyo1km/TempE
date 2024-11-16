import turtle as t

# 定義一個曲線繪制函數
def DegreeCurve(n, r, d=1):
    for i in range(n):
        t.left(d)
        t.circle(r, abs(d))

# 初始位置設定
s = 0.2  # size
t.setup(450 * 5 * s, 750 * 5 * s)
t.pencolor('black')
t.fillcolor('red')
t.speed(100)
t.penup()
t.goto(0, 900 * s)
t.pendown()

# 繪制花朵形狀
t.begin_fill()
t.circle(200 * s, 30)
DegreeCurve(60, 50 * s)
t.circle(200 * s, 30)
DegreeCurve(4, 100 * s)
t.circle(200 * s, 50)
DegreeCurve(50, 50 * s)
t.circle(350 * s, 65)
DegreeCurve(40, 70 * s)
t.circle(150 * s, 50)
DegreeCurve(20, 50 * s, -1)
t.circle(400 * s, 60)
DegreeCurve(18, 50 * s)
t.fd(250 * s)
t.right(150)
t.circle(-500 * s, 12)
t.left(140)
t.circle(550 * s, 110)
t.left(27)
t.circle(650 * s, 100)
t.left(130)
t.circle(-300 * s, 20)
t.right(123)
t.circle(220 * s, 57)
t.end_fill()

# 繪制花枝形狀
t.left(120)
t.fd(280 * s)
t.left(115)
t.circle(300 * s, 33)
t.left(180)
t.circle(-300 * s, 33)
DegreeCurve(70, 225 * s, -1)
t.circle(350 * s, 104)
t.left(90)
t.circle(200 * s, 105)
t.circle(-500 * s, 63)

# 繪制一個綠色葉子
t.penup()
t.goto(670 * s, -180 * s)
t.pendown()
t.right(140)
t.fillcolor('green')
t.begin_fill()
t.circle(300 * s, 120)
t.left(60)
t.circle(300 * s, 120)
t.end_fill()

# 第二片葉子
t.penup()
t.goto(180 * s, -550 * s)
t.pendown()
t.right(85)
t.circle(600 * s, 40)

# 繪制另一個綠色葉子
t.penup()
t.goto(-150 * s, -1000 * s)
t.pendown()
t.begin_fill()
t.right(120)  # 正確的葉子角度
t.circle(300 * s, 115)
t.left(75)
t.circle(300 * s, 115)  # 繪制另一半葉子
t.end_fill()

# 結束
t.hideturtle()
t.done()