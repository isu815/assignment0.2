import numpy as np
Names of patients and wards
names = [f"Patient_{i+1}" for i in range(50)]
ages = np.random.randint(18, 80, size=50)
wards = np.random.choice(['ICU', 'General', 'Pediatric', 'Emergency'], size=50)

Generate medical data
temperatures = np.random.uniform(36.0, 40.5, size=50).round(2)
heart_rates = np.random.randint(60, 120, size=50)
infection_status = np.random.choice([True, False], size=50, p=[0.3, 0.7])

print("Patient Data Generated Successfully!")
print(f"Total Patients: 50")
print(f"Infected Patients: {np.sum(infection_status)}")
print(f"Temperatures: {temperatures[:5]} ...")
print(f"Heart Rates: {heart_rates[:5]} ...")