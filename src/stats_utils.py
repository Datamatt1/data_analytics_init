import pandas as pd

sales = pd.read_csv("data/sales.csv")

sales=sales[sales["id"]>0]
sales=sales[sales["montant"]>0]
sales=sales.sort_values("montant")
print(sales)

nb_total_trans_valide=len(sales)
somme_total_ventes=sales["montant"].sum()
vente_moyenne=somme_total_ventes/nb_total_trans_valide
double_moyenne=vente_moyenne*2
mediane_vente=sales["montant"].median()
ecart_type=sales["montant"].std()
min, max = sales["montant"].min(), sales["montant"].max()
## outliers_values=sales[sales["montant"]>double_moyenne]  ## Dataframe ok ou pas ? pour le dictionnaire ?
outliers_values = sales[sales["montant"] > double_moyenne]["montant"].tolist()
print(f"Nombre de transactions valides : {nb_total_trans_valide}")
print(f"Somme totale des ventes : {somme_total_ventes}€")
print(f"Vente moyenne : {vente_moyenne}€")
print(f"Vente médiane : {mediane_vente}€")
print(f"Ecart type :{ecart_type.round(2)}")
print(f"Prix minimum {min}€, prix maximum : {max}€")
print(outliers_values)

resume={
    "Nombre_transactions_valides" : int(nb_total_trans_valide),
    "Somme_ventes": float(somme_total_ventes.round(2)),
    "Vente_moyenne" : float(vente_moyenne.round(2)),
    "Vente_mediane" : float(mediane_vente.round(2)),
    "Ecart_type" : float(ecart_type.round(2)),
    "Prix_minimum" : float(min),
    "Prix_maximum" : float(max),
    "Valeurs_extremes" : outliers_values
}

print(resume)

#v2 - Doïna

def analyser_ventes(sales):
    sales=sales[sales["id"]>0] & sales[sales["montant"]>0]
    sales=sales.sort_values("montant")

    if len(sales) == 0 :
        print("erreur")
        return{"erreur"}

    nb_total_trans_valide=len(sales)
    somme_total_ventes=sales["montant"].sum()
    vente_moyenne=somme_total_ventes/nb_total_trans_valide
    double_moyenne=vente_moyenne*2
    mediane_vente=sales["montant"].median()
    ecart_type=sales["montant"].std()
    min, max = sales["montant"].min(), sales["montant"].max()
    outliers_values = sales[sales["montant"] > double_moyenne]["montant"].tolist()

    resume={"Nombre_transactions_valides" : int(nb_total_trans_valide),
        "Somme_ventes": float(somme_total_ventes.round(2)),
        "Vente_moyenne" : float(vente_moyenne.round(2)),
        "Vente_mediane" : float(mediane_vente.round(2)),
        "Ecart_type" : float(ecart_type.round(2)),
        "Prix_minimum" : float(min),
        "Prix_maximum" : float(max),
        "Valeurs_extremes" : outliers_values}

    return resume

resultat = analyser_ventes(sales)
print(resultat)