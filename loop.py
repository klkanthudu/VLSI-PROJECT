#!/usr/bin/perl

$n1 = 10;
  ##scenario1
if ($n1 > 10) {
	print "number is greater then 10\n";
} ##end if

##scenario2

if ($n1 > 10) {
	print "number is greater then 10\n";
} else {
	print "number isnot greater then 10\n";
} ##end if

##scenario3

if ($n1 > 10 ) {
	print "number is greater then 10\n";
} elsif($n1 < 10) {
	print "number is lesser then 10\n";
} else {
	print "number is neither greater then not lesser then 10\n";
} ##end if




##WHILE LOOP

$n2 = 20;
while ($n2 < 40) {
	print "$n2\n";
	$n2 = $n2 + 6;
} #end while

#forloop

for ($n=5; $n < 30; $n = $n +5) {
	print "forloop:$n\n";
}

@arr =(34,45,45,33);
foreach $v (@arr) {
	print"$v\n";
}





