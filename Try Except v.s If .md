### This is How if-else work for error detection

```python
import os

if os.path.exists("nonexistent_file.txt"):
    f = open("nonexistent_file.txt", "r")
else:
    print("File not found")
```
it takes one-line longer to test the potential mistakes while opening files

### This is How try-except work for error detection

```python
try:
    f = open("nonexistent_file.txt", "r")
except FileNotFoundError:
    print("File not found")
```
try-except expression is more consice and more readable when it comes to debuging

#### Summary :
try-except expression會自動從 f = open("nonexistent_file.txt", "r")的執行過程中找到錯誤，
並決定要不要進入到except的部分；反之使用if-else，需要用額外的boolean函數來進行條件分支的判斷。
