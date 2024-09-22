import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle
import os

# Définir le chemin du fichier CSV
data_path = os.path.join('data', 'train.csv')

# Charger les données
data = pd.read_csv(data_path)

# Prétraitement des données
# Remplacer 'Sex' par des valeurs numériques
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})

# Remplacer les valeurs manquantes dans 'Embarked' par 'S'
data['Embarked'] = data['Embarked'].fillna('S')
data['Embarked'] = data['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})

# Remplacer les valeurs manquantes dans 'Age' et 'Fare' par la médiane
data['Age'] = data['Age'].fillna(data['Age'].median())
data['Fare'] = data['Fare'].fillna(data['Fare'].median())

# Sélectionner les features pertinentes
features = ['Pclass', 'Sex', 'Age', 'Fare', 'Embarked']
X = data[features]
y = data['Survived']

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Entraîner un modèle de régression logistique
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Sauvegarder le modèle entraîné dans un fichier .pkl
model_path = os.path.join('data', 'titanic_model.pkl')
with open(model_path, 'wb') as file:
    pickle.dump(model, file)

print("Modèle entraîné et sauvegardé avec succès dans 'data/titanic_model.pkl'")
