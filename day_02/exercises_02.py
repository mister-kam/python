patient = {"id": 1042, "age": 67, "status": "active", "unit": "ICU"}


patient = {"id": 1042, "age": 67, "status": "active",
           "diagnoses": {"I10", "E11.9"}}
print(patient["diagnoses"])
print(type(patient["diagnoses"]))

patients = {
    "MRN001": {
        "name": "Alice Johnson",
        "diagnoses": ["E11.9", "I10", "E11.9"]
    },
    "MRN002": {
        "name": "Bob Smith",
        "diagnoses": ["J45.909", "I10"]
    },
    "MRN003": {
        "name": "Carol Davis",
        "diagnoses": ["E78.5", "M54.5"]
    }
}

# Add a new diagnosis to MRN001
patients["MRN001"]["diagnoses"].append("E78.5")

# Print the distinct diagnosis count
print(len(set(patients["MRN001"]["diagnoses"])))

# Look up a patient's name directly by MRN
print(patients["MRN002"]["name"])
