# Ouverture du fichier d'entrée
with open('input-emails.txt', 'r') as input_file:
    # Lecture des lignes du fichier dans une liste
    lines = input_file.readlines()

# Création d'une liste vide pour stocker les adresses filtrées
filtered_emails = []

# Boucle sur les lignes du fichier
for line in lines:
    # Suppression des espaces et des retours à la ligne en début et fin de ligne
    line = line.strip()
    # Vérification que la ligne ne contient pas le caractère '!'
    if '!' not in line:
        # Vérification que l'adresse se termine par '.fr'
        if line.endswith('.fr'):
            filtered_emails.append(line)

# Ouverture du fichier de sortie
with open('outputmailfr.txt', 'w') as output_file:
    # Écriture des adresses filtrées dans le fichier de sortie
    for email in filtered_emails:
        output_file.write(email + '\n')