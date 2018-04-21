# Semantic Hash

SemaSum is a small tool for creating file hashes using real words. It is meant for making it easier to identify and remember files.

## Installation

```bash
sudo curl -L https://raw.githubusercontent.com/olastor/sema-sum/master/semasum.py -o /usr/local/bin/semasum
sudo chmod a+rx /usr/local/bin/semasum
```

## Example Usage

```bash
$ ls -lh
-rw-r--r--. 1 user user  308 21. Apr 21:37 file-01.txt
-rw-r--r--. 1 user user 1,2K 21. Apr 21:40 file-02.txt
-rw-r--r--. 1 user user  59K 21. Apr 21:37 file-03.txt

$ semasum file-01.txt
"unimproved, homely, prominent"	file-01.txt

$ semasum .
"unimproved, homely, prominent"   	file-01.txt
"pristine, unamused, insolent"    	file-03.txt
"potential, merciful, choosy"     	file-02.txt
```
