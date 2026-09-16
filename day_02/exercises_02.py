patient = {"id": 1042, "age": 67, "status": "active", "unit": "ICU"}


patient = {"id": 1042, "age": 67, "status": "active", "diagnoses": {"I10", "E11.9"}}
print(patient["diagnoses"])
print(type(patient["diagnoses"]))
