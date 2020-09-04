# OOXML代码

## 分节符

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

```{=openxml}
<w:p>
  <w:r>
    <w:br w:type="page"/>
  </w:r>
</w:p>
```

## 特殊制表符

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
