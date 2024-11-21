import joblib
import pandas as pd
import numpy as np

model = joblib.load('model.pkl')

data = pd.read_csv('employee_data.csv')

# seed the data

random_state = np.random.randint(0, 10000)
data = data.sample(frac=1, random_state=random_state).reset_index(drop=True)

test_data = data.sample(5, random_state=random_state)

if 'Attrition' in test_data.columns:
    test_data = test_data.drop(columns=['Attrition', 'EmployeeId', 'Over18', ])

test_data['BusinessTravel'] = test_data['BusinessTravel'].map({'Travel_Rarely': 1, 'Travel_Frequently': 0, 'Non-Travel': 0})
categorical_columns = ['Department', 'EducationField', 'Gender', 'JobRole', 'MaritalStatus', 'OverTime']

for column in categorical_columns:
    test_data[column] = test_data[column].astype('category').cat.codes


# test_data['Travel_Rarely'] = test_data['Travel_Rarely'].map({'Travel_Rarely': 1, 'Travel_Frequently': 0, 'Non-Travel': 0})
test_data['Predicted Attrition'] = model.predict(test_data)

print(test_data[['Predicted Attrition']])

test_data.to_csv('predicted_attrition.csv', index=False)
print("Predictions saved to predicted_attrition.csv")
