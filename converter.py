import sys
import os
import fitz  # PyMuPDF
import subprocess

class NullWriter:
    def write(self, arg): pass
    def flush(self): pass

sys.stdout = NullWriter()
sys.stderr = NullWriter()
# ---------------------------------------------

def ask_file_mac():
    try:
        script = """
        set theFile to POSIX path of (choose file with prompt "Select a PDF to convert:" of type {"pdf"})
        return theFile
        """
        return subprocess.check_output(['osascript', '-e', script]).decode('utf-8').strip()
    except:
        return None

def ask_folder_mac():
    try:
        script = """
        set theFolder to POSIX path of (choose folder with prompt "Where to save images?")
        return theFolder
        """
        return subprocess.check_output(['osascript', '-e', script]).decode('utf-8').strip()
    except:
        return None

def notify(title, text):
    safe_text = text.replace('"', '\\"')
    safe_title = title.replace('"', '\\"')
    os.system(f"""osascript -e 'display notification "{safe_text}" with title "{safe_title}"'""")

def convert_pdf_to_images(input_pdf_path, output_root_folder):
    try:
        pdf_name = os.path.basename(input_pdf_path).replace('.pdf', '')
        final_output_folder = os.path.join(output_root_folder, pdf_name)
        
        if not os.path.exists(final_output_folder):
            os.makedirs(final_output_folder)

        doc = fitz.open(input_pdf_path)
        
        notify("Started", f"Converting {len(doc)} pages...")

        for page_num in range(len(doc)):
            page = doc[page_num]
            mat = fitz.Matrix(2.0, 2.0)
            pix = page.get_pixmap(matrix=mat)
            output_image = os.path.join(final_output_folder, f"{pdf_name}_page{page_num+1}.png")
            pix.save(output_image)

        doc.close()
        
        notify("Success!", f"Saved in folder: {pdf_name}")
        
        os.system(f"open '{final_output_folder}'")

    except Exception as e:
        notify("Error", f"Failed: {str(e)}")

if __name__ == "__main__":
    selected_pdf = ask_file_mac()
    if selected_pdf:
        destination_folder = ask_folder_mac()
        if destination_folder:

            convert_pdf_to_images(selected_pdf, destination_folder)
