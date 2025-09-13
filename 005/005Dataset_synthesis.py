'''Q5. Generate a synthetic dataset for the university course 
enrollments with fields like EnrollmentID, StudentName,
coursecode, enrollmentdate,Grade[A-F].'''
import numpy as np
import pandas as pd
from faker import Faker
import random
n=250
fake=Faker()
course_codes = ["CS101", "MATH202", "ENG303", "BIO404", "HIST505"]
grades = ["A", "B", "C", "D", "E", "F"]
data = {
    "EnrollmentID":np.arange(1,n+1),
    "StudentName":[fake.name() for _ in range(n)],
    "CourseCode":[random.choice(course_codes) for _ in range(n)],
    "EnrollmentDate":[fake.date_this_year() for _ in range(n)],
    "Grade":[random.choice(grades) for _ in range(n)]
}
df=pd.DataFrame(data)
print(df.head())
print(df.describe())
df.to_csv('University_course_enrollments.csv',index=False)