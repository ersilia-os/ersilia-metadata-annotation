import marker
import os

def convert_pdf_to_text(pdf_path, output_path=None):
    # Check if the PDF file exists
    if not os.path.isfile(pdf_path):
        raise FileNotFoundError(f"PDF file not found at: {pdf_path}")
    
    try:
        # Create a PDF document object
        doc = marker.Document(pdf_path)
        
        # Extract the text content from the PDF
        # By default, marker extracts text only (not images or tables)
        text_content = ""
        
        # Process each page
        for page in doc.pages():
            # Extract text from the page
            text_content += page.get_text()
            # Add a page separator 
            text_content += "\n\n----- Page Break -----\n\n"
        
        # Save the text content to a file if output_path is provided
        if output_path:
            with open(output_path, "w", encoding="utf-8") as text_file:
                text_file.write(text_content)
            print(f"Text successfully saved to: {output_path}")
        
        return text_content
    
    except Exception as e:
        raise Exception(f"Error converting PDF to text: {str(e)}")