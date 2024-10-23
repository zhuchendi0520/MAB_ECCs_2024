ls *cns|while read i
do a=${i%.cns}
markkept=${a}.mixmarkkept
keptfilt=${a}.keptfilt
keptsnp=${a}.keptsnp
keptanofilt=${a}.keptanofilt
echo "perl /home/Unfixed_SNPs_Calling/repeatloci_filter.pl 5up_remove_loc.list $markkept > $keptfilt; cut -f9-11 $keptfilt > $keptsnp; perl /home/edwin/script/translate/1_M.abscessus_Annotation.pl $keptsnp > $keptanofilt;"
done
