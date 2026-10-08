import pandas as pd

# df = pd.DataFrame(
#     {
#         "patient": ["Ana", "Ben", "Cy"],
#         "age": [54, 61, 47],
#     }
# )

# print(df)
# print(df[df["age"] < 55])


#   patient  age
# 0     Ana   54
# 2      Cy   47

# filtered.loc[2, "patient"]   # Cy      (the row labeled 2, column "patient")
# filtered.iloc[1, 0]          # Cy      (second row by position, first column)
# filtered.loc[1, "age"]       # error   (there is no row labeled 1)
# Q4a: print(filtered.loc[2, "age"])
# Q4b: print(filtered.iloc[0, 1])
# Q4c: print(filtered.iloc[2, 0])

#   patient  age  under_50
# 0     Ana   44     true
# 1     Ben   51     false
# 2      Cy   37     true

# import pandas as pd

# df = pd.DataFrame(
#     {"patient": ["Ana", "Ben", "Cy", "Dee"], "systolic": [128, 152, 141, 119]}
# )
# df["systolic_minus_120"] = df["systolic"] - 120

# print(df)
# print(df[df["systolic"] > 140])
# print(df.loc[3, "systolic"])

df = pd.DataFrame(
    {
        "patient": ["Ana", "Ben", "Cy", "Dee"],
        "hr": [72, 88, 95, 64],
    }
)
sub = df[df["hr"] > 80]

print(df["hr"] - 70)
print(sub)
print(sub.loc[2, "patient"])
print(sub.iloc[0, 0])

df["high"] = df["hr"] > 90
print(df["high"])
