cd '/home/userroot/ncbi/public/sra/'
while read line
do
prefetch line
done < './SRR_Acc_List.txt'
