ls *cns|while read i
do a=${i%.cns}
cns=${a}.cns
dep=${a}.dep
forup=${a}.forup
mix=${a}.mix
mixfor=${a}.mixfor
mixmark=${a}.mixmark
echo "sed 's/:/\t/g' $cns|awk '{if (\$6 >= 3){n++;sum+=\$6}} END {print \"\t\",n/4411532,\"\t\",sum/n}' > $dep; perl /home/MD140/cyw/HIV/Unfixed_SNPs_Calling/mix_extract_0.95.pl $forup > $mix; perl /home/MD140/cyw/HIV/Unfixed_SNPs_Calling/forup_format.pl $mix > $mixfor; perl /home/MD140/cyw/HIV/Unfixed_SNPs_Calling/info_mark.pl $mixfor > $mixmark; perl /home/MD140/cyw/HIV/Unfixed_SNPs_Calling/redepin_filt.pl /home/MD140/cyw/HIV/Unfixed_SNPs_Calling/Excluded_loci_mask.list $dep $mixmark;"
done
