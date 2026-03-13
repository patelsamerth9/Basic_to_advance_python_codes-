import pandas as pd
from sklearn.linear_model import LogisticRegression

data = {
    "income": [20000, 50000, 30000, 80000, 25000],
    "loan_amount": [15000, 20000, 10000, 40000, 12000],
    "credit_score": [500, 750, 650, 800, 550],
    "risk": [1, 0, 0, 0, 1]
}

df = pd.DataFrame(data)

X = df[["income", "loan_amount", "credit_score"]]
y = df["risk"]

model = LogisticRegression()
model.fit(X, y)

new_customer = [[30000, 20000, 600]]
# The new customer's income is $30,000, loan amount is $20,000, and credit score is 600.
prediction = model.predict(new_customer)

print("Risk Prediction:", prediction)
# The output will be either 0 (low risk) or 1 (high risk) based on the model's prediction for the new customer.