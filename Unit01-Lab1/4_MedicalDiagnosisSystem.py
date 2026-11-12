def medical_diagnosis(symptoms):
    """Production Rule-Based System for Medical Diagnosis."""
    symptoms = {s.lower().strip() for s in symptoms}
    rules = [
        ({"fever", "cough", "fatigue"}, "Possible Viral Infection / Flu"),
        ({"fever", "headache", "body ache"}, "Possible Seasonal Fever"),
        ({"sneezing", "runny nose", "itchy eyes"}, "Possible Allergic Rhinitis"),
        ({"headache", "nausea"}, "Possible Migraine"),
        ({"stomach pain", "acidity"}, "Possible Gastritis")
    ]
    for condition_set, diagnosis in rules:
        if condition_set.issubset(symptoms):
            return diagnosis
    return "Symptoms inconclusive. Please consult a doctor."

if __name__ == "__main__":
    patient_symptoms = ["fever", "headache", "body ache"]
    print("Patient Symptoms:", patient_symptoms)
    print("Diagnosis:", medical_diagnosis(patient_symptoms))
