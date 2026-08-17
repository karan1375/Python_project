import tkinter as tk
from tkinter import filedialog, messagebox 
from pypdf import PdfWriter
import os


def select_pdfs():
    files = filedialog.askopenfilenames(
        title="Select PDF files to merge",
        filetypes=[("PDF files", "*.pdf")] 
        
     )    #filedialog.askopenfilenames() this function open file selection window and 
          # allow user to select multiple files and return the selected file path as a tuple
          # .pdf is the file extension for pdf files and we are using it to filter the files in the file selection window


    if files:
        pdf_list.delete(0, tk.END) #previous selected files will be removed 0 is starting index and tk.END is the last index of the listbox
        for file in files: #
            pdf_list.insert(tk.END, file) #this function is show the selected file in the listbox 
            
        for file in files:
            pdf_list.size(tk.END,file)
            print(f"selected files{file}")


def merge_pdfs():
    pdfs = list(pdf_list.get(0, tk.END))
    if not pdfs:
        messagebox.showerror("Error", "No PDF files selected!")
        return
     #this function is check listbox is empty or not if it is empty then show error message and return form the function

    merger = PdfWriter() #this is the class of pypdf library which is used to merge pdf files and create a new pdf file
    try:
        for pdf in pdfs:
            merger.append(pdf) #add the selected pdf files to the merger object with the help of for loop and loop

        output_file = filedialog.asksaveasfilename( #.asksaveasfilename() this function is open save file dialog  
            defaultextension=".pdf",     #this is the default file extension for the merged pdf file add default extension .pdf            
            filetypes=[("PDF files", "*.pdf")], #[] because filetypes is a list , so its convert tuple to list 
            title="Save merged PDF as" #this is the title of dialog box
        )
        if output_file: #this is check output file name is empty or not if it is empty then do nothing and return form the function 
                        #and if is not empty then save the merged pdf file with the user given name and show success message
            
            merger.write(output_file)# this function is save the merged pdf file with the given name and path  by user 
            merger.close()
            messagebox.showinfo(
                "Success",
                f"PDFs merged successfully into {os.path.basename(output_file)}"
            )
    except Exception as e: # if any error occurs during the merging process then it will store the error in e variable 
        messagebox.showerror("Error", f"An error occurred: {str(e)}") #and show the error message in the messagebox

root = tk.Tk()
root.title("PDF Merger")
root.geometry("400x300")

select_button = tk.Button(root, text="Select PDF Files", command=select_pdfs) 
# command=select_pdfs why not use () this is because we want to pass the function reference to the button and not call the function immediately  
select_button.pack(pady=10)

pdf_list = tk.Listbox(root, selectmode=tk.MULTIPLE, width=50, height=10)
pdf_list.pack(pady=10) 
# this is show the selected pdf files in the listbox 

merge_button = tk.Button(root, text="Merge PDFs", command=merge_pdfs)
merge_button.pack(pady=10)

root.mainloop()