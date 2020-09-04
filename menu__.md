---
output:
    word_document: {highlight: tango, reference_doc: 'menu - 副本 (2).docx'}
---  
  
  
  
#   使用手册123345 {#使用手册123345 }
 {#使用手册123345 }
  
##   编号段落 {#编号段落 }
 {#编号段落 }
  
编号段落即以数字开头的`有序列表`（ordered list）和以特殊符号开头的`无序列表`（unordered list）的统称。
  
###   有序列表 {#有序列表 }
 {#有序列表 }
  
有序列表采用
  
1. 有序列表1
2. 有序列表2
3. 有序列表3
  
###   无序列表 {#无序列表 }
 {#无序列表 }
  
* 无序列表1
* 无序列表2
* 无序列表3
  
###   列表嵌套 {#列表嵌套 }
 {#列表嵌套 }
  
有序列表和无序列表可以通过缩进进行嵌套，嵌套的时候每一层使用的符号默认都不相同。
  
* 无序列表1
  * 嵌套无序列表1
    1. 嵌套有序列表1
       * 嵌套无序列表1
       * 嵌套无序列表2
       * 嵌套无序列表3
    2. 嵌套有序列表2
    3. 嵌套有序列表3
  * 嵌套无序列表2
  * 嵌套无序列表3
* 无序列表2
  1. 嵌套有序列表1
  2. 嵌套有序列表2
  3. 嵌套有序列表3
* 无序列表3
  
代码如下：
  
```markdown
* 无序列表1
  * 嵌套无序列表1
    1. 嵌套有序列表1
       * 嵌套无序列表1
       * 嵌套无序列表2
       * 嵌套无序列表3
    2. 嵌套有序列表2
    3. 嵌套有序列表3
  * 嵌套无序列表2
  * 嵌套无序列表3
* 无序列表2
  1. 嵌套有序列表1
  2. 嵌套有序列表2
  3. 嵌套有序列表3
* 无序列表3
```
  
可以发现，缩进有的时候是3个空格，有的时候是2个空格，总的嵌套缩进的原则是，下一层列表的第一个字符对齐上一层列表的正文第一个字符。
  
直观理解就是
  
* 如果上一层是无序列表，那么无序列表的前缀`*`以及空格占2个字符的位置，所以下一层应该缩进2个空格
* 如果上一层是有序列表，那么有序列表的前缀`1.`以及空格占3个字符的位置，所以下一层应该缩进3个空格
  
总之看着右边的预览和`markdownlint`扩展提供的语法检查就可以了。
  
###   特殊语法 {#特殊语法 }
 {#特殊语法 }
  
* 有时候我们需要对首行进行编号
  
  而后面跟上的几行不编号
  
  比如在第一行说明分类讨论是讨论的哪种情况，而在后面的段落论证这个情况
  
  1. 还可能在这几个段落中再分类
  
     再讨论
  
  * 再分类
  
    再讨论
  
* 然后再继续编号
  
要实现上述的功能，只需要在不编号的段落前面插入“和前缀及空格等距”的空格即可，缩进空格的数量和列表嵌套的规则一样；需要注意的是，不编号的段落由于不是列表，所以需要空行隔开。代码如下：
  
```markdown
* 有时候我们需要对首行进行编号
  
  而后面跟上的几行不编号
  
  比如在第一行说明分类讨论是讨论的哪种情况，而在后面的段落论证这个情况
  
  1. 还可能在这几个段落中再分类
  
     再讨论
  
  * 再分类
  
    再讨论
  
* 然后再继续编号
```
  
来段python代码试试
  
  
```python
print()
if xxx:
    for i in range(10):
        pass
    pass
```
  
<div class="pagebreak"> </div>
  
<div class="pagebreak"> </div>
  
  
```py
import numpy
from matplotlib import pyplot as plt
  
class test(numpy):
    def __init__(self):
        super().__init__()
        pass
  
    @classmethod
    async def funcname(parameter_list):
        pass
  
    @property
    def funcname(self, parameter_list):
        pass
  
if __name__ == "__main__":
    for i in range(10):
        try:
            pass
        except expression as identifier:
            pass
        else:
            pass
        finally:
            pass
  
    dic = {"12": 123}
    lst = [dic]
    plt.figure.make_active(dic)
    x = [0 if 0 > 1 else 12]
  
```  
  
123
  
```latex
% Please add the following required packages to your document preamble:
\documentclass{article}
\usepackage{multirow}
\usepackage[active,tightpage]{preview}
\PreviewEnvironment{tabular}
\begin{document}
\begin{table}[]
\begin{tabular}{|l|l|c|l|}
\hline
1 & 1                                       & \multicolumn{1}{l|}{2}        & 3       \\ \hline
2 & 4                                       & \multicolumn{2}{c|}{6}                  \\ \hline
8 & \multicolumn{1}{c|}{\multirow{2}{*}{7}} & \multicolumn{2}{c|}{\multirow{2}{*}{5}} \\ \cline{1-1}
9 & \multicolumn{1}{c|}{}                   & \multicolumn{2}{c|}{}                   \\ \hline
\end{tabular}
\end{table}
\end{document}
```
![](../assets/6c8aa6682df6ba45e21ea5956bd97926_1.svg?0.6875492434757553)

  