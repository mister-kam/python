import numpy as np

systolic = np.array([120, 145, 130, 110, 155, 125])
diastolic = np.array([80, 95, 85, 70, 100, 80])

sys_mean = np.mean(systolic)
print(sys_mean)
dia_mean = np.mean(diastolic)
print(dia_mean)

high_bp = systolic > 140
print(high_bp)
filtered = diastolic[high_bp]
print(filtered)

#######################################################

vitals = np.array([
    [98.6, 145, 80, 95.0],
    [98.9, 130, 75, 105.0],
    [99.1, 155, 90, 110.0],
    [98.2, 120, 78, 100.0]
])

normal = np.array([98.0, 120, 70, 100.0])

difference = vitals - normal
print(difference)

######################################################
# 5 patients' glucose readings (some missing)
glucose = np.array([95.0, np.nan, 105.0, 100.0, np.nan])

print("Raw data:", glucose)
print("Mean (with NaN):", np.mean(glucose))
print("Mean (ignoring NaN):", np.nanmean(glucose))

# Filter: which patients have glucose >= 100?
high_glucose = glucose >= 100
print("High glucose mask:", high_glucose)

filtered = glucose[high_glucose]
print("Filtered (high glucose only):", filtered)

######################################################
# 6 patients: [temp, systolic, glucose]
vitals = np.array([
    [98.6, 145, 95.0],
    [98.9, 130, np.nan],
    [99.1, 155, 105.0],
    [98.2, 120, 100.0],
    [97.9, np.nan, 110.0],
    [99.5, 140, 98.0]
])

mean_systolic = np.nanmean(vitals[:,1])
print(mean_systolic)

high_sys = vitals[:,1] > 140
print(high_sys)
filtered_high_sys = vitals[high_sys]
print(filtered_high_sys)

filtered_mean_glu = np.mean(filtered_high_sys[:,2])
print(filtered_mean_glu)

######################################################
arr = np.array([10, 20, 30, 40, 50])
mask = (arr > 15) & (arr < 45)
result = arr[mask]
print(result)

print(np.arange(5, 15, 3))

temps = np.array([98.6, 99.1, 98.9, 99.5])
temps_f_to_c = (temps - 32) * 5/9
print(temps_f_to_c)


data = np.array([[1, 2], [3, 4], [5, 6]])
result = data[1, :]
print(result)

arr = np.array([10, np.nan, 30, 40, 50])
print(arr > 25)