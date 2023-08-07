# Solution

Here is the Bash script that appends new content to the 'book.txt' file:

```bash
#!/bin/bash

echo "Before appending the file"
cat book.txt

echo "Learning Laravel 5" >> book.txt
echo "After appending the file"
cat book.txt
```
**MY SOLUTION**
```bash
vim book.txt
Secret Seven
Nancy drew
Deltora quest
Malory High

vim append_file.sh
#!/bin/bash
echo "Before appending"
cat book.txt
echo "Larning Laravel 5" >> book.txt
echo "After appending"
cat book.txt
```
To run the script, use the following command:

```bash
bash append_file.sh
```
