# 基于pandoc的`markdown写作Word论文`转换方案

用Word写作论文时，需要不停的调整样式和格式，而插入公式的时候体验也很差。该项目的目的是，基于pandoc工具提供的Markdown转换Word功能，改善Word写作论文的体验。**以重庆大学毕业论文排版作为例子**，试图给出用Markdown写作Word论文的指导方案，并处理该过程中因为Word排版要求复杂带来的各种问题。

大致思路为：

1. 用Markdown实现绝大部分的“后端”写作（即论文输入），提升写作体验
2. 而后在Word中调整样式，做出“前端”的排版效果
3. 用pandoc转换Markdown为docx格式
4. 最后在Word中处理转换过程无法实现的细节（局限性）

**目前仓库刚刚建立，所有文件均为之前测试的文件，杂乱无章，还不具有指导价值，欢迎watch！**
**目前仓库刚刚建立，所有文件均为之前测试的文件，杂乱无章，还不具有指导价值，欢迎watch！**
**目前仓库刚刚建立，所有文件均为之前测试的文件，杂乱无章，还不具有指导价值，欢迎watch！**

运行`pandoc_make.ps1`即可编译`example.md`生成`example.docx`，但需要pandoc和几个pandoc的插件依赖，可以直接对比已经存在的`example.md`和`example.docx`查看直接转换的效果！

**可以直接对比已经存在的`example.md`和`example.docx`查看直接转换的效果！**
**可以直接对比已经存在的`example.md`和`example.docx`查看直接转换的效果！**
**可以直接对比已经存在的`example.md`和`example.docx`查看直接转换的效果！**

## 缘起

TODO

## 优势&局限性

### 优势

* 前后端分离
  * Markdown负责后端内容输入
  * Word负责前端样式
* LaTeX公式输入
* 交叉引用方便（图，表，公式）
* 章节编号在Word样式中自动生成，无需手动调整编号

### 局限性

本例子基于重庆大学的毕业论文排版，在转换过程中发现了很多因为Word排版的复杂要求带来的“麻烦”，整个转换流程大部分的内容都是在处理这些无法自动换行的地方。
另一点是Word样式的复杂性，需要调整大量的样式，但是这些格式调整本来在Word排版中就存在，原本就很麻烦，不算是缺点。

## 我适合使用吗

如果你：

1. 不知道什么是Markdown
2. 对Word排版，尤其是“样式”功能一窍不通甚至没听说过
3. 没听说过LaTeX公式
4. 对命令行操作半点不懂

那么该方案对你没有任何优势，建议先学习Word自动化排版

## TODO

目前仓库刚刚建立，所有文件均为之前测试的文件，还不具有指导价值，欢迎watch

- [ ] 查询如何生成github目录
- [ ] 继续完善Readme
- [ ] 添加参考文档列表
- [ ] 添加感谢列表
- [ ] 添加更细致的说明
