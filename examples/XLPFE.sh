#!bin/bash
cd ./for_feature
mkdir xscore
mkdir ligand
mkdir pocket
mkdir fullprotein
cd ../data
cp *_protein.pdb ../for_feature/xscore
cp *_ligand.mol2 ../for_feature/xscore
cp *_ligand.mol2 ../for_feature/ligand
cp *_pocket.pdb ../for_feature/pocket
cp *_protein.pdb ../for_feature/fullprotein
cd ../for_feature
sh prepare.sh
sh xscore.sh
sh ligand.sh
python pocket.py
python fullprotein.py
python combine_feature.py
cp test.csv ../for_model
#cd ../for_model
#python XLPFE.py
#cp results.csv ..
