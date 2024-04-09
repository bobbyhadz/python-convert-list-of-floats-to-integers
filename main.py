# Convert a List of Floats to a List of Integers in Python

list_of_floats = [1.23, 3.45, 5.67]

result = [int(item) for item in list_of_floats]
print(result)  # 👉️ [1, 3, 5]