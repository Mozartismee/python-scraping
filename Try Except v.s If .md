### This is How if-else work for error detection

```
import os

if os.path.exists("nonexistent_file.txt"):
    f = open("nonexistent_file.txt", "r")
else:
    print("File not found")
```
it takes one-line longer to test the potential mistakes while opening files

### This is How try-except work for error detection

```
try:
    f = open("nonexistent_file.txt", "r")
except FileNotFoundError:
    print("File not found")
```
try-except expression is more consice and more readable when it comes to debuging
