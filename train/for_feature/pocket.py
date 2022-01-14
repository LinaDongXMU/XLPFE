import os
import csv
add=open('./pocket.csv','w')
addWriter=csv.writer(add)


for filename in os.listdir('./pocket'):
    numlist=[]
    content=[]
    his=arg=lys=ile=phe=leu=trp=ala=met=pro=val=cys=asn=gly=ser=gln=tyr=thr=asp=glu=hoh=other=0
    id=filename[0:4]
    file1=open(os.path.join('./pocket',filename))
    file1content=file1.readlines()
    l=len(file1content)-1
    for a in file1content[3:l]:
        a=a.split()
        if a[5].isalnum()==True:
            if a[3]=="HOH":
                hoh=hoh+1
            if a[5] not in numlist:
                numlist.append(a[5])
                if a[3]=="HIS":
                    his=his+1
                elif a[3]=="ARG":
                    arg=arg+1
                elif a[3]=="LYS":
                    lys=lys+1
                elif a[3]=="ILE":
                    ile=ile+1
                elif a[3]=="PHE":
                    phe=phe+1
                elif a[3]=="LEU":
                    leu=leu+1
                elif a[3]=="TRP":
                    trp=trp+1
                elif a[3]=="ALA":
                    ala=ala+1
                elif a[3]=="MET":
                    met=met+1
                elif a[3]=="PRO":
                    pro=pro+1
                elif a[3]=="VAL":
                    val=val+1
                elif a[3]=="CYS":
                    cys=cys+1
                elif a[3]=="ASN":
                    asn=asn+1
                elif a[3]=="GLY":
                    gly=gly+1
                elif a[3]=="SER":
                    ser=ser+1
                elif a[3]=="GLN":
                    gln=gln+1
                elif a[3]=="TYR":
                    tyr=tyr+1
                elif a[3]=="THR":
                    thr=thr+1
                elif a[3]=="ASP":
                    asp=asp+1
                elif a[3]=="GLU":
                    glu=glu+1
                else:
                    other=other+1
        else:
            if a[3]=="HOH":
                hoh=hoh+1
            if a[4] not in numlist:
                numlist.append(a[4])
                if a[3]=="HIS":
                    his=his+1
                elif a[3]=="ARG":
                    arg=arg+1
                elif a[3]=="LYS":
                    lys=lys+1
                elif a[3]=="ILE":
                    ile=ile+1
                elif a[3]=="PHE":
                    phe=phe+1
                elif a[3]=="LEU":
                    leu=leu+1
                elif a[3]=="TRP":
                    trp=trp+1
                elif a[3]=="ALA":
                    ala=ala+1
                elif a[3]=="MET":
                    met=met+1
                elif a[3]=="PRO":
                    pro=pro+1
                elif a[3]=="VAL":
                    val=val+1
                elif a[3]=="CYS":
                    cys=cys+1
                elif a[3]=="ASN":
                    asn=asn+1
                elif a[3]=="GLY":
                    gly=gly+1
                elif a[3]=="SER":
                    ser=ser+1
                elif a[3]=="GLN":
                    gln=gln+1
                elif a[3]=="TYR":
                    tyr=tyr+1
                elif a[3]=="THR":
                    thr=thr+1
                elif a[3]=="ASP":
                    asp=asp+1
                elif a[3]=="GLU":
                    glu=glu+1
                else:
                    other=other+1

    content.append(id)
    content.append(his)
    content.append(arg)
    content.append(lys)
    content.append(ile)
    content.append(phe)
    content.append(leu)
    content.append(trp)
    content.append(ala)
    content.append(met)
    content.append(pro)
    content.append(val)
    content.append(cys)
    content.append(asn)
    content.append(gly)
    content.append(ser)
    content.append(gln)
    content.append(tyr)
    content.append(thr)
    content.append(asp)
    content.append(glu)
    content.append(hoh)
    addWriter.writerow(content)
    file1.close()

add.close()
