'''Q4. Generate a synthetic dataset of hospital patient records with 
   fields like PatientID, Name, Age , Gender, Diagnosis
   [Flue,diabetes,hypertension, covid, injury], AdmissionDate,
   Discharge[Yes/No].'''
import numpy as np 
import pandas as pd     
from faker import Faker
import random
n=250
fake=Faker()
diagnoses = ["Flue","Diabetes","Hypertension","Covid","Injury"]
data = {
    "PatientID":np.arange(1,n+1), 
    "Name":[fake.name() for _ in range(n)],
    "Age":np.random.randint(0,100,n),
    "Gender":np.random.choice(["Male","Female","Other"],n),
    "Diagnosis":[random.choice(diagnoses) for _ in range(n)],
    "AdmissionDate":[fake.date_this_year() for _ in range(n)],  
    "Discharge":np.random.choice(["Yes","No"],n)
}
df=pd.DataFrame(data)
print(df.head())
print(df.describe())
df.to_csv('Hospital_patient_records.csv',index=False)