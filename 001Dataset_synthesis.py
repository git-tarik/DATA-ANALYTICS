import numpy as np 
import pandas as pd
from faker import Faker

n=1000
fake=Faker()
data = {
    
    "CustomerId":np.arange(1,n+1),
    "Name":[fake.name() for _ in range(n)],
    "Age":np.random.randint(18,76,n),
    "Gender":np.random.choice(["Male","Female","Other"],n),
    "PurchaseDate":[fake.date_this_year() for _ in range(n)],
    "ProductCategory":np.random.choice(["Electronics","Fashion","Grocery"],n),
    "AmountSpent":np.round(np.random.uniform(1,500,n),2)
}


df=pd.DataFrame(data)
print(df.head())