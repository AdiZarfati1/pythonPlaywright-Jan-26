# name = input("Enter your name: ") #קלט
# print(name) # פלט
# age = input("Enter your age: ")
# print(age)
# n1 = input("Enter number 1: ") # 3
# n2 = input("Enter number 2: ") # 5
# print(n1 + n2) # 35 יצר שרשור ולא חיבור
# # אינפוט מחזיר אך ורק סטרינג.
# # פשוט הדבקה של טקסטים. לכן צריך לעשות המרה כדי לקבל מספרים שלמים

# n1 = int(input("Enter number 1: ")) # 3
# n2 = int(input("Enter number 2: ")) # 5
# print(n1 + n2) # 8

# n1 = float(input("Enter number 1: ")) # 3
# n2 = float(input("Enter number 2: ")) # 5
# print(n1 + n2) # 8.0

# n1 = input("Enter number 1: ") # 3
# n2 = input("Enter number 2: ") # 5
# print(type(n1)) # str שוב מהסיבה שאינפוט מחזיר רק סטרינג כל עוד לא בוצע המרה
# print(type(n2))# str
# print(n1 + n2) # 35

# n1 = int(input("Enter number 1: ")) # 3
# n2 = int(input("Enter number 2: ")) # 5
# print(type(n1)) # int
# print(type(n2)) # int
# print(n1 + n2) # 8

# n1 = int(input("Enter number 1: "))
# print(n1) # int
# # אם נקלוט מספר כך: 12 34
# # יעשה שגיאה כיוון שרווח זה לא מספר
# n2 = input("Enter number 2: ")
# # אבל אם כאן נקלוט מספר כך: 12 34
# # לא יעשה שגיאה כי רווח הוא חלק מסטרינג-טקסט
# print(n2)

numbers = (input("Enter 2 numbers separated by space: "))
numbers_with_split = numbers.split()
# print(numbers) # 12 34 # המספרים אינם נפרדים
# print(numbers_with_split) # ['12', '34'] # כל מספר הוא אלמנט נפרד
# print(type(numbers_with_split[0])) # str
# print(type(numbers_with_split[1])) # str
n1 = int(numbers_with_split[0])
n2 = int(numbers_with_split[1])
print(type(n1)) # int
print(type(n2)) # int



