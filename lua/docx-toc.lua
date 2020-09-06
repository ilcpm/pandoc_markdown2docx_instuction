local RAW_TOC = [[
<w:sdt>
    <w:sdtContent xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
        <w:p>
            <w:pPr>
                <w:pStyle w:val="TOC" />
            </w:pPr>
            <w:r>
                <w:t xml:space="preserve">目录</w:t>
            </w:r>
        </w:p>
        <w:p>
            <w:r>
                <w:fldChar w:fldCharType="begin" w:dirty="true" />
                <w:instrText xml:space="preserve">TOC \o "1-3" \h \z \u</w:instrText>
                <w:fldChar w:fldCharType="separate" />
                <w:fldChar w:fldCharType="end" />
            </w:r>
        </w:p>
    </w:sdtContent>
</w:sdt>
]]

-- Filter function called on each RawBlock element.
function RawBlock (el)
  if el.text == "\\toc" then
    if FORMAT == "docx" then
        el.text = RAW_TOC
        el.format = "openxml"
        return el
    end
  end
end

return {
  {Meta = meta},
  {RawBlock = RawBlock}
}
