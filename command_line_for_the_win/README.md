# Command line for the win

## 0-first_9_tasks
```bash
echo "hello world"
```

```bash
pwd
```

```bash
ls -1
```

```bash
head access.log
```

```bash
tail -n 5 access.log
```

```bash
touch take-the-command-challenge
```

```bash
mkdir -p tmp/files
```

```bash
cp take-the-command-challenge tmp/files/
```

```bash
mv take-the-command-challenge tmp/files/
```

## 1-next_9_tasks

```bash
ln -s tmp/files/take-the-command-challenge take-the-command-challenge
```

```bash
mkdir -p /var/challenges/delete_files
find /var/challenges/delete_files -mindepth 1 -delete
```

```bash
find . -type f -name "*.doc" -delete
```

```bash
grep "GET" access.log
```

```bash
grep -l "500" *
```

```bash
find . -type f -name "access.log*" | grep -oE './[^/]+$' | sed 's|^./||'
```

```bash
grep -rh "500" --include="access.log*" .
```

```bash
grep -rhoE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b" --include="access.log*" . | sort -u
```

```bash
find . -maxdepth 1 -type f | wc -l
```

##2-next_9_tasks

```bash
sort access.log
```

```bash
grep -c "GET" access.log
```

```bash
tr ';' '\n' < split-me.txt
```

```bash

#!/bin/bash

for ((i=1; i<=100; i++)); do
  echo -n "$i "
done

echo # new line after the numbers
```
```bash
find . -type f -name "*.txt" -exec sed -i 's/challenges are difficult//g' {} +
```

```bash
awk '{ sum += $1 } END { print sum }' sum-me.txt
```

```bash
find . -type f -exec basename {} \;
```

```bash
find . -type f -execdir rename 's/\.[^.]+$//' {} \;
```

```bash
ls -p | tr ' ' '.'
```

