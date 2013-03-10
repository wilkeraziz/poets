First let's get some data

`head corpora/pt-en/bitexts/99_1570.pt`

Now let's replace every sequence of punctuation and white spaces by a new line

`head corpora/pt-en/bitexts/99_1570.pt | tr -s '[[:punct:]][[:blank:]]' '\n'`

We can now sort the output and count duplicates

`head corpora/pt-en/bitexts/99_1570.pt | tr -s '[[:punct:]][[:blank:]]' '\n' | sort | uniq -c`

Finally we can sort the types by their frequencies

`head corpora/pt-en/bitexts/99_1570.pt | tr -s '[[:punct:]][[:blank:]]' '\n' | sort | uniq -c | sort -n -k1 -r > types.txt`

We could now count the types

`wc -l types.txt`

We could have counted the tokens

`head corpora/pt-en/bitexts/99_1570.pt | tr -s '[[:punct:]][[:blank:]]' '\n' | wc -l`
