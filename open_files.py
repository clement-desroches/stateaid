
import pandas as pd

liste_pays = ['at', 'be', 'bg', 'cy', 'cz', 'de', 'dk', 'ee', 
'el', 'es', 'fi', 'fr', 'gb', 'gr', 'hr', 'hu', 'ie', 'it', 
'lt', 'lu', 'lv', 'lv', 'mt', 'nl', 'pl', 'pt', 'ro', 'se', 
'si', 'sk']

bdd = pd.read_csv('bdd.csv')


df = pd.read_csv('ms_firms_at_nace.txt', sep = '\t')
df = df[df['BVDID'].isin(list(bdd['BvD_ID_NUMBER']))]
df.to_csv('at.csv', index = False, header = True)

for pays in liste_pays[1:] : 
	df_pays = pd.read_csv('ms_firms_'+pays+'_nace.txt', sep = '\t')
	df_pays = df_pays[df_pays['BVDID'].isin(list(bdd['BvD_ID_NUMBER']))]
	df = pd.concat([df, df_pays])
	df_pays.to_csv(pays +'.csv', index = False, header = True)

df.to_csv('tous_pays_nace.csv', index = False, header = True)
