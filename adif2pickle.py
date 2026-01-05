import sys
import os
import adiftools.adiftools as adiftools
# https://github.com/JS2IIU-MH/adiftools-dev

adi = adiftools.ADIFParser()

def campo(nome,riga):
	field_start = riga.find(nome)
    
	if field_start == -1:
		return('n/a')
	else:
		field_start = riga.find('>',field_start)
		field_end = riga.find('<',field_start)
		return(riga[field_start +1:field_end:])

def standardize_log(nomefile):
	fileout = nomefile.removesuffix('.adi.txt') + "-conv.adi"
	outfile = open(fileout, 'w')
	riga = ''
	with open(nomefile, 'r') as file:
		for line in file:
			line = line.strip()
			line = line.replace(' ', '')
			line = line.upper()
			riga = riga + line
			if line == '<EOH>':
				riga = ''
			if line == '<EOR>':
				riga = riga + '\r\n'
				outfile.write(riga)
				riga = ''
	outfile.close()
	file.close()
	return(fileout)

def checkapp(logoriginale):
	logfile = ''
	with open(logoriginale) as origfile:
		for line in origfile:
			logapp = campo('PROGRAMID:',line)
			if (logapp == 'QLog') or (logapp == 'BBLOGGER'):
				logfile = standardize_log(logoriginale)
				break
			else:
				logfile = logoriginale
	origfile.close()
	return(logfile)

if len(sys.argv) == 2:
	adif_in = checkapp(sys.argv[1])
	print('apro ', end='')
	print(adif_in)
    
else:
   print("Utilizzo: python adif2pickle.py <nomelog>")
   quit()

# import adif log
df_adi = adi.read_adi(adif_in) # Use your own adi file


df_activator = df_adi[['CALL','BAND','STATION_CALLSIGN','QSO_DATE','TIME_ON','TIME_OFF']].copy()
del df_adi

#print(df_activator.columns.values)
print(df_activator)

pickfile = adif_in.removesuffix('-conv.adi') + '.pick.zip'
df_activator.to_pickle(pickfile)
os.remove(adif_in)
