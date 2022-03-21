from tkinter import Tk, Button, Message, messagebox, Canvas, StringVar, Menu, Text
from tkinter.filedialog import askopenfile
from PyPDF2 import PdfFileReader


window = Tk()
window.title("Welcome to LikeGeeks app")
window.configure(bg="slategray")
window.eval('tk::PlaceWindow . Center')
window.iconbitmap('files/bucinsk1.ico')
window.resizable(0, 0)

canvas = Canvas(window, width=600, height=300)
canvas.grid(columnspan=3)


def close_app():
    msg_box = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application', icon='warning')
    if msg_box == 'yes':
        window.destroy()
    else:
        messagebox.showinfo('Return', 'You will now return to the application screen')


def select_file():
    #pdf_file = askopenfile(filetypes=[("PDF Files", "*.pdf")]).name
    pdf_file = 'C:/Users/Peter/Downloads/CCN-STIC-652A Seguridad en contenedores.pdf'
    if pdf_file:
        with open(pdf_file, 'rb') as f:
            pdf_file_name.set(pdf_file)
            pdf = PdfFileReader(f)
            information = pdf.getDocumentInfo()
            number_of_pages = pdf.getNumPages()
            #print(pdf.getFields())
            print(pdf_file)
        text_box.delete("1.0", "end")
        text_box.insert('insert', 'Propiedades:')

        txt = f"""
        Author: {information.author}
        Creator: {information.creator}
        Producer: {information.producer}
        Subject: {information.subject}
        Title: {information.title}
        Number of pages: {number_of_pages}
        """

        print(txt)
        text_box.insert('end', txt)
    else:
        msg = "ningún fichero seleccionado"
        pdf_file_name.set(msg)
        print(msg)


# DEFINICIÓN DE WIDGETS
menubar = Menu(window)
filemenu = Menu(menubar, tearoff=1)
#filemenu.add_command(label="New", command=say_hello)
#filemenu.add_command(label="Save", command=say_hello)
submenu = Menu(menubar, tearoff=0)
submenu.add_command(label="Open File", command=select_file)
submenu.add_command(label="Open Folder", command=select_file)
filemenu.add_cascade(label="Open...", menu=submenu)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=close_app)
menubar.add_cascade(label="File", menu=filemenu)

msg_filename = Message(window, text="")
input_cut_from = Message(window, text="")
input_cut_to = Message(window, text="")
button = Button(window,
                text="Buscar archivo...",
                command=select_file,
                activebackground='#345',
                activeforeground='white',
                borderwidth=3,
                # padx=20,
                # pady=5,
                font=('times bold', 10))

text_box = Text(window,
                height=12,
                width=10,
                state='normal')


#UBICACIÓN DE LOS WIDGETS
button.grid(column=0, row=0, sticky="we", padx=10)
pdf_file_name = StringVar()
msg_filename.grid(column=1, row=0, columnspan=2, sticky="we", padx=10)
msg_filename.configure(textvariable=pdf_file_name, anchor="w", width=280)
pdf_cut_from = StringVar()
input_cut_from.grid(column=1, row=1, padx=10)
input_cut_from.configure(textvaria)
cortar_hasta = StringVar()

canvas.grid(column=0, row=1)
text_box.grid(column=0, row=1, sticky="we", padx=10)

window.config(menu=menubar)
window.mainloop()
