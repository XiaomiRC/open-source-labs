# Solution

The following code can be used to create the `add_numbers.sh` script.

```bash
#!/bin/bash
echo "Enter first number"
read x
echo "Enter second number"
read y
((sum = x + y))
echo "The result of addition=$sum"
```
OR
```bash
vim add_numbers.sh
#!/bin/bash
echo "This script finds the sum of 2 numbers"
echo "Enter the first number"
read n1
echo "Enter the second number"
read n2
sum=$(($n1+$n2))
echo "The sum is : $sum"
```

To run the script, execute the following command in the terminal:

```bash
bash add_numbers.sh
```
OR
```bash
chmod 766 add_numbers.sh
./add_numbers.sh
```
