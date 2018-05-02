#!/bin/csh
set word = "anything"
     while ($word != "")
       echo -n "Enter a word to check (Return to exit): "
       set word = $<
       if ($word != "") grep $word /usr/share/dict/words
     end
