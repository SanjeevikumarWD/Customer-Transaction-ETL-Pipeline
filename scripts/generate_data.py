from faker import Faker
import pandas as pd

fake = Faker()
data = [
    {
        "transaction_id": i,
        "customer_id": fake.uuid4(),
        "amount": fake.random_int(10, 1000),
        "date": fake.date(),
        "category": fake.random_element(["Food", "Travel", "Retail"])
    }
    for i in range(1000)
]
pd.DataFrame(data).to_csv("data/transactions.csv", index=False)
print("Generated 1000 transaction records in data/transactions.csv")
