import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#loading data
df= pd.read_csv("titanic.csv")
df.head(5)
df.info()
df.describe()


#cleaning data
print(df.isnull().sum())
df["Age"].fillna(df["Age"].mean(), inplace=True)
df.dropna(subset=["Cabin"])
df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)
df.drop_duplicates(inplace=True)

#exploring data
# Survival count
plt.figure()
sns.countplot(x='Survived', data=df)
plt.title("Survival Count")
plt.show()


# Survival by Gender
plt.figure()
sns.countplot(x='Sex', hue='Survived', data=df)
plt.title("Survival by Gender")
plt.show()


# Survival by Passenger Class
plt.figure()
sns.countplot(x='Pclass', hue='Survived', data=df)
plt.title("Survival by Passenger Class")
plt.show()


# Age distribution
plt.figure()
sns.histplot(df['Age'], bins=30)
plt.title("Age Distribution")
plt.show()

#data analysis

print(df.groupby('Sex')['Survived'].mean())

print(df.groupby('Pclass')['Survived'].mean())

print(df.groupby('Survived')['Age'].mean())