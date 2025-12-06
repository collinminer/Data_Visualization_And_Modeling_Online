"""
Run Titanic analysis outside of Jupyter to avoid environment issues
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend

# Load data
print("Loading data...")
df = pd.read_csv('titanic_passengers.csv')
print(f"Loaded {len(df)} passengers")

# Categorize age
df.loc[df['Age'] <= 12, 'Age_Category'] = 'Child'
df.loc[(df['Age'] > 12) & (df['Age'] <= 30), 'Age_Category'] = 'Young Adult'
df.loc[(df['Age'] > 30) & (df['Age'] <= 50), 'Age_Category'] = 'Adult'
df.loc[df['Age'] > 50, 'Age_Category'] = 'Senior'

# Categorize fare
df.loc[df['Fare'] <= 10, 'Fare_Category'] = 'Low'
df.loc[(df['Fare'] > 10) & (df['Fare'] <= 30), 'Fare_Category'] = 'Medium'
df.loc[(df['Fare'] > 30) & (df['Fare'] <= 100), 'Fare_Category'] = 'High'
df.loc[df['Fare'] > 100, 'Fare_Category'] = 'Very High'

# Create categories for travel companions
df.loc[df['Parch'] == 0, 'Parch_Category'] = 'No Parents/Children'
df.loc[df['Parch'] > 0, 'Parch_Category'] = 'With Parents/Children'
df.loc[df['SibSp'] == 0, 'SibSp_Category'] = 'No Siblings/Spouse'
df.loc[df['SibSp'] > 0, 'SibSp_Category'] = 'With Siblings/Spouse'

print("\n=== SURVIVAL STATISTICS ===\n")

# 1. Sex
print("1. SURVIVAL BY SEX:")
sex_survival = pd.crosstab(df['Sex'], df['Survived'], normalize='index') * 100
print(sex_survival)
print()

# 2. Class
print("2. SURVIVAL BY PASSENGER CLASS:")
class_survival = pd.crosstab(df['Pclass'], df['Survived'], normalize='index') * 100
print(class_survival)
print()

# 3. Age
print("3. SURVIVAL BY AGE CATEGORY:")
age_survival = pd.crosstab(df['Age_Category'], df['Survived'], normalize='index') * 100
print(age_survival)
print()

# 4. Fare
print("4. SURVIVAL BY FARE CATEGORY:")
fare_survival = pd.crosstab(df['Fare_Category'], df['Survived'], normalize='index') * 100
print(fare_survival)
print()

# 5. Travel companions
print("5. SURVIVAL BY TRAVEL COMPANIONS:")
print("Parents/Children:")
parch_survival = pd.crosstab(df['Parch_Category'], df['Survived'], normalize='index') * 100
print(parch_survival)
print("\nSiblings/Spouse:")
sibsp_survival = pd.crosstab(df['SibSp_Category'], df['Survived'], normalize='index') * 100
print(sibsp_survival)
print()

# 6. Embarkation
print("6. SURVIVAL BY PORT OF EMBARKATION:")
embarked_survival = pd.crosstab(df['Embarked'], df['Survived'], normalize='index') * 100
print(embarked_survival)
print()

print("\n=== CHARACTER PROFILES ===\n")

# Most likely to survive
print("PROFILE 1: MOST LIKELY TO SURVIVE")
print("Looking for: Female, 1st Class, Child, High Fare, With companions, Cherbourg")
survivors = df[(df['Sex'] == 'female') &
               (df['Pclass'] == 1) &
               (df['Age'] <= 12) &
               (df['Fare'] > 100) &
               (df['Parch'] > 0) &
               (df['SibSp'] > 0) &
               (df['Embarked'] == 'C')]

if len(survivors) > 0:
    print(f"\nFound {len(survivors)} exact match(es):")
    print(survivors[['Name', 'Age', 'Sex', 'Pclass', 'Fare', 'Survived', 'Parch', 'SibSp', 'Embarked']])
else:
    print("\nNo exact matches. Relaxing criteria (female, 1st class, child, Cherbourg, survived):")
    survivors = df[(df['Sex'] == 'female') &
                   (df['Pclass'] == 1) &
                   (df['Age'] <= 12) &
                   (df['Embarked'] == 'C') &
                   (df['Survived'] == 1)]
    print(f"Found {len(survivors)} passenger(s):")
    if len(survivors) > 0:
        print(survivors[['Name', 'Age', 'Sex', 'Pclass', 'Fare', 'Survived', 'Parch', 'SibSp', 'Embarked']])

print("\n" + "="*80 + "\n")

# Least likely to survive
print("PROFILE 2: LEAST LIKELY TO SURVIVE")
print("Looking for: Male, 3rd Class, Adult (31-50), Low Fare, Alone, Southampton, Died")
non_survivors = df[(df['Sex'] == 'male') &
                   (df['Pclass'] == 3) &
                   (df['Age'] > 30) & (df['Age'] <= 50) &
                   (df['Fare'] <= 10) &
                   (df['Parch'] == 0) &
                   (df['SibSp'] == 0) &
                   (df['Embarked'] == 'S') &
                   (df['Survived'] == 0)]

print(f"\nFound {len(non_survivors)} passenger(s):")
if len(non_survivors) > 0:
    print(non_survivors[['Name', 'Age', 'Sex', 'Pclass', 'Fare', 'Survived', 'Parch', 'SibSp', 'Embarked']].head(10))
    print("\nSelect one of these passengers to research on Encyclopedia Titanica")

print("\n=== ANALYSIS COMPLETE ===")
print("\nNext steps:")
print("1. Review the survival statistics above")
print("2. Note the passenger names that match each profile")
print("3. Look up these passengers on Encyclopedia Titanica (https://www.encyclopedia-titanica.org/)")
print("4. Add interesting facts about them to your notebook")
