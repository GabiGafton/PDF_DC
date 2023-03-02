import PyPDF2
from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF
from PyPDF2 import PdfReader, PdfWriter
from tkinter import *
from tkinter import ttk, filedialog
import os
import datetime

date = (datetime.datetime.now().strftime("%d.%m.%Y"))

myWindow = Tk()
myWindow.title("Add stamp")
myWindow.geometry("510x400")

file_name = ""


def input_file(user_input):
    #get the text that needs to be added to the stamp
    text_entry = entry.get()
    print(text_entry)

    # opens the document
    file_input = open(user_input, "rb")
    box = PdfReader(file_input).pages[0].mediabox
    print(box[2], box[3])

    # handles 2 sizes of documents: A4 and letter
    if box[2] < 596:
        if type_of_document_value.get() == 1:
            insert_text = "Nr. intrare DC: "
            print("Documentul este A4, tipul este INTRARE")
            if placement_var.get() == 1:
                d = Drawing(595.276, 841.89)
                d.add(Rect(2, 820, 126, 20, fill=0, stroke=1, strokeColor=colors.red, fillColor=colors.white))
                d.add(String(5, 827, insert_text + text_entry + "/" + date, fontSize=9, stroke=1, fillColor=colors.red))
            elif placement_var.get() == 2:
                d = Drawing(595.276, 841.89)
                d.add(Rect(466, 820, 126, 20, fill=0, stroke=1, strokeColor=colors.red, fillColor=colors.white))
                d.add(String(468, 827, insert_text + text_entry + "/" + date, fontSize=9, stroke=1, fillColor=colors.red))
            elif placement_var.get() == 3:
                d = Drawing(595.276, 841.89)
                d.add(Rect(2, 2, 126, 20, fill=0, stroke=1, strokeColor=colors.red, fillColor=colors.white))
                d.add(String(5, 8, insert_text + text_entry + "/" + date, fontSize=9, stroke=1, fillColor=colors.red))
            elif placement_var.get() == 4:
                d = Drawing(595.276, 841.89)
                d.add(Rect(466, 2, 126, 20, fill=0, stroke=1, strokeColor=colors.red, fillColor=colors.white))
                d.add(String(468, 8, insert_text + text_entry + "/" + date, fontSize=9, stroke=1, fillColor=colors.red))
        if type_of_document_value.get() == 2:
            insert_text = "Nr. iesire DC: "
            print("Documentul este A4, tipul este IESIRE")
            if placement_var.get() == 1:
                d = Drawing(595.276, 841.89)
                d.add(Rect(2, 820, 126, 20, fill=0, stroke=1, strokeColor=colors.red, fillColor=colors.white))
                d.add(String(5, 827, insert_text + text_entry + "/" + date, fontSize=9, stroke=1, fillColor=colors.red))
            elif placement_var.get() == 2:
                d = Drawing(595.276, 841.89)
                d.add(Rect(466, 820, 126, 20, fill=0, stroke=1, strokeColor=colors.red, fillColor=colors.white))
                d.add(String(468, 827, insert_text + text_entry + "/" + date, fontSize=9, stroke=1, fillColor=colors.red))
            elif placement_var.get() == 3:
                d = Drawing(595.276, 841.89)
                d.add(Rect(2, 2, 126, 20, fill=0, stroke=1, strokeColor=colors.red, fillColor=colors.white))
                d.add(String(5, 8, insert_text + text_entry + "/" + date, fontSize=9, stroke=1, fillColor=colors.red))
            elif placement_var.get() == 4:
                d = Drawing(595.276, 841.89)
                d.add(Rect(466, 2, 126, 20, fill=0, stroke=1, strokeColor=colors.red, fillColor=colors.white))
                d.add(String(468, 8, insert_text + text_entry + "/" + date, fontSize=9, stroke=1, fillColor=colors.red))

    else:
        if type_of_document_value.get() == 1:
            insert_text = "Nr. intrare DC: "
            print("Documentul este letter, tipul este INTRARE")
            if placement_var.get() == 1:
                d = Drawing(612, 793)
                print("Documentul este Letter")
                d.add(Rect(2, 770, 126, 20, fill=0, stroke=1, strokeColor=colors.red, fillColor=colors.white))
                d.add(String(5, 777, insert_text + text_entry + "/" + date, fontSize=9, stroke=1, fillColor=colors.red))
            elif placement_var.get() == 2:
                d = Drawing(612, 793)
                print("Documentul este Letter")
                d.add(Rect(484, 770, 126, 20, fill=0, stroke=1, strokeColor=colors.red, fillColor=colors.white))
                d.add(String(486, 777, insert_text + text_entry + "/" + date, fontSize=9, stroke=1, fillColor=colors.red))
            elif placement_var.get() == 3:
                d = Drawing(612, 792)
                print("Documentul este Letter")
                d.add(Rect(2, 2, 126, 20, fill=0, stroke=1, strokeColor=colors.red, fillColor=colors.white))
                d.add(String(5, 8, insert_text + text_entry + "/" + date, fontSize=9, stroke=1, fillColor=colors.red))
            elif placement_var.get() == 4:
                d = Drawing(612, 792)
                print("Documentul este Letter")
                d.add(Rect(484, 2, 126, 20, fill=0, stroke=1, strokeColor=colors.red, fillColor=colors.white))
                d.add(String(486, 8, insert_text + text_entry + "/" + date, fontSize=9, stroke=1, fillColor=colors.red))
        elif type_of_document_value.get() == 2:
            insert_text = "Nr. iesire DC: "
            print("Documentul este letter, tipul este IESIRE")
            if placement_var.get() == 1:
                d = Drawing(612, 793)
                print("Documentul este Letter")
                d.add(Rect(2, 770, 126, 20, fill=0, stroke=1, strokeColor=colors.red, fillColor=colors.white))
                d.add(String(5, 777, insert_text + text_entry + "/" + date, fontSize=9, stroke=1, fillColor=colors.red))
            elif placement_var.get() == 2:
                d = Drawing(612, 793)
                print("Documentul este Letter")
                d.add(Rect(484, 770, 126, 20, fill=0, stroke=1, strokeColor=colors.red, fillColor=colors.white))
                d.add(
                    String(486, 777, insert_text + text_entry + "/" + date, fontSize=9, stroke=1, fillColor=colors.red))
            elif placement_var.get() == 3:
                d = Drawing(612, 792)
                print("Documentul este Letter")
                d.add(Rect(2, 2, 126, 20, fill=0, stroke=1, strokeColor=colors.red, fillColor=colors.white))
                d.add(String(5, 8, insert_text + text_entry + "/" + date, fontSize=9, stroke=1, fillColor=colors.red))
            elif placement_var.get() == 4:
                d = Drawing(612, 792)
                print("Documentul este Letter")
                d.add(Rect(484, 2, 126, 20, fill=0, stroke=1, strokeColor=colors.red, fillColor=colors.white))
                d.add(String(486, 8, insert_text + text_entry + "/" + date, fontSize=9, stroke=1, fillColor=colors.red))



    # saves a temp document which contains the stamp to be added
    with open(os.getcwd() + "watermark.pdf", "wb") as temp_file:
        renderPDF.drawToFile(d, temp_file)

    # opens the temporary stamp file
    watermark_file = open(os.getcwd() + "watermark.pdf", "rb")
    watermark = PyPDF2.PdfReader(watermark_file)

    # opens the pdf file
    pdf = PyPDF2.PdfReader(file_input)

    first_page = pdf.pages[0]
    first_page_watermark = watermark.pages[0]
    first_page.merge_page(first_page_watermark)

    pdf_writer = PyPDF2.PdfWriter()
    pdf_writer.add_page(first_page)

    #closes the temporary file
    watermark_file.close()

    # writes the output file
    with open(user_input.rsplit(".pdf")[0] + "_stamped.pdf", "wb") as output:
        pdf_writer.write(output)

    # deletes the temporary stamp file
    if os.path.exists(os.getcwd() + "watermark.pdf"):
        os.remove(os.getcwd() + "watermark.pdf")

    # updates the label with the directory name in which the file was saved
    posOfLastSlash = user_input.rindex("/")
    path = user_input[0:posOfLastSlash]
    pathLabel.config(text='The file was saved to the following folder: ' + '\n' + path)
    file_input.close()
    reset_function()


