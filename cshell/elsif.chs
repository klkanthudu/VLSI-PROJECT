#!/bin/csh
if ($#argv == 0) then  
        echo "No number to classify"  
     else if ($#argv > 0) then  
        set number = $argv[1]  
        if ($number < 0) then  
           @ class = 0  
        else if (0 <= $number && $number < 100) then  
           @ class = 1  
        else if (100 <= $number && $number < 200) then  
           @ class = 2  
        else  
           @ class = 3  
        endif
        echo The number $number is in class $class
     endif  
