$isOpenDocxAfterComplete = 1

$in = "example.md"
$out = $in.Split('.')[0] + ".docx"
$refer = "reference.docx"
$toc_depth = 3

pandoc.exe `
    $in `
    -o $out `
    --from markdown+startnum+footnotes `
    --toc-depth=$toc_depth `
    --filter pandoc-fignos `
    --filter pandoc-eqnos `
    --filter pandoc-secnos `
    --filter pandoc-citeproc `
    --reference-doc=$refer
    # --include-before-body=$front `

if ($isOpenDocxAfterComplete) {
    Start-Process $out
}
