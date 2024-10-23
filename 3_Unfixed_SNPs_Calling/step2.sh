cat *mixmarkkept > all_KEPT.txt; perl /home/Unfixed_SNPs_Calling/loci_freq_count.pl all_KEPT.txt > kept_repeat.txt; 
cat *mixmark > all_MIX.txt; perl /home/Unfixed_SNPs_Calling/loci_freq_count.pl all_MIX.txt > mix_repeat.txt; 
perl /home/Unfixed_SNPs_Calling/repeat_number_merge.pl mix_repeat.txt kept_repeat.txt > merge_kept_mix.txt; 
perl /home/Unfixed_SNPs_Calling/ratio.pl merge_kept_mix.txt > merge_kept_mix_ratio.txt; 
awk '$4>=5' merge_kept_mix_ratio.txt |awk '$6>0.6'|cut -f1|while read i;do echo $i > $i.per5up.txt;grep -w $i all_KEPT.txt|cut -f12 >> $i.per5up.txt;done
paste *per5up.txt > 5up_0.6_paste.txt
perl /home/Unfixed_SNPs_Calling/stdv.pl 5up_0.6_paste.txt |awk '$2<0.25'|cut -f1 > 5up_0.6_0.25.list
perl /home/Unfixed_SNPs_Calling/freq_extract.pl 5up_0.6_0.25.list 5up_0.6_paste.txt > 5up_0.6_0.25.txt
awk '$4>=5' merge_kept_mix_ratio.txt|cut -f1 > 5up.list
perl /home/Unfixed_SNPs_Calling/repeat_loci.pl 5up_0.6_0.25.list 5up.list > 5up_remove_loc.list
