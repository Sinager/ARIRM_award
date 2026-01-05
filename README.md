# ARIRM_award
Log checker for HAM awards

Work on ADIF files.

Very early - non yet working stage.
General concept:
- add all activators logs into a master file
- check hunters logs against master file

Requires ADIF Tools: https://github.com/JS2IIU-MH/adiftools-dev and PANDAS.

- adif2pickle.py -- cleanup of log, keeping only necessary fields
- attivatori-add.py file.adi -- add a pickled log into the master table of activators
- attivatori-show.py -- show master table of QSOs
- hunter.py -- cross check hunter log with the master table