def browseFunc():
    global file_name
    file_name = filedialog.askopenfilename(filetypes = (("Adobe Acrobat'", "*.pdf"), ("All files", "*.*")))
    print(file_name)
    return file_name


def submit_function():
    input_file(file_name)


def reset_function():
    for widget in myWindow.winfo_children():
        if isinstance(widget, Entry):
            widget.delete(0, "end")
        if isinstance(widget, Radiobutton):
            placement_var.set(None)
            type_of_document_value.set(None)


selectLabel = Label(myWindow)
selectLabel.config(text="Select the PDF file")
selectLabel.place(x=210, y=10)

browsebutton = Button(myWindow, padx=20, pady=0 ,text="Browse", command= browseFunc)
browsebutton.place(x=210, y=35)

sep_1 = ttk.Separator(myWindow, orient='horizontal')
sep_1.place(x=0, y=73, relwidth=1)

label = Label(text="Enter text:")
label.place(x=70, y=85)

entry = Entry()
entry.place(x=70, y=112)

selectLabel = Label(myWindow)
selectLabel.config(text="Document type")
selectLabel.place(x=300, y=85)

type_of_document_value = IntVar()
in_option = Radiobutton(myWindow, text="IN", variable=type_of_document_value, value=1)
in_option.place(x=300, y=110)
out_option = Radiobutton(myWindow, text="OUT", variable=type_of_document_value, value=2)
out_option.place(x=340, y=110)

