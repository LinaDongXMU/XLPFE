import csv

xscore=open('./xscore.csv')
xscoreReader=csv.reader(xscore)
xscoreData=list(xscoreReader)
ligand=open('./ligand.csv')
ligandReader=csv.reader(ligand)
ligandData=list(ligandReader)
pocket=open('./pocket.csv')
pocketReader=csv.reader(pocket)
pocketData=list(pocketReader)
fullprotein=open('./fullprotein.csv')
fullproteinReader=csv.reader(fullprotein)
fullproteinData=list(fullproteinReader)
exp=open('./exp.csv')
expReader=csv.reader(exp)
expData=list(expReader)

add=open('./train.csv','w')
addWriter=csv.writer(add)

d=['Name','VDW','HB','HP','HM','HS','RT','x-score','q','C','N','O','H','F','P','S','Cl','Br','I','1','2','3','am','ar','his','arg','lys','ile','phe','leu','trp','ala','met','pro','val','cys','asn','gly','ser','gln','tyr','thr','asp','glu','hoh','phis','parg','plys','pile','pphe','pleu','ptrp','pala','pmet','ppro','pval','pcys','pasn','pgly','pser','pgln','ptyr','pthr','pasp','pglu','exp']
addWriter.writerow(d)

for i in xscoreData:
    a=i[0]
    for j in ligandData:
        b=j[0]
        if a==b:
            c=i
            c=c+j[1:]
            for k in pocketData:
                x=k[0]
                if x==b:
                    c=c+k[1:]
                    for l in fullproteinData:
                        y=l[0]
                        if y==x:
                            c=c+l[1:]
                            for m in expData:
                                z=m[0]
                                if z==y:
                                    c.append(m[1])
                                    addWriter.writerow(c)


xscore.close()
ligand.close()
pocket.close()
fullprotein.close()
exp.close()
add.close()