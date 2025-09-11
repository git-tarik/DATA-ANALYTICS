

'''Q3. Generate a dataset for ecommerce product reviews
   with fields like ReviewID, ProductID , Receivers Name,
   ReviewText, Rating (1-5), ReviewDate.'''

import numpy as np 
import pandas as pd  
from faker import Faker
import random
n=250
fake=Faker()
review_texts = [
    "Great product, highly recommend!",
    "Not worth the price.",
    "Average quality, could be better.",
    "Exceeded my expectations!",
    "Would not buy again.",
    "Fantastic value for money.",
    "Poor customer service experience.",
    "Loved the design and functionality.",
    "Disappointed with the durability.",
    "Five stars, will purchase again!"
]
data = {
    "ReviewID":np.arange(1,n+1), 
    "ProductID":np.random.randint(1000,2000,n),
    "ReceiversName":[fake.name() for _ in range(n)],
    "ReviewText":[random.choice(review_texts) for _ in range(n)],
    "Rating":np.random.randint(1,6,n),
    "ReviewDate":[fake.date_this_year() for _ in range(n)]
}
df=pd.DataFrame(data)
print(df.head())
print(df.describe())
df.to_csv('Ecommerce_product_reviews.csv',index=False)
print(df['Rating'].value_counts()) 


