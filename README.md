
# Insurance Fraud Prediction Model
Final Project for Data Analytics Boot Camp

-- TBD  ---

## Background 
ABC Insurance has requested you, as a data analyst, to build a model for identifying the risk of insurance fraud using their historical claims activity dataset. 
They aim to establish an insurance fraud management system.

Part 1: Extract from Excel

** handle missing values and "?" values:**

- Replace missing values in the authorities_contacted column with "Other".
- Replace "?" values in the collision_type column with "Other" if incident_severity is "Trivial Damage" or "Minor Damage".
- Replace "?" values in the police_report_available column with "YES" if authorities_contacted is "Police", "Ambulance", or "Fire", otherwise replace with "NO".
- Replace "?" values in the property_damage column with "YES" if property_claim exists, otherwise replace with "NO".

**These adjustments maintain the integrity of the entire dataset, which consists of 1000 entries.**


** Would you trust this model to detect if a fraud will be detected?**

## Datasets used: 
[https://www.kaggle.com/datasets/mastmustu/insurance-claims-fraud-data](https://www.kaggle.com/code/niteshyadav3103/insurance-fraud-detection-using-12-models/input)

## Code snippets



## Limitations
- Amad

## Presentation
![image](https://github.com/sunghea/Insurance_Fraud_Detection_Model/assets/143130002/dc7ee556-73ed-460e-af3f-e211c3cd9cbc)

**Random_Forest**

![image](https://github.com/sunghea/Insurance_Fraud_Detection_Model/assets/143130002/61b0cb77-d887-402e-a0d6-b5a133936c28)
![image](https://github.com/sunghea/Insurance_Fraud_Detection_Model/assets/143130002/6514220d-c7e4-49b7-8139-531471b3514c)


**Support vector machine linear classifier**

![image](https://github.com/sunghea/Insurance_Fraud_Detection_Model/assets/143130002/ad41e605-2997-4a65-8638-202e650f1638)


**KNN_classifier**

![image](https://github.com/sunghea/Insurance_Fraud_Detection_Model/assets/143130002/270def0c-4f1f-4709-9c33-d13bbe5117c0)

**Decision Tree**

![image](https://github.com/sunghea/Insurance_Fraud_Detection_Model/assets/143130002/039b7629-e557-48ba-9cfa-ac7bb33f87b7)

![transactions_tree (1)](https://github.com/sunghea/Insurance_Fraud_Detection_Model/assets/143130002/e9f9114c-0e8a-489b-8b69-12f470173074)

