## find_all() 函數簡介：

find_all函數是Beautiful Soup中用於查找匹配條件的HTML或XML元素的主要方法。其參數如下：

1. name： 可以是字符串、正則表達式或者函數等對象。此參數用於指定查找的標籤名稱。例如：將其設置為'div'以查找所有<div>標籤。

2. attrs： 一個字典，用於指定標籤的屬性名和屬性值。例如：將其設置為{'class': 'myclass'}以查找帶有'class'屬性值為'myclass'的所有標籤。

3. recursive： 布爾值。此參數表示是否搜索子孫節點。默認為True，代表在該元素及其子節點中搜索符合條件的元素；如果設置為False，則僅搜索指定節點的直接子節點。

4. text： 可以是字符串、正則表達式或者函數等對象。用於查找帶有匹配文本內容的標籤。例如：將其設置為'the prince'以查找包含文本內容為'the prince'的標籤元素。

5. limit： 一個整數，用於限制返回的結果數量。例如：將其設置為10來返回最多10個匹配的元素（如果有的話）。

6. kwargs： 其他關鍵字參數，用於指定查找元素的標籤屬性。例如：將find_all(id='my_id', class_='my_class')設置為查找具有指定'id'和'class'屬性值的標籤。

find_all函數可以根據您指定的匹配條件來搜索標籤和屬性，它會返回一個列表，包含所有符合條件的元素。
 
---

範例：

```python
  from bs4 import BeautifulSoup
import re

html = """
<html><head><title>My Web Page</title></head>
<body>
<p class="content" article-number="101">Article 1 - Lorem ipsum</p>
<p class="content" article-number="102">Article 2 - Lorem ipsum</p>
<p class="content" article-number="103">Article 3 - Lorem ipsum</p>
<p class="content" article-number="104">Article 4 - Lorem ipsum</p>
<span class="content" article-number="105">Not a Paragraph - Lorem ipsum</span>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')

# Create a function that filters the elements by content.
def filter_function(text):
    return 'Article 1 -' in text

# Use find_all() with all possible parameters.
result = soup.find_all(
    name='p',  # Include the <p> tags.
    attrs={'class': 'content', 'article-number': re.compile(r'\d{3}')},  # Require the class "content" and a 3-digit article-number attribute.
    recursive=True,  # Search this tag and all its children.
    text=filter_function,  # Only treat elements whose text include 'Article 1 -'.
    limit=2  # Limit the number of results.
)

# Output the results.
for item in result:
    print(item)
  
```
  
這個示例將返回：

 ```htmnl
<p article-number="101" class="content">Article 1 - Lorem ipsum</p>
 ```
  
在這個示例中，我們使用了名為filter_function的過濾函數，以更進一步篩選要查找的元素。find_all()方法是根據設定的name、attrs、recursive、text和limit參數來查找匹配條件的元素。對於實際應用，您可能不需要在一個查詢中使用所有參數。通常，根據需求組合使用幾個參數即可滿足大多數情況。
  
---
**若只要內文，可以使用get_text()**
 
  ```python
  for item in result:
    print(item.get_text())
  ```
  
 輸出結果為：
  
  ```html
  Paragraph
  ```
 
 
 ## Reference
 ---
 - https://www.crummy.com/software/BeautifulSoup/bs4/doc/#searching-the-tree
