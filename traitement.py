import pandas as pd 
import numpy as np

bdd = pd.read_csv('data/bdd.csv')
df = pd.read_csv('data/tous_pays.csv')
nace = pd.read_csv('data/tous_pays_nace.csv')

companies_df = np.sort(list(set(list(df['BVDID'])))) #companies in 'tous_pays.csv'

### traitement des données financières (si données type C1 (C2) et U1 (U2) on garde U1 (U2))
df1 = df[(df['consolidation_code'] != 'C1') & (df['consolidation_code'] != 'C2')]
for company in companies_df :
	if company not in list(set(list(df1['BVDID']))) :
		df1 = pd.concat([df1, df[df['BVDID'] == company]])

### liste des companies présentes dans chaque bdd
companies_df1 = np.sort(list(set(list(df1['BVDID']))))
companies_bdd = list(bdd['BvD_ID_NUMBER'])


### traitement nace
nace = nace.loc[nace['nace_main_section'].notna(), :]
companies_nace = list(nace['BVDID'])

### reindexation et tri en fonction du BVDID
df1.set_index('BVDID', inplace = True)
df1.sort_index(inplace = True)

bdd.set_index('BvD_ID_NUMBER', inplace = True)
bdd.sort_index(inplace = True)

nace.set_index('BVDID', inplace = True)
nace.sort_index(inplace = True)
### tri des colonnes
colonnes_bdd = []
colonnes_df1 = []

## colonnes à ajouter : Nace code, profitability ?, revenue per employees

### nace 
df1 = df1.join(nace, how = 'left')

###revenue per employees
df1['revenue_per_employees'] = df1['Turnover']/df1['Employees']

### merging bdd et df1

df1 = df1.join(bdd, how = 'left')
#print(df1)
df1.to_csv('donnees_finales.csv', index = True, header = True)
#donnees_financieres = []

#for i in companies_bdd :
#	if i in companies_nace : 
#		donnees_financieres.append(df1.loc[i])
#	else :
#		donnees_financieres.append(np.nan)

#bdd['donnees_financieres'] = donnees_financieres




#print(bdd.columns, '\n\n', bdd['donnees_financieres']['AT9150092530'].columns)

#pour accèder aux données financières : print(bdd['donnees_financieres']['AT9150092530']) (Dataframe)

