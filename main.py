# 4
rang = input("Chiroq rangini kiriting: ")

if rang == "qizil":
    print("Toxtang")
elif rang == "sariq":
    print("Tayorlaning")
elif rang == "yashil":
    print("Yuring")
else:
    print("Bunday rang yoq")

# 5
tezlik = float(input("Internet tezligini: "))

if tezlik > 100:
    print("Sizda ajoyib tezlik")
elif 50 <= tezlik <= 100:
    print("Tezlik yaxshi lekin yaxshilash mumkin")
elif 10 <= tezlik < 50:
    print("Tezlik past provayder bilan boglaning")
else:
    print("Bu tezlik bilan internet ishlatib bolmaydi")

# 6
ball = int(input("Imtihon ballini kiriting : "))

if ball > 90:
    print("Alo")
elif 75 <= ball <= 89:
    print("Yaxshi")
elif 50 <= ball <= 74:
    print("Qoniqarli")
else:
    print("Yiqildingiz")
