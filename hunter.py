import sys
import os
import pandas as pd

# importa il nuovo log
if len(sys.argv) == 2:
	hunter_df = pd.read_pickle(sys.argv[1])
	print('apro ', end='')
	print(sys.argv[1])
	hunter_lst = hunter_df.values.tolist()
	#print(hunter_lst)
    
else:
   print("Utilizzo: python hunter.py <nomelog>")
   quit()

master_df = pd.read_pickle("./master_pkl.zip")
master_dic = master_df.set_index('CALL').T.to_dict()
#print(master_dic)

score = 0

for newqso in hunter_lst:
	call = newqso[2]
	inlog = any(call for x in master_dic)
	if inlog:
		if master_dic[call]['QSO_DATE'] == newqso[3]:
			if master_dic[call]['QSO_DATE'] == newqso[3]:
				print(call, end=' ')
				print(newqso[3], end=' ')
				print(newqso[1], end=' <> ') 
				print(master_dic[call]['BAND'], end=' ')
				print(master_dic[call]['QSO_DATE'], end=' ')
				print(master_dic[call]['STATION_CALLSIGN'])
				if master_dic[call]['STATION_CALLSIGN'] == 'IQ0RM': score += 5
				else: score += 1
print("Tot score: ", end='')
print(score)

