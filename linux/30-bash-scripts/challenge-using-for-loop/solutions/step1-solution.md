# Solution

The following code can be used to create the 'for_example.sh' script.

```bash
#!/bin/bash
for ((counter = 10; counter > 0; counter--)); do
  echo -n "$counter "
done
printf "\\n"
```
**MY SOUTION**
```bash
#!/bin/bash               
for((i=10;i>=1;i--));                                                                                                                                                
do             
echo -n "$i "  
done
```

To run the script, execute the following command in the terminal:

```bash
$ bash for_example.sh
```

This will output the values from 10 to 1 on a single line.
