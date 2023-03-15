height = input ("enter your height in m: ")
weight = input ("enter your weight in kg: ")

h = float(height)
w = int(weight)

bmi = w/(h*h)
bmi_int = int (bmi)

print ("My BMI is =" + str(bmi_int))
print (f"My BMI is = {bmi_int}")
