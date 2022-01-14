##

function get_bond()
{
        #printf "%-4s," "${i:0:4}" >> list_bond.csv

        awk '/<TRIPOS>BOND/{f=1;next} /<TRIPOS>SUBSTRUCTURE/{f=0} f' $i | awk '{print $4}' | sort | uniq -c > atm.tmp
        > atm.tmp_2
        if [[ -n $(grep  1$ atm.tmp) ]];then echo $(grep  1$  atm.tmp | awk '{printf "%2s\n", $1}') >> atm.tmp_2;  else echo "0" >> atm.tmp_2;fi
        if [[ -n $(grep  2$ atm.tmp) ]];then echo $(grep  2$  atm.tmp | awk '{printf "%2s\n", $1}') >> atm.tmp_2;  else echo "0" >> atm.tmp_2;fi
        if [[ -n $(grep  3$ atm.tmp) ]];then echo $(grep  3$  atm.tmp | awk '{printf "%2s\n", $1}') >> atm.tmp_2;  else echo "0" >> atm.tmp_2;fi
        if [[ -n $(grep am$ atm.tmp) ]];then echo $(grep am$  atm.tmp | awk '{printf "%2s\n", $1}') >> atm.tmp_2;  else echo "0" >> atm.tmp_2;fi
        if [[ -n $(grep ar$ atm.tmp) ]];then echo $(grep ar$  atm.tmp | awk '{printf "%2s\n", $1}') >> atm.tmp_2;  else echo "0" >> atm.tmp_2;fi
#        if [[ -n $(grep du$ atm.tmp) ]];then echo $(grep du$  atm.tmp | awk '{printf "%2s\n", $1}') >> atm.tmp_2;  else echo "0" >> atm.tmp_2;fi

        paste -s -d "," atm.tmp_2 >> list_bond.csv
}


function get_element()
{
        chg=$(awk '/<TRIPOS>ATOM/{f=1;next} /<TRIPOS>BOND/{f=0} f' $i | awk '{sum += $NF};END {print sum}'); int=$(printf "%.0f\n" $chg)
        printf "%-4s," "${i:0:4}" >> list_chg.tmp
        printf "%2s\n" $int >> list_chg.tmp
        awk '/<TRIPOS>ATOM/{f=1;next} /<TRIPOS>BOND/{f=0} f' $i | awk '{print $6}' | awk -F '.' '{print $1}' | sort | uniq -c > atm.tmp
        > atm.tmp_2
        if [[ -n $(grep C$ atm.tmp) ]];then echo $(grep C$ atm.tmp | awk '{printf "%2s\n", $1}') >> atm.tmp_2;  else echo "0" >> atm.tmp_2;fi
        if [[ -n $(grep N atm.tmp) ]];then echo $(grep N atm.tmp |   awk '{printf "%2s\n", $1}') >> atm.tmp_2;  else echo "0" >> atm.tmp_2;fi
        if [[ -n $(grep O atm.tmp) ]];then echo $(grep O atm.tmp |   awk '{printf "%2s\n", $1}') >> atm.tmp_2;  else echo "0" >> atm.tmp_2;fi
        if [[ -n $(grep H atm.tmp) ]];then echo $(grep H atm.tmp |   awk '{printf "%2s\n", $1}') >> atm.tmp_2;  else echo "0" >> atm.tmp_2;fi
        if [[ -n $(grep F atm.tmp) ]];then echo $(grep F atm.tmp |   awk '{printf "%2s\n", $1}') >> atm.tmp_2;  else echo "0" >> atm.tmp_2;fi
        if [[ -n $(grep P atm.tmp) ]];then echo $(grep P atm.tmp |   awk '{printf "%2s\n", $1}') >> atm.tmp_2;  else echo "0" >> atm.tmp_2;fi
        if [[ -n $(grep S atm.tmp) ]];then echo $(grep S atm.tmp |   awk '{printf "%2s\n", $1}') >> atm.tmp_2;  else echo "0" >> atm.tmp_2;fi
        if [[ -n $(grep Cl atm.tmp) ]];then echo $(grep Cl atm.tmp | awk '{printf "%2s\n", $1}') >> atm.tmp_2;  else echo "0" >> atm.tmp_2;fi
        if [[ -n $(grep Br atm.tmp) ]];then echo $(grep Br atm.tmp | awk '{printf "%2s\n", $1}') >> atm.tmp_2;  else echo "0" >> atm.tmp_2;fi
        if [[ -n $(grep I atm.tmp) ]];then echo $(grep I atm.tmp |   awk '{printf "%2s\n", $1}') >> atm.tmp_2;  else echo "0" >> atm.tmp_2;fi


        paste -s -d "," atm.tmp_2 >> list_atm.tmp
}


#main
#
path=./ligand
cd $path
> list_bond.csv
> list_chg.tmp
> list_atm.tmp
for i in $(ls *.mol2);do
		get_bond
		get_element 
done

sed -i '1i\1,2,3,am,ar' list_bond.csv


sed -i 's/-0/ 0/' list_chg.tmp
paste -d "," list_chg.tmp list_atm.tmp > list.csv
sed -i '1i\Name,q,C,N,O,H,F,P,S,Cl,Br,I' list.csv

paste -d "," list.csv list_bond.csv > ../ligand.csv
#echo "Please view list_liginfo.csv about ligand_infomation!"
