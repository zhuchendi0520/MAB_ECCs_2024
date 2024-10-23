#!usr/bin/perl
use warnings;

while(<>){
chomp;
@a=split "\t",$_;
$a[4]=~s/%//;
if($a[4]>=75){
print "$a[1]\t$a[2]\t$a[3]\n";
}
}
