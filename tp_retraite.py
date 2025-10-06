nb_trimestre = 170
age = 64

# < 62 ans taux_retraite = 0
# > 67 ans taux_retraite = 1
# Si né > 1968 il faut avoir 172 trimestre
# Règle 62 ans + nb trimestre manquant => afficher l'age de retraite à taux plein

if age < 62:
    print("Pas de retraite")
elif age > 67:
    print("Retraite à taux plein")
else:
    if nb_trimestre >= 172:
        print("Retraite à taux plein")
    else:
        nb_trimestre_restant = 172 - nb_trimestre
        age_prevu = age + nb_trimestre_restant / 4
        if age_prevu >= 67:
            print("Retraite à 67 ans")
        else:
            print(f"Retraite à {age_prevu} ans")