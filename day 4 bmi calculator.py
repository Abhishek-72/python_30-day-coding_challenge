height = input("enter the height in m: ")
weight = input("enter the weight in kg: ")

bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)