sep_2 = ttk.Separator(myWindow, orient='horizontal')
sep_2.place(x=0, y=150, relwidth=1)

label_2 = Label(text="Select text placement")
label_2.place(x=190, y=155)

placement_var = IntVar()
top_left_option = Radiobutton(myWindow, text="", variable=placement_var, value=1)
top_left_option.place(x=200, y=190)
top_left_label = Label(text="Top left")
top_left_label.place(x=153, y=190)

top_right_option = Radiobutton(myWindow, text="", variable=placement_var, value=2)
top_right_option.place(x=280, y=190)
top_right_label = Label(text="Top right")
top_right_label.place(x=300, y=190)

bottom_left_option = Radiobutton(myWindow, text="", variable=placement_var, value=3)
bottom_left_option.place(x=200, y=260)
bottom_left_label = Label(text="Bottom left")
bottom_left_label.place(x=133, y=260)

bottom_right_option = Radiobutton(myWindow, text="", variable=placement_var, value=4)
bottom_right_option.place(x=280, y=260)
bottom_right_label = Label(text="Bottom right")
bottom_right_label.place(x=300, y=260)

canvas = Canvas(myWindow, height=70, width=50, bg="#f7f7f7")
canvas.place(x=222, y=200)
canvas.create_rectangle(2,2,50,68)

# canvas.create_oval(4,4,10,10, outline="", fill="black")
# canvas.create_oval(4,60,10,66, outline="", fill="black")
# canvas.create_oval(42,4,48,10, outline="", fill="black")
# canvas.create_oval(42,60,48,66, outline="", fill="black")

sep_3 = ttk.Separator(myWindow, orient='horizontal')
sep_3.place(x=0, y=290, relwidth=1)

button_submit = Button(myWindow, text ="CREATE PDF", command=submit_function)
button_submit.config(width=20, height=2)
button_submit.place(x=175, y=305)

pathLabel = Label(myWindow)
pathLabel.place(x=135, y=350)


myWindow.mainloop()