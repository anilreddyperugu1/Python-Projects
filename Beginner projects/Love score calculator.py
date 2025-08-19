name1 = input("Enter your name: ")
name2 = input("Enter his/her name: ")
combine = name1 + name2
lower_combine = combine.lower()

t = lower_combine.count("t")
r = lower_combine.count("r")
u = lower_combine.count("u")
e = lower_combine.count("e")
true = t + r + u + e

l = lower_combine.count("l")
o = lower_combine.count("o")
v = lower_combine.count("v")
e = lower_combine.count("e")
love = l + o + v + e

true_love = int(str(true) + str(love))
if true_love < 10 or true_love > 90:
    print(f"Your love is {true_love}% and you go together like coke and mentos!")
elif true_love >= 40 and true_love <= 50:
    print(f"Your love score is {true_love}% and you people glow up together!")
else:
    print(f"Your love score is {true_love}%")