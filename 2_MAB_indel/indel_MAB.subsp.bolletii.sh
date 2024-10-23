ls *.sort.bam|while read i
do a=${i%.sort.bam}
b=${a}
var=${a}.varscan.vcf
format=${a}.indel_for
fix=${a}.indel_fix
filter=${a}.indel_filter
ppe=${a}.indel_ppe
echo "samtools mpileup -q 30 -Q 20 -BOf /home/ND140/ytt/NTM/evolution/mapping/MAB.subsp.bolletii.fna $i | java -jar /home/edwin/bin/VarScan.v2.3.6.jar mpileup2indel -–output-vcf 1 > $var;perl /home/edwin/script/varscan_work_flow/1_format_trans.pl $var > $format; perl /home/ND140/ytt/NTM/scripts/indel/2_fix_indel_extract.pl $format > $fix; perl /home/ND140/ytt/NTM/scripts/indel/3_indel_filter_fix_extract.pl $format > $filter; perl /home/ND140/ytt/NTM/scripts/indel/0.1_PE_IS_filt_Rv.pl /home/ND140/ytt/NTM/evolution/mapping/MAB.subsp.bollitii_repeat_PEPPE_phage_transposase.loci.txt $filter > $ppe;"
done
