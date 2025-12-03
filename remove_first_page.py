import os
from PyPDF2 import PdfReader, PdfWriter
import glob

# --- Configuration ---
# 1. Directory where your 100 original PDFs are located
# YOU MUST UPDATE THESE PATHS!
INPUT_DIR = "C:/Users/xxdrk/OneDrive/Documents/Notes/Islamic/Islamic/00_Qur'ran" 

# 2. Directory where you want to save the modified PDFs
# YOU MUST UPDATE THESE PATHS!
OUTPUT_DIR = "C:/Users/xxdrk/Desktop/Pythonscripts/test"

# Create the output directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)
# ---------------------

print(f"Starting to process PDFs in: {INPUT_DIR}")

# Use glob to find all files ending with .pdf in the input directory
pdf_files = glob.glob(os.path.join(INPUT_DIR, '*.pdf'))

if not pdf_files:
    print("No PDF files found. Check your INPUT_DIR path.")
else:
    print(f"Found {len(pdf_files)} PDF files to process.")
    
    for filename in pdf_files:
        try:
            # 1. Open the original PDF
            input_file_handle = open(filename, 'rb')
            reader = PdfReader(input_file_handle)
            writer = PdfWriter()
            
            # Get the base filename (e.g., "document1.pdf")
            base_filename = os.path.basename(filename)
            
            # Check if the PDF has more than 1 page
            if len(reader.pages) > 1:
                # 2. Iterate through all pages starting from the *second* page (index 1)
                # This effectively skips the first page (index 0)
                for i in range(1, len(reader.pages)):
                    page = reader.pages[i]
                    writer.add_page(page)
                
                # 3. Define the path for the new output file
                output_filepath = os.path.join(OUTPUT_DIR, base_filename)
                
                # 4. Write the new PDF to the output directory
                with open(output_filepath, 'wb') as output_file_handle:
                    writer.write(output_file_handle)
                    
                print(f"✅ Processed and saved: {base_filename}")
            else:
                print(f"⚠️ Skipped: {base_filename} (Only has 1 page or less).")

        except Exception as e:
            print(f"❌ Error processing {os.path.basename(filename)}: {e}")
        finally:
            # Important: Close the input file handle to free up resources
            if 'input_file_handle' in locals() and not input_file_handle.closed:
                input_file_handle.close()

    print("\nProcessing complete.")
