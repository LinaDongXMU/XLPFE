# XLPFE
XLPFE: a Simple and Effective Machine Learning Scoring Function for Protein-ligand Scoring and Ranking

---------------------------------------------------------------------------------------------------------------------------------------------
See requrements.txt first.

This is an instruction for use.

---------------------------------------------------------------------------------------------------------------------------------------------
1 To apply our model and parameters


copy the file named application to your service

open the file named application

make a new file and name it data

put your data(*_protein.pdb, *_pocket.pdb and *_ligand.mol2) in the file named data

sh XLPFE.sh

then the results.csv will show in the file named application

Second time when you want to apply the model without training again, note the XLPFE/application/for_model/XLPFE.py line 24，25，27 and 35

---------------------------------------------------------------------------------------------------------------------------------------------
2 To train your model and paramenters


copy the file named train to your service

open the file named train

make a new file and name it data

put your data(*_protein.pdb, *_pocket.pdb and *_ligand.mol2) in the file named data

substitute the file named exp.csv in for_model with your own exp.csv

sh XLPFE.sh

then the train.csv and XLPFE.pkl will show in the file named train

substitute the two to the application/for_model and do 1, then you can test your own model

---------------------------------------------------------------------------------------------------------------------------------------------
3 We set up an file named examples which includes 5 structures from PDBbind and the results are shown in the file

Remember copy XLPFE/application/for_model/XLPFE.pkl to XLPFE/examples/for_model

Then examples can be repeated
