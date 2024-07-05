import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
import webbrowser
import img2pdf
import pdfrw

root = tk.Tk()
root.title("PDF Tools")
root.geometry("640x480")
root.resizable(False, False)
root.config(bg="Grey")

def open_pdf():
    file_path = filedialog.askopenfilename(title="Open PDF File", filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        webbrowser.open(file_path)

def convert_img_to_pdf():
    image_files = filedialog.askopenfilenames(title="Select Image Files", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if image_files:
        pdf_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        if pdf_file:
            with open(pdf_file, "wb") as f:
                f.write(img2pdf.convert(image_files))
            messagebox.showinfo("Conversion Complete", "Images converted to PDF successfully!")

def compress_pdf():
    file_path = filedialog.askopenfilename(title="Open PDF File", filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        compressed_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        if compressed_file:
            # Open the input PDF
            input_pdf = pdfrw.PdfReader(file_path)

            # Create a new PDF writer object
            output_pdf = pdfrw.PdfWriter()

            # Copy all pages to the output PDF writer
            for page in input_pdf.pages:
                output_pdf.addpage(page)

            # Write the compressed PDF to output file
            output_pdf.write(compressed_file)

            messagebox.showinfo("Compression Complete", "PDF compressed successfully!")

# icon image
image_icon = PhotoImage(file="pdfvie.png")
root.iconphoto(False, image_icon)

# Top Frame
Top_frame = Frame(root, bg="White", width=900, height=170)
Top_frame.place(x=0, y=0)

Logo = PhotoImage(file="pdfvie.png")
Label(Top_frame, image=Logo, bg="white").place(x=10, y=5)

Label(Top_frame, text="PDF Tools", font=("Arial", 30, "bold"), bg="white", fg="black").place(x=290, y=70)

# Buttons
btn_view = Button(root, text="View PDF", compound=LEFT, width=14, font=("Arial", 14, "bold"), command=open_pdf)
btn_view.place(x=240, y=200)

btn_convert = Button(root, text="Img to PDF", compound=LEFT, width=14, font=("Arial", 14, "bold"), command=convert_img_to_pdf)
btn_convert.place(x=240, y=270)

btn_compress = Button(root, text="Compress PDF", compound=LEFT, width=14, font=("Arial", 14, "bold"), command=compress_pdf)
btn_compress.place(x=240, y=340)

root.mainloop()
