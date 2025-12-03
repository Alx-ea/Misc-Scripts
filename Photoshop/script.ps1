$sourcePath = "C:\Users\xxdrk\OneDrive - Circle Sports\product images\dickies\online"
$tempPath = "C:\Users\xxdrk\OneDrive - Circle Sports\product images\dickies\test\removed_bg"

# Create the temporary folder if it doesn't exist
New-Item -ItemType Directory -Force -Path $tempPath

Get-ChildItem -Path $sourcePath\*.jpg, $sourcePath\*.png | ForEach-Object {
    $inputPath = $_.FullName
    $outputPath = Join-Path $tempPath ($_.BaseName + ".png")
    Write-Host "Processing: $inputPath"
    rembg i "$inputPath" "$outputPath"
}

Write-Host "Background removal complete. Files are in: $tempPath"