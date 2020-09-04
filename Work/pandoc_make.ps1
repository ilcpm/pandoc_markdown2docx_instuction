$isOpenDocxAfterComplete = 1

$in = "menu.md"
$out = $in.Split('.')[0] + ".docx"
$refer = "menu.docx"
$toc_depth = 3

pandoc.exe `
    $in `
    -o $out `
    --metadata link-citations=true `
    --from markdown+startnum+footnotes `
    --toc-depth=$toc_depth `
    --filter pandoc-citeproc `
    # --reference-doc=$refer
    # --filter pandoc-crossref `
    # --filter pandoc-fignos `
    # --filter pandoc-eqnos `
    # --filter pandoc-secnos `
    # --include-before-body=$front `

if ($isOpenDocxAfterComplete) {
    Start-Process $out
}
