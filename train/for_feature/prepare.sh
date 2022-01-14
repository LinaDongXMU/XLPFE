cd ./pocket
sed -i '/CONECT/d' *_pocket.pdb
cd ../fullprotein
sed -i '/HEADER/d;/COMPND/d;/SEQRES/d;/REMARK/d;/END/d;/MASTER/d;/TER/d;/SSBOND/d;/HET/d;/HELIX/d;/SHEET/d;/CONECT/d' *_protein.pdb
