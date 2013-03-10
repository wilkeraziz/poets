Simplest tokenizer

`sed -r 's/([[:punct:]]+)/ \1 /g;s/\s+/ /g'`

A bit more for English

`sed -r "s/([[:alpha:]])'([sdt])/\1 \&quot;\2/g;s/([[:punct:]]+)/ \1 /g;s/\s+/ /g;s/[&] quot ; ([sdt])/'\1/g;"`

A bit more for Portuguese

`sed -r "s/([[:alpha:]])-([[:alpha:]])/\1 @-@ \2/g;s/([[:punct:]])/ \1 /g;s/\s+/ /g;s/ @ \- @ / @-@ /g"`

or

`sed -r "s/([[:alpha:]])-([[:alpha:]])/\1 @-@ \2/g;s/([[:punct:]])/ \1 /g;s/\s+/ /g;s/ @ \- @ /-/g"`

