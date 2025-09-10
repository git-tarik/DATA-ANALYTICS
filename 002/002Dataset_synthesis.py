'''Q2. Generate a synthetic dataset for Employee attendance
   where attributes include EmployeeID, Name, Department,
   Date, Status (Present/Absent)'''

import numpy as np 
import pandas as pd
from faker import Faker
n=250
fake=Faker()    
data = {
    "EmployeeID":np.arange(1,n+1),
    "Name":[fake.name() for _ in range(n)],
    "Department":np.random.choice(["HR","Finance","IT","Sales"],n),
    "Date":[fake.date_this_year() for _ in range(n)],
    "Status":np.random.choice(["Present","Absent"],n)

}
df=pd.DataFrame(data)
print(df.head())
print(df.describe())
df.to_csv('Employee_attendance.csv',index=False)

