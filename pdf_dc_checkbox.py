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
    print("Textul introdus este: ", text_entry)

    # opens the document
    file_input = open(user_input, "rb")
    box = PdfReader(file_input).pages[0].mediabox
    page_width = box[2]
    page_height = box[3]
    page_margin = 2

    box_width = 126
    box_height = 20
    text_x = 3
    text_y = 7
    print("Page size in points: ", page_width, page_height)

    d = Drawing(page_width, page_height)

    def top_left(document):
        insert_text = document
        # d = Drawing(page_width, page_height)
        d.add(Rect(page_margin, page_height - box_height - page_margin, box_width, box_height, fill=0, stroke=1,
                   strokeColor=colors.red, fillColor=colors.white))
        d.add(String(page_margin + text_x, float(page_height - box_height - page_margin + text_y),
                     insert_text + text_entry + "/" + date, fontSize=9, stroke=1, fillColor=colors.red))

    def top_right(document):
        insert_text = document
        # d = Drawing(page_width, page_height)
        d.add(Rect(page_width - box_width - page_margin, page_height - box_height - page_margin, box_width, box_height,
                   fill=0, stroke=1, strokeColor=colors.red, fillColor=colors.white))
        d.add(String(page_width - box_width - page_margin + text_x,
                     float(page_height - box_height - page_margin + text_y),
                     insert_text + text_entry + "/" + date, fontSize=9, stroke=1, fillColor=colors.red))

    def bottom_left(document):
        insert_text = document
        # d = Drawing(page_width, page_height)
        d.add(Rect(page_margin, page_margin, box_width, box_height, fill=0, stroke=1, strokeColor=colors.red,
                   fillColor=colors.white))
        d.add(String(page_margin + text_x, text_y + 1, insert_text + text_entry + "/" + date, fontSize=9, stroke=1,
                     fillColor=colors.red))

    def bottom_right(document):
        insert_text = document
        # d = Drawing(page_width, page_height)
        d.add(Rect(page_width - box_width - page_margin, page_margin, box_width, box_height, fill=0, stroke=1,
                   strokeColor=colors.red, fillColor=colors.white))
        d.add(String(page_width - box_width, text_y + 1, insert_text + text_entry + "/" + date, fontSize=9, stroke=1,
                     fillColor=colors.red))

    match type_of_document_value.get(), placement_var.get():
        case 1, 1:
            top_left("Nr. intrare DC: ")
        case 1, 2:
            top_right("Nr. intrare DC: ")
        case 1, 3:
            bottom_left("Nr. intrare DC: ")
        case 1, 4:
            bottom_right("Nr. intrare DC: ")
        case 2, 1:
            top_left("Nr. iesire DC: ")
        case 2, 2:
            top_right("Nr. iesire DC: ")
        case 2, 3:
            bottom_left("Nr. iesire DC: ")
        case 2, 4:
            bottom_right("Nr. iesire DC: ")
        case _:
            print("Nu au fost alese optiuni valide")

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
    # with open(text_entry + ".pdf", "wb") as output:
    #     pdf_writer.write(output)

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
    print("Nume fisierului este: ", file_name)
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
        if isinstance(widget, Checkbutton):
            placement_var.set(None)
            canvas.create_rectangle(4, 4, 20, 10, outline="", fill="white")
            canvas.create_rectangle(4, 60, 20, 66, outline="", fill="white")
            canvas.create_rectangle(32, 4, 48, 10, outline="", fill="white")
            canvas.create_rectangle(32, 60, 48, 66, outline="", fill="white")

def clear_selection():
    canvas.create_rectangle(4,4,20,10, outline="", fill="white")
    canvas.create_rectangle(4,60,20,66, outline="", fill="white")
    canvas.create_rectangle(32,4,48,10, outline="", fill="white")
    canvas.create_rectangle(32,60,48,66, outline="", fill="white")


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

def create_tl_dot():
    canvas.create_rectangle(4,4,20,10, outline="", fill="white")
    canvas.create_rectangle(4,60,20,66, outline="", fill="white")
    canvas.create_rectangle(32,4,48,10, outline="", fill="white")
    canvas.create_rectangle(32,60,48,66, outline="", fill="white")
    canvas.create_rectangle(4, 4, 20, 10, outline="", fill="black")
top_left_option = Checkbutton(myWindow, text = "",
					variable = placement_var,
					onvalue = 1,
					offvalue = None,
					height = 2,
					width = 10,
                    command=lambda: create_tl_dot())
top_left_option.place(x=165, y=182)
top_left_label = Label(text="Top left")
top_left_label.place(x=153, y=190)

def create_tr_dot():
    canvas.create_rectangle(4,4,20,10, outline="", fill="white")
    canvas.create_rectangle(4,60,20,66, outline="", fill="white")
    canvas.create_rectangle(32,4,48,10, outline="", fill="white")
    canvas.create_rectangle(32,60,48,66, outline="", fill="white")
    canvas.create_rectangle(32, 4, 48, 10, outline="", fill="black")
top_right_option = Checkbutton(myWindow, text = "",
					variable = placement_var,
					onvalue = 2,
					offvalue = None,
					height = 2,
					width = 10,
                    command=lambda: create_tr_dot())
top_right_option.place(x=242, y=182)
top_right_label = Label(text="Top right")
top_right_label.place(x=300, y=190)

def create_bl_dot():
    canvas.create_rectangle(4,4,20,10, outline="", fill="white")
    canvas.create_rectangle(4,60,20,66, outline="", fill="white")
    canvas.create_rectangle(32,4,48,10, outline="", fill="white")
    canvas.create_rectangle(32,60,48,66, outline="", fill="white")
    canvas.create_rectangle(4,60,20,66, outline="", fill="black")
bottom_left_option = Checkbutton(myWindow, text = "",
					variable = placement_var,
					onvalue = 3,
					offvalue = None,
					height = 2,
					width = 10,
                    command=lambda: create_bl_dot())
bottom_left_option.place(x=165, y=252)
bottom_left_label = Label(text="Bottom left")
bottom_left_label.place(x=133, y=260)

def create_br_dot():
    canvas.create_rectangle(4,4,20,10, outline="", fill="white")
    canvas.create_rectangle(4,60,20,66, outline="", fill="white")
    canvas.create_rectangle(32,4,48,10, outline="", fill="white")
    canvas.create_rectangle(32,60,48,66, outline="", fill="white")
    canvas.create_rectangle(32,60,48,66, outline="", fill="black")
bottom_right_option = Checkbutton(myWindow, text = "",
					variable = placement_var,
					onvalue = 4,
					offvalue = None,
					height = 2,
					width = 10,
                    command=lambda: create_br_dot())
bottom_right_option.place(x=242, y=252)
bottom_right_label = Label(text="Bottom right")
bottom_right_label.place(x=300, y=252)

canvas = Canvas(myWindow, height=70, width=50, bg="#f7f7f7")
canvas.place(x=222, y=200)
canvas.create_rectangle(2,2,50,68)

sep_3 = ttk.Separator(myWindow, orient='horizontal')
sep_3.place(x=0, y=290, relwidth=1)

button_submit = Button(myWindow, text ="CREATE PDF", command=submit_function)
button_submit.config(width=20, height=2)
button_submit.place(x=175, y=305)

pathLabel = Label(myWindow)
pathLabel.place(x=135, y=350)

myWindow.mainloop()