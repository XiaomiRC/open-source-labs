# Solution

```bash
#!/bin/bash
valid=true
count=1
while $valid; do
  echo $count
  if [ $count -eq 5 ]; then
    break
  fi
  ((count++))
done
```
**MY SOLUTION**
```bash
#!/bin/bash               
count=1
while true; 
do
echo $count
if [ $count -eq 5 ];
then
break
fi
((count ++))
done
```
To run the Bash file, use the following command:

```
bash while_example.sh
```
