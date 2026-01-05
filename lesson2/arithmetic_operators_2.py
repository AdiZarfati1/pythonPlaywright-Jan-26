# abs
print(abs(-25)) # 25
print(abs(25)) # 25

# min
print(min(2, -25, 1000, 0)) # -25
print(min(2, abs(-25), 1000, -1)) # -1

# max
print(max(2, -25, 1000, 0)) # 1000

# pow
print(pow(5, 3)) # 125
print(5 ** 3) # 125
print(pow(25, 0.5)) # 5

# round
print(round(2.49)) # 2 # מעגל כלפי מטה
print(round(2.50)) # 2 # לא מעגל אלא כאילו מעגל למטה
print(round(2.51)) # 3 # מעגל כלפי מעלה
print(round(2.56789, 2)) # 2.57 #מעגל כלפי מעלה
print(round(2.56189, 2)) # 2.56 # מעגל כלפי מטה
