## Insurance Claims Fraud Detection

This project aims to predict insurance claims fraud using machine learning algorithms. The dataset used in this project is obtained from Kaggle and contains information about insurance claims, including policy details, incident details, and whether the claim was fraudulent or not.

### Dataset Overview

The dataset consists of the following columns:

- 'months_as_customer': Number of months as a customer
- 'age': Age of the customer
- 'policy_annual_premium': Annual premium of the insurance policy
- 'insured_sex': Gender of the insured (0: Female, 1: Male)
- 'insured_education_level': Education level of the insured
- 'insured_relationship': Relationship of the insured with policyholder
- 'capital-gains': Capital gains recorded
- 'capital-loss': Capital losses recorded
- 'incident_type': Type of incident
- 'collision_type': Type of collision
- 'incident_severity': Severity of the incident
- 'authorities_contacted': Authorities contacted after the incident
- 'incident_hour_of_the_day': Time of the incident (hour of the day)
- 'number_of_vehicles_involved': Number of vehicles involved in the incident
- 'property_damage': Property damage (YES/NO)
- 'bodily_injuries': Number of bodily injuries in the incident
- 'witnesses': Number of witnesses to the incident
- 'police_report_available': Availability of the police report (YES/NO)
- 'total_claim_amount': Total claim amount
- 'injury_claim': Claim amount for injuries
- 'property_claim': Claim amount for property damage
- 'vehicle_claim': Claim amount for vehicle damage
- 'fraud_reported': Whether the claim was fraudulent (YES/NO)

### Data Preprocessing

To handle missing values and "?" values in the dataset:

- Missing values in the 'authorities_contacted' column are replaced with "Other".
- "?" values in the 'collision_type' column are replaced with "Other" if incident_severity is "Trivial Damage" or "Minor Damage".
- "?" values in the 'police_report_available' column are replaced with "YES" if authorities_contacted is "Police", "Ambulance", or "Fire"; otherwise, they are replaced with "NO".
- "?" values in the 'property_damage' column are replaced with "YES" if property_claim exists; otherwise, they are replaced with "NO".

**Models and Evaluation**

Four machine learning models were trained and evaluated:

**Support Vector Classifier (SVC)**
- Test Accuracy: 0.776
- Precision (N): 0.85, Recall (N): 0.84, F1-score (N): 0.85
- Precision (Y): 0.57, Recall (Y): 0.59, F1-score (Y): 0.58

**K-Nearest Neighbors (KNN)**
- Test Accuracy: 0.692
- Precision (N): 0.77, Recall (N): 0.82, F1-score (N): 0.80
- Precision (Y): 0.40, Recall (Y): 0.33, F1-score (Y): 0.36

**Random Forest Classifier**
- Accuracy Score: 0.76
- Precision (N): 0.82, Recall (N): 0.87, F1-score (N): 0.84
- Precision (Y): 0.56, Recall (Y): 0.45, F1-score (Y): 0.50

**Decision Tree Classifier**
- Accuracy Score: 0.708
- Precision (N): 0.81, Recall (N): 0.79, F1-score (N): 0.80
- Precision (Y): 0.45, Recall (Y): 0.48, F1-score (Y): 0.47

**Feature Importance**

The top 10 most important features for predicting insurance claims fraud are:
1. incident_severity_Major Damage
2. vehicle_claim
3. property_claim
4. total_claim_amount
5. injury_claim
6. policy_annual_premium
7. months_as_customer
8. incident_hour_of_the_day
9. age
10. incident_severity_Minor Damage

**Conclusion**

Based on the evaluation results, the Support Vector Classifier and Random Forest Classifier perform relatively better compared to the other models. Features such as incident severity, claim amounts, policy details, and customer information play crucial roles in predicting insurance claims fraud. However, further tuning and optimization of the models could potentially improve their performance.


# Presentation

## Project Structure

![image](https://github.com/sunghea/Insurance_Fraud_Detection_Model/assets/143130002/4976607f-f19d-4d1e-9c48-014d2aedd703)

## Checking the prediction functionality of the saved model

![image](https://github.com/sunghea/Insurance_Fraud_Detection_Model/assets/143130002/32f7a0ce-aaa9-4f7d-a33e-2b16b5541795)


## Loading the SVM model, making predictions, and storing the results in the database from app.py

![image](https://github.com/sunghea/Insurance_Fraud_Detection_Model/assets/143130002/9ae9b79a-1109-4dd2-b917-ec1283f89530)

![image](https://github.com/sunghea/Insurance_Fraud_Detection_Model/assets/143130002/8cf57dd7-d312-41cb-9b85-bfdb8e2b6153)

![image](https://github.com/sunghea/Insurance_Fraud_Detection_Model/assets/143130002/b3e9b867-202c-4d89-85ce-6868b18fa7be)

![image](https://github.com/sunghea/Insurance_Fraud_Detection_Model/assets/143130002/63194e60-0a50-437d-add7-514c13e4b300)

