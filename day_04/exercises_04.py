# name = "Jordan"
# print(name)

# names = ["Jordan", "Casey"]
# print(names)


def calculate_bmi(height_cm, weight_kg):
    bmi = weight_kg / (height_cm / 100) ** 2
    return bmi


patient1_bmi = calculate_bmi(200, 75)
print(patient1_bmi)

patient2_bmi = calculate_bmi(150, 80)
print(patient2_bmi)


def categorize_bmi(bmi_value):
    if bmi_value < 18.5:
        return "underweight"
    elif bmi_value >= 18.5 and bmi_value <= 24.9:
        return "normal"
    elif bmi_value >= 25 and bmi_value <= 29.9:
        return "overweight"
    else:
        return "obese"


test1 = categorize_bmi(patient1_bmi)
print(test1)
test2 = categorize_bmi(patient2_bmi)
print(test2)


def categorize_bmi(bmi_value, threshold_obese=30):
    if bmi_value > threshold_obese:
        return "obese"
    elif bmi_value < 18.5:
        return "underweight"
    elif bmi_value >= 18.5 and bmi_value <= 24.9:
        return "normal"
    elif bmi_value >= 25 and bmi_value <= 29.9:
        return "overweight"


test3 = categorize_bmi(31)
print(test3)
test4 = categorize_bmi(28, 27)
print(test4)

count = 0


def increment():
    global count
    count = count + 1
    return count


result = increment()
print(result)
print(count)  # Now this works and prints 1


def summarize_vitals(pt_name, **kwargs):
    pieces = []
    for key, value in kwargs.items():
        pieces.append(f"{key}={value}")
    return f"{pt_name}: {', '.join(pieces)}"


patient4 = summarize_vitals(pt_name="Alice", temp=98.6, hr=72, bp_systolic=120)
print(patient4)
patient5 = summarize_vitals("bill", temp=100, bp=90)
print(patient5)

square = lambda x: x**2
print(square(5))  # 25

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

bmi_values = [18.5, 25, 30, 22]
result = list(filter(lambda bmi: bmi >= 25, bmi_values))
print(result)

patients = [("Alice", 18.5), ("Bob", 31), ("Casey", 24)]
# Sort by BMI (second element), and print the result
pt_sorted = sorted(patients, key=lambda p: p[1])
print(pt_sorted)


def calculate_bmi(height_cm, weight_kg):
    bmi = weight_kg / (height_cm / 100) ** 2
    return bmi


def categorize_bmi(bmi_value, threshold_obese=30):
    if bmi_value < 18.5:
        return "underweight"
    elif bmi_value >= 18.5 and bmi_value <= 24.9:
        return "normal"
    elif bmi_value >= 25 and bmi_value <= 29.9:
        return "overweight"
    elif bmi_value > threshold_obese:
        return "obese"
    else:
        return "unknown"


def analyze_patient(name, height_cm, weight_kg, threshold_obese=30):
    bmi_value = calculate_bmi(height_cm, weight_kg)  # Call the other function
    cat = categorize_bmi(bmi_value, threshold_obese)
    return f"{name}: BMI={bmi_value}({cat})"


print(analyze_patient("Alice", 175, 70))

print(analyze_patient("Bill", 170, 80, 28))


numbers = [1, 2, 3, 4, 5]
result = list(filter(lambda x: x % 2 == 0, numbers))
print(result)


def collect(*args):
    return len(args)


print(collect(1, 2, 3, 4))

patients = [("Alice", 22.8), ("Bob", 31.2), ("Casey", 18.5)]
result = sorted(patients, key=lambda p: p[1])
print(result[0][0])
