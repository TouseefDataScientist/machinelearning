import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv")
print(df.head())

x = df["Age"]
y = df["Fare"]
plt.scatter(x, y, c='blue', alpha=1)
plt.xlabel('Age')
plt.ylabel('Fare')
plt.title('Scatter Plot of Age vs. Fare')
plt.show()

colors = ['red' if age > 30 else 'green' for age in x]
plt.scatter(x, y, c=colors, alpha=1)
plt.xlabel('Age')
plt.ylabel('Fare')
plt.title('Scatter Plot of Age vs. Fare with Age-based Colors')
plt.show()

def age_category(age):
    if age <= 12:
        return 'Child'
    elif age <= 19:
        return 'Teen'
    elif age <= 30:
        return 'Adult'
    elif age <= 40:
        return 'Old'
    else:
        return 'Senior'

df['AgeCategory'] = df['Age'].apply(age_category)
categories = df['AgeCategory'].unique()
colors_dict = {'Child': 'yellow', 'Teen': 'purple', 'Adult': 'blue', 'Old': 'orange', 'Senior': 'brown', 'Unknown': 'gray'}
colors = df['AgeCategory'].map(colors_dict)

for category in categories:
    mask = df['AgeCategory'] == category
    plt.scatter(df[mask]['Age'], df[mask]['Fare'], c=colors_dict[category], label=category)

plt.xlabel('Age')
plt.ylabel('Fare')
plt.title('Scatter Plot of Age vs. Fare with Age Categories')
plt.legend()
plt.show()
