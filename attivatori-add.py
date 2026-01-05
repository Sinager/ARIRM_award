import sys
import os
import pandas as pd

# importa il nuovo log
if len(sys.argv) == 2:
	nuovo_df = pd.read_pickle(sys.argv[1])
	print('apro ', end='')
	print(sys.argv[1])
	nuovo_lst = nuovo_df.values.tolist()
	#print(nuovo_lst)
    
else:
   print("Utilizzo: python attivatori.py <nomelog>")
   quit()

master_df = pd.read_pickle("./master_pkl.zip")
master_lst = master_df.values.tolist()
#print(master_lst)

for newqso in nuovo_lst:
	if newqso not in master_lst:
		master_lst.append(newqso)
		print('Add: ',end='')
		print(newqso)
	else:
		print('dupe')

sommato_df = pd.DataFrame(master_lst, columns=['CALL', 'BAND', 'STATION_CALLSIGN', 'QSO_DATE', 'TIME_ON', 'TIME_OFF'])
#CALL BAND STATION_CALLSIGN  QSO_DATE TIME_ON TIME_OFF

sommato_df.to_pickle('master_pkl.zip')
renamed = '_____' + sys.argv[1]
os.rename(sys.argv[1],renamed)