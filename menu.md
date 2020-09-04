---
output:
  word_document:
    # highlight: "tango"
    reference_doc: 'menu - 副本 (2).docx'
# export_on_save:
  # pandoc: true
---

# 使用手册

## 大纲（要写些什么）

* 能不能用这个方案写Word？
  * pandoc能够实现的功能
  * pandoc不能实现但能够使用插件和相关工具完成的功能
* 环境搭建
* markdown语法指导
* 增强语法文档
* 如何转换

## 编号段落

编号段落即以数字开头的`有序列表`（ordered list）和以特殊符号开头的`无序列表`（unordered list）的统称。

### 有序列表

有序列表采用

1. 有序列表1
2. 有序列表2
3. 有序列表3

### 无序列表

* 无序列表1
* 无序列表2
* 无序列表3

### 列表嵌套

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

### 特殊语法

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