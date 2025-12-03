// This script exports each top-level layer in a Photoshop document as a separate PNG file with a transparent background,
// using incremental filenames starting from "1.png" upwards.

#target photoshop

function exportLayersAsPNG() {
    if (app.documents.length === 0) {
        alert("Please open a document before running this script.");
        return;
    }

    var doc = app.activeDocument;
    var originalActiveLayer = doc.activeLayer; // Store the originally active layer
    var originalVisibility = []; // Store original visibility of all layers
    var fileCounter = 1;
    var saveFolder;

    // Ask the user to choose a folder to save the PNGs
    try {
        saveFolder = Folder.selectDialog("Select a folder to save the PNG files:");
        if (saveFolder === null) { // User cancelled
            return;
        }
    } catch (e) {
        alert("Error selecting folder: " + e);
        return;
    }

    // Store original visibility of all top-level layers and hide them
    for (var i = 0; i < doc.layers.length; i++) {
        var layer = doc.layers[i];
        originalVisibility[i] = layer.visible;
        layer.visible = false; // Hide all layers initially
    }

    // Iterate through top-level layers
    for (var i = 0; i < doc.layers.length; i++) {
        var layer = doc.layers[i];

        // Skip background layer if it exists
        if (layer.isBackgroundLayer) {
            continue;
        }

        // Make the current layer visible
        layer.visible = true;

        // Set PNG options
        var pngSaveOptions = new PNGSaveOptions();
        pngSaveOptions.interlaced = false; // Set to true if you want interlaced PNGs

        // Construct the filename
        var fileName = fileCounter + ".png";
        var filePath = new File(saveFolder + "/" + fileName);

        try {
            // Save as PNG
            doc.saveAs(filePath, pngSaveOptions, true, Extension.LOWERCASE);
            fileCounter++;
        } catch (e) {
            alert("Error saving layer '" + layer.name + "': " + e);
        }

        // Hide the layer again
        layer.visible = false;
    }

    // Restore original visibility of all layers
    for (var i = 0; i < doc.layers.length; i++) {
        doc.layers[i].visible = originalVisibility[i];
    }
    
    // Restore original active layer
    doc.activeLayer = originalActiveLayer;


    alert("Export complete! " + (fileCounter - 1) + " PNG files were exported to:\n" + saveFolder.fullName);
}

// Run the function
exportLayersAsPNG();