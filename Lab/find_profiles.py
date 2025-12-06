"""
Find realistic passenger profiles
"""
import pandas as pd

df = pd.read_csv('titanic_passengers.csv')

print("="*80)
print("SEARCHING FOR PROFILE 1: MOST LIKELY TO SURVIVE")
print("="*80)

# Try different combinations
print("\n1. Female, 1st Class, Cherbourg, Survived:")
p1 = df[(df['Sex'] == 'female') & (df['Pclass'] == 1) & 
        (df['Embarked'] == 'C') & (df['Survived'] == 1)]
print(f"Found {len(p1)} passengers")
if len(p1) > 0:
    print(p1[['Name', 'Age', 'Fare', 'Parch', 'SibSp']].head(10))

print("\n2. Female, 1st Class, Child (<=12), Survived:")
p2 = df[(df['Sex'] == 'female') & (df['Pclass'] == 1) & 
        (df['Age'] <= 12) & (df['Survived'] == 1)]
print(f"Found {len(p2)} passengers")
if len(p2) > 0:
    print(p2[['Name', 'Age', 'Embarked', 'Fare', 'Parch', 'SibSp']])

print("\n3. Female, 1st Class, With family, High fare, Survived:")
p3 = df[(df['Sex'] == 'female') & (df['Pclass'] == 1) & 
        ((df['Parch'] > 0) | (df['SibSp'] > 0)) &
        (df['Fare'] > 50) & (df['Survived'] == 1)]
print(f"Found {len(p3)} passengers")
if len(p3) > 0:
    print(p3[['Name', 'Age', 'Embarked', 'Fare', 'Parch', 'SibSp']].head(10))

print("\n" + "="*80)
print("SEARCHING FOR PROFILE 2: LEAST LIKELY TO SURVIVE")
print("="*80)

print("\nMale, 3rd Class, Adult (31-50), Alone, Southampton, Low Fare, Died:")
p4 = df[(df['Sex'] == 'male') & (df['Pclass'] == 3) & 
        (df['Age'] > 30) & (df['Age'] <= 50) &
        (df['Parch'] == 0) & (df['SibSp'] == 0) &
        (df['Embarked'] == 'S') & (df['Fare'] <= 10) &
        (df['Survived'] == 0)]
print(f"Found {len(p4)} passengers")
if len(p4) > 0:
    print(p4[['Name', 'Age', 'Fare']].head(5))
    print("\nRecommended: Allen, Mr. William Henry (Age 35, Fare £8.05)")
