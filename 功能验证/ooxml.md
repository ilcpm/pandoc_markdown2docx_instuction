# OOXML代码&特殊语法

- [OOXML代码&特殊语法](#ooxml代码特殊语法)
  - [分节符](#分节符)
  - [分页符](#分页符)
  - [普通制表符](#普通制表符)
  - [特殊制表符](#特殊制表符)
  - [域代码插入](#域代码插入)
    - [去掉该部分拼写检查](#去掉该部分拼写检查)
    - [复杂域代码](#复杂域代码)
    - [简单域代码](#简单域代码)
    - [题注域代码](#题注域代码)
  - [书签](#书签)
    - [书签开始](#书签开始)
    - [书签结束](#书签结束)
    - [书签引用域代码](#书签引用域代码)
  - [自定义样式](#自定义样式)

## 分节符

单独成段

```{=openxml}
<w:p/>
<w:p>
    <w:pPr>
        <w:sectPr>
        </w:sectPr>
    </w:pPr>
</w:p>
```

## 分页符

单独成段

```{=openxml}
<w:p>
  <w:r>
    <w:br w:type="page"/>
  </w:r>
</w:p>
```

## 普通制表符

插入在`<w:p>  </w:p>`标签内

```{=openxml}
<w:r>
    <w:tab/>
</w:r>
```

## 特殊制表符

插入在`<w:p>  </w:p>`标签内

* 左

  ```{=openxml}
  <w:r>
      <w:ptab w:relativeTo="margin" w:alignment="left" w:leader="none"/>
  </w:r>
  ```

* 中

  ```{=openxml}
  <w:r>
      <w:ptab w:relativeTo="margin" w:alignment="center" w:leader="none"/>
  </w:r>
  ```

* 右

  ```{=openxml}
  <w:r>
      <w:ptab w:relativeTo="margin" w:alignment="right" w:leader="none"/>
  </w:r>
  ```

## 域代码插入

### 去掉该部分拼写检查

```
<w:rPr>
    <w:noProof/>
</w:rPr>
```

### 复杂域代码

```{=openxml}
<w:p>
    <w:r>
        <w:fldChar w:fldCharType="begin"/>
    </w:r>
    <w:r>
        <w:instrText>TOC \o "1-3" \h \z \u</w:instrText>
    </w:r>
    <w:r>
        <w:fldChar w:fldCharType="end"/>
    </w:r>
</w:p>
```

### 简单域代码

```
<w:fldSimple w:instr=" STYLEREF 1 \s ">
    <w:r>
        <w:rPr>
            <w:noProof/>
        </w:rPr>
        <w:t>0</w:t>
    </w:r>
</w:fldSimple>
```

```
<w:fldSimple w:instr=" SEQ Figure \* ARABIC \s 1 ">
    <w:r>
        <w:rPr>
            <w:noProof/>
        </w:rPr>
        <w:t>1</w:t>
    </w:r>
</w:fldSimple>
```

### 题注域代码

章节-编号

```
<w:p>
    <w:pPr>
        <w:pStyle w:val="aa"/>
    </w:pPr>
    <w:r>
        <w:t xml:space="preserve">题注前缀 </w:t>
    </w:r>
    <w:fldSimple w:instr=" STYLEREF 1 \s ">
        <w:r>
            <w:rPr>
                <w:noProof/>
            </w:rPr>
            <w:t>0</w:t>
        </w:r>
    </w:fldSimple>
    <w:r>
        <w:noBreakHyphen/>
    </w:r>
    <w:fldSimple w:instr=" SEQ Figure \* ARABIC \s 1 ">
        <w:r>
            <w:rPr>
                <w:noProof/>
            </w:rPr>
            <w:t>1</w:t>
        </w:r>
    </w:fldSimple>
    <w:r>
        <w:t>题注内容</w:t>
    </w:r>
</w:p>
```

## 书签

### 书签开始

```{=openxml}
<w:bookmarkStart w:id="20" w:name="name" />
```

### 书签结束

```{=openxml}
<w:bookmarkEnd w:id="20" />
```

### 书签引用域代码

* 引用文本

  ```{=openxml}
  REF name \h 
  ```

* 引用页码

  ```{=openxml}
  PAGEREF name \h
  ```

## 自定义样式

::: {custom-style="Poetry"}
| A Bird came down the Walk---
| He did not know I saw---
:::
