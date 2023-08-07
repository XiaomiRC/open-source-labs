# Solution

```bash
#!/bin/bash

string1="Linux"
string2="Hint"
string3="$string1$string2"
string3+=" is a good tutorial blog site"
echo $string3
```
**MY SOLUTION**
```bash
vim string_combine.sh
#!/bin/bash
echo "enter string 1"
read string1
echo "enter string 2"
read string2
string3=$string1$string2
string3+=" is a good tutorial blog site"
echo $string3
```
