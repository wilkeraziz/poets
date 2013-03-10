`cat data/corpora/pt-en/bitexts/99_1570.pt | sed -r 's/([[:punct:]]+)/ \1 /g;s/\s+/ /g;s/^/<s> /;s/\s*$/ <\/s>/' | tr ' ' '\n' > exercises/tokens.1`
