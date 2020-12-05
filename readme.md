# 基于pandoc的markdown转Word论文写作方案

用Word写作论文时，需要不停的调整样式和格式，而插入公式的时候体验也很差。该项目的目的是，基于pandoc工具提供的Markdown转换Word功能，改善Word写作论文的体验。**以重庆大学毕业论文排版作为例子**，试图给出用Markdown写作Word论文的指导方案，处理该过程中因为Word排版要求复杂带来的各种问题，并尽可能自动化完成排版过程。

大致思路为：

1. 用Markdown实现绝大部分的“后端”写作（即论文输入），提升写作体验
2. 在Word中调整样式，做出预设的“前端”的排版效果，将该文件作为模版
3. 以上述文档为模版，用pandoc转换Markdown为docx格式
   * 转换过程中借助**自行编写的pandoc插件**实现大部分原来pandoc转换markdown无法实现的内容
4. 最后在Word中处理转换过程无法实现的细节（局限性）
   * 考虑制作另一简单工具处理最后的细节（目前只发现页眉页脚需要处理）

**目前仓库建立不久，各方面还不完善，大部分文件均未完成，不具有太大的指导价值，欢迎watch**

~~运行`pandoc_make.ps1`即可编译`example.md`生成`example.docx`，但需要pandoc和几个pandoc的插件依赖，可以直接对比已经存在的`example.md`和`example.docx`查看直接转换的效果！~~

**可以直接对比已经存在的`menu.md`和`menu.docx`，以及`/Work/example.md`和`/Work/example.docx`查看直接转换的效果！**

**2020.11.19，手动实现了对公式编号和引用的原生实现，对比`/功能验证/test_raw.txt`和`/功能验证/test_raw.docx`查看效果**

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [基于pandoc的markdown转Word论文写作方案](#基于pandoc的markdown转word论文写作方案)
  - [缘起](#缘起)
  - [文件介绍](#文件介绍)
  - [优势&局限性](#优势局限性)
    - [优势](#优势)
    - [局限性](#局限性)
  - [我适合使用吗](#我适合使用吗)
  - [环境搭建（依赖）](#环境搭建依赖)
    - [必备的转换工具](#必备的转换工具)
    - [建议的写作环境](#建议的写作环境)
  - [工作流时间表](#工作流时间表)
  - [参考文献](#参考文献)
  - [进展](#进展)
  - [TODO](#todo)

<!-- /code_chunk_output -->

## 缘起

重庆大学未提供毕业论文的LaTeX模版，且LaTeX学习成本较高，如需自行调整格式难度较大。且LaTeX排版论文存在被刁难的风险以及抽检查重时需要提交Word版本，故还是Word写论文比较保险。可偏偏Word又不甚好用。

另一方面个人对markdown甚是喜欢，也希望能够让markdown完成写论文的“出圈”之路，遂展开研究。

该项目同时申请了2020年重庆市的市级创新实践项目，具体实施期限约为2020年6月~2021年6月

详细项目介绍见[项目介绍.md](开题答辩/项目介绍.md)

## 文件介绍

```text
./
│   menu.md                                   手册markdown文件
│   menu.docx                                 转换后的手册Word文件
│   pandoc_MANUAL.pdf                         pandoc官网的PDF手册
│   readme.md                                 Readme
│   reference2.docx                           测试用的Word模版文件
│   Reference_md.docx                         生成手册使用的模版文件
│
├───Work                                      工作汇总文件夹，合并研究成功，目前为草稿
│
├───功能验证                                  工作文件夹，各种测试预研
│       ThinsToDo.md                          整个流程要处理的事情
│       ooxml.md                              转换为Word所需的Word ooxml代码
│
└───开题答辩                                  开题答辩相关文件，含项目介绍
        项目介绍.md                           为开题答辩准备的项目介绍
```

## 优势&局限性

### 优势

* 前后端分离
  * Markdown负责后端内容输入
  * Word负责前端样式
* LaTeX公式输入
* 交叉引用方便（图，表，公式）
* 超级方便的参考文献引用
* 章节编号在Word样式中自动生成，无需手动调整编号

### 局限性

~~本例子基于重庆大学的毕业论文排版，在转换过程中发现了很多因为Word排版的复杂要求带来的“麻烦”，整个转换流程大部分的内容都是在处理这些无法自动换行的地方。~~

~~另一点是Word样式的复杂性，需要调整大量的样式，但是这些格式调整本来在Word排版中就存在，原本就很麻烦，不算是缺点。~~

完成插件编写后能解决几乎所有的问题

## 我适合使用吗

如果你：

1. 不知道什么是Markdown
2. 对Word排版，尤其是“样式”功能一窍不通甚至没听说过
3. 没听说过LaTeX公式
4. 对命令行操作半点不懂

那么该方案对你没有任何优势，建议先学习Word排版

## 环境搭建（依赖）

### 必备的转换工具

* pandoc
* python编写的pandoc插件*n

TODO

### 建议的写作环境

* VS Code
  * MPE
    * 设置为pandoc模式
  * pandoc citer
  * markdown写作插件若干
    * Markdownlint：语法检查
    * markdown all in one：语法高亮
    * markdown shortcut：快捷键支持

TODO

## 工作流时间表

* 2020年11月底，通过直接在Markdown中插入ooxml代码的方式实现对交叉引用，公式编号等内容的实现，即实现“所有功能手动实现，只需要编程把这个过程自动化即可”的目标，完成中期答辩
* 2021年1至2月寒假，编程工作预研，学习python库和项目的编写，阅读lua-filter代码，研究pandoc`类`
* 2021年1至2月寒假，主要的编程工作，编写python插件库，实现自动化
* 2021年2至6月，完成各种测试，完善功能，修复bug，在17级毕业时寻找志愿者利用该方案排版Word论文，寻找问题并进行调试
* 2021年2至6月，逐步完成文档撰写

## 参考文献

* 王树义：[如何用Markdown写论文？](https://www.jianshu.com/p/b0ac7ae98100)
* pandoc文档：[https://pandoc.org/MANUAL.html](https://pandoc.org/MANUAL.html)
* pandoc核心数据结构：[pandoc filter](https://pandoc.org/filters.html)
* pandoc插件作者：[\@tomduck](https://github.com/tomduck?tab=repositories)
* pandoc-lua-filter：[pandocker-lua-filters](https://github.com/pandocker/pandocker-lua-filters)
* Word ooxml文档：[API 参考 | Microsoft Docs](https://docs.microsoft.com/zh-cn/dotnet/api/overview/openxml/?view=openxml-2.8.1)

## 进展

* ~~2020.11.19：解构了pandoc的数据结构，通过直接修改`native`代码完成了对**公式编号**和**交叉引用**的原生实现，只需要编程实现即可~~（搞错了）
* 2020.12.03：发现南京大学的毕业论文pandoc实现，所有技术细节几乎都有解决方案
* 2020.12.05：借助python的`panflute`库测试性编写python扩展，对LaTeX形式的自定义语法实现功能替换，实现了之前找到的ooxml代码的替换；细化重庆大学本科毕业论文排版要求细节，准备制作模版试探性排版

## TODO

- [ ] 持续完善Readme
- [ ] 添加更细致的说明
- [ ] 添加感谢列表
- [x] 添加参考文献列表
- [x] 查询如何生成github目录
