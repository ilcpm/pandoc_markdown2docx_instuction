$isOpenDocxAfterComplete = 1

$in = "test.md"
$out = $in.Split('.')[0] + ".docx"
# $refer = "menu.docx"
$toc_depth = 3

pandoc.exe `
    $in `
    -o $out `
    --from markdown+startnum+footnotes `
    --lua-filter ..\lua\pagebreak.lua `
    --lua-filter ..\lua\docx-toc.lua `
    --lua-filter ..\lua\docx-newsection.lua
    # --toc-depth=$toc_depth `
    # --filter pandoc-citeproc `
    # --metadata link-citations=true `
    # --reference-doc=$refer
    # --filter pandoc-crossref `
    # --filter pandoc-fignos `
    # --filter pandoc-eqnos `
    # --filter pandoc-secnos `
    # --include-before-body=$front `

if ($isOpenDocxAfterComplete) {
    Start-Process $out
}
