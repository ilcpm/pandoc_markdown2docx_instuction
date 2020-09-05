local RAW_NEWSECTION = '<w:p/><w:p><w:pPr><w:sectPr></w:sectPr></w:pPr></w:p>'

-- Filter function called on each RawBlock element.
function RawBlock (el)
  if el.text == "\\newsection" then
    if FORMAT == "docx" then
        el.text = RAW_NEWSECTION
        el.format = "openxml"
        return el
    end
  end
end

return {
  {Meta = meta},
  {RawBlock = RawBlock}
}
