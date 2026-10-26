
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# 1. Load the CSV file
df = pd.read_csv("startup.csv")

# 2. Select input and target columns
X = df[['RD_Spend', 'Administration', 'Marketing_Spend']]
y = df['Profit']

# 3. Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Create and train the regression model
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Predict profit
y_pred = model.predict(X_test)

# 6. Evaluate the model
print("Regression Analysis Results")
print("---------------------------")
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# 7. Display regression coefficients
print("\nRegression Coefficients")
for feature, coefficient in zip(X.columns, model.coef_):
    print(feature, ":", round(coefficient, 4))

print("Intercept:", round(model.intercept_, 4))

# 8. Predict profit for new spending values
new_data = pd.DataFrame({
    'RD_Spend': [21892.92],
    'Administration': [81910.77],
    'Marketing_Spend': [164270.7]
})

predicted_profit = model.predict(new_data)

print("\nPredicted Profit:", round(predicted_profit[0], 2))
