import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
titanic = sns.load_dataset('titanic')

# Check basic info
print(titanic.head())

# Plot 1: Survival count
sns.countplot(x='survived', data=titanic)
plt.title('Survival Count')
plt.xlabel('Survived (0 = No, 1 = Yes)')
plt.ylabel('Count')
plt.show()

# Plot 2: Survival by gender
sns.countplot(x='sex', hue='survived', data=titanic)
plt.title('Survival by Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.legend(title='Survived')
plt.show()

# Plot 3: Age distribution
sns.histplot(titanic['age'].dropna(), bins=30, kde=True)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

# Plot 4: Class vs Survival
sns.countplot(x='class', hue='survived', data=titanic)
plt.title('Passenger Class vs Survival')
plt.xlabel('Passenger Class')
plt.ylabel('Count')
plt.legend(title='Survived')
plt.show()
