from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import re
import datetime

s = ""
path = ""
current_file = 'No File'
font = ""
style = ""
size = ""
start = '1.0'


def opt_undo():
    text1.delete('1.0', END)


def opt_new():
    global current_file, text1
    if current_file != "No file" and text1.get('1.0', END + '-1c'):
        res = messagebox.askyesnocancel(title="Notepad", message="Do you want to save changes?")
        if res:
            opt_saveas()
        else:
            text1.delete('1.0', END)
            current_file = ""


def opt_open():
    global current_file, path
    f = filedialog.askopenfile(title="Open", filetypes=(("text files", "*.txt"), ("all files", "*.*")))
    if f != None:
        text1.delete('1.0', END)
        content = f.read()
        text1.insert('1.0', content)
        name = f.name.split("/")[-1].split(".")[0]
        root.title(name)
        text1.pack(fill='both', expand=True)
        current_file = name
        path = f.name


def opt_copy():
    text1.event_generate("<<Copy>>")


def opt_cut():
    text1.event_generate("<<Cut>>")


def opt_del():
    s = text1.selection_get()
    text1.delete(s)


def opt_paste():
    text1.event_generate("<<Paste>>")


def opt_datetime():
    a = datetime.datetime.today()
    text1.insert(END, a)


def opt_find():
    def btn_fd():
        global start
        countVar = StringVar()
        if start < END:
            p = entry_find.get()
            pos = text1.search(p, start, stopindex="end", count=countVar)
            length = "{}+{}c".format(pos, countVar.get())
            text1.tag_add("highlight", pos, length)
            text1.tag_config("highlight", background="green")
            start = length

    root_find = Tk()
    root_find.geometry('200x200+2+2')
    label1 = Label(root_find, text="Find What:")
    label1.place(relx=0.0, rely=0.15, relheight=0.2, relwidth=0.3)
    entry_find = Entry(root_find)
    entry_find.place(relx=0.35, rely=0.2, relheight=0.1, relwidth=0.3)
    # print(find.span())
    button_find1 = Button(root_find, text="Find Text", command=btn_fd)
    button_find1.place(relx=0.7, rely=0.2, relheight=0.1, relwidth=0.3)
    button_find2 = Button(root_find, text="Cancel")
    button_find2.place(relx=0.7, rely=0.4, relheight=0.1, relwidth=0.3)
    radiobutton_up = Radiobutton(root_find, text="Up")
    radiobutton_up.deselect()
    radiobutton_up.place(relx=0.4, rely=0.6, relheight=0.1, relwidth=0.3)
    radiobutton_down = Radiobutton(root_find, text="Down")
    radiobutton_down.deselect()
    radiobutton_down.place(relx=0.6, rely=0.6, relheight=0.1, relwidth=0.3)
    checkbutton1 = Checkbutton(root_find, text="Match")
    checkbutton1.place(relx=0.0, rely=0.9, relheight=0.1, relwidth=0.3)
    root_find.mainloop()


def opt_saveas():
    global current_file, path
    f = filedialog.asksaveasfile(title="Save As", defaultextension="txt",
                                 filetypes=(("text files", "*.txt"), ("all files", "*.*")))
    if f != None:
        data = text1.get('1.0', END + '-1c')
        f.write(data)
        path = f.name
        root.title(f.name.split("/")[-1].split(".")[0])
        current_file = root.title()
        f.close()


def opt_save():
    global current_file, path
    if current_file == "No File":
        opt_saveas()
    else:
        data = text1.get('1.0', END)
        file = open(path, 'w')
        file.write(data)
        file.close()


def opt_pagesetup():
    root_pagesetup = Tk()
    button_p = Radiobutton(root_pagesetup, text="Potrait")
    button_p.deselect()
    button_p.place(relx=0.1, rely=0.2, relheight=0.2, relwidth=0.3)
    button_l = Radiobutton(root_pagesetup, text="Landscape")
    button_l.place(relx=0.1, rely=0.4, relheight=0.2, relwidth=0.4)
    root_pagesetup.mainloop()


def opt_replace():
    def btn_rfd():
        pass

    root_replace = Tk()
    root_replace.geometry("200x200+5+5")
    replace = StringVar()
    root_replace.geometry('200x200+2+2')
    label1 = Label(root_replace, text="Find What:")
    label1.place(relx=0.0, rely=0.15, relheight=0.2, relwidth=0.35)
    entry_replace = Entry(root_replace, textvariable=replace)
    entry_replace.place(relx=0.35, rely=0.2, relheight=0.1, relwidth=0.3)
    label2 = Label(root_replace, text="Replace With:")
    label2.place(relx=0.0, rely=0.35, relheight=0.2, relwidth=0.35)
    entry_replace2 = Entry(root_replace, textvariable=replace)
    entry_replace2.place(relx=0.35, rely=0.4, relheight=0.1, relwidth=0.3)
    button_replace1 = Button(root_replace, text="Find Text", command=btn_rfd)
    button_replace1.place(relx=0.7, rely=0.2, relheight=0.1, relwidth=0.3)
    button_replace2 = Button(root_replace, text="Replace")
    button_replace2.place(relx=0.7, rely=0.4, relheight=0.1, relwidth=0.3)
    button_replace3 = Button(root_replace, text="Replace All")
    button_replace3.place(relx=0.7, rely=0.6, relheight=0.1, relwidth=0.3)
    button_replace4 = Button(root_replace, text="Cancel")
    button_replace4.place(relx=0.7, rely=0.8, relheight=0.1, relwidth=0.3)
    checkbutton_replace = Checkbutton(root_replace, text="Match")
    checkbutton_replace.place(relx=0.0, rely=0.9, relheight=0.1, relwidth=0.3)
    root_replace.mainloop()


def opt_exit():
    global current_file, te
    if current_file != "No file" or te.get('1.0', tk.END + '-1c'):
        res = messagebox.askyesnocancel(title="Notepad",
                                        message="Do you want to save changes to\n{}".format(current_file))
        if res:
            filedialog.asksaveasfile(title="Save As", defaultextension="txt",
                                     filetypes=(("text files", "*.txt"), ("all files", "*.*")))
        else:
            root.destroy()


def opt_goto():
    def highlight(n):
        text1.tag_add("highlight", "{}.0".format(n), "{}.end".format(n))
        text1.tag_config("highlight", background="blue", foreground="yellow")

    def remove_highlight():
        text1.tag_remove("highlight", '1.0', END)

    def btn_goto():
        remove_highlight()
        line = entry_goto.get()
        highlight(line)

    root_goto = Tk()
    root_goto.title("Go To Line")
    label_go = Label(root_goto, text="Line Number:")
    label_go.place(relx=0.1, rely=0.2, relheight=0.1, relwidth=0.4)
    entry_goto = Entry(root_goto, width=10)
    entry_goto.place(relx=0.1, rely=0.3, relheight=0.1, relwidth=0.4)
    button_goto = Button(root_goto, command=btn_goto)
    button_goto.place(relx=0.3, rely=0.5, relheight=0.1, relwidth=0.3)
    button_gotocancel = Button(root_goto, text="Cancel")
    button_gotocancel.place(relx=0.7, rely=0.5, relheight=0.1, relwidth=0.3)
    root_goto.mainloop()


def opt_print():
    pass


def opt_selectall():
    text1.tag_add("highlight", '1.0', END)
    text1.tag_config("highlight", background="light blue")


def opt_wordwrap():
    pass


def opt_font():
    def font(font1):
        global font
        font = combobox_font.get()

    def style(style1):
        global style
        style = combobox_style.get()

    def size(size1):
        global size
        size = combobox_size.get()

    def re_ok():
        global font, style, size
        text1['font'] = font + " " + size + " " + style
        font = ""
        style = ""
        size = ""
        root_font.destroy()

    def re_cancel():
        root_font.destroy()

    root_font = Tk()
    root_font.geometry('300x300+5+5')
    root_font.title("Font")
    label_font = Label(root_font, text="Font:")
    label_font.place(relx=0.0, rely=0.1, relheight=0.1, relwidth=0.3)
    combobox_font = ttk.Combobox(root_font)
    combobox_font['values'] = ('Modern', 'Verdana', 'Arial', 'Roman', 'Calibri', 'Cambria',
                               'Candara', 'Century', 'Constantia', 'Courier', 'Impact', 'System')
    combobox_font.place(relx=0.0, rely=0.2, relheight=0.1, relwidth=0.3)
    label_style = Label(root_font, text="Font Style:")
    label_style.place(relx=0.4, rely=0.1, relheight=0.1, relwidth=0.3)
    combobox_style = ttk.Combobox(root_font)
    combobox_style['values'] = ('bold')
    combobox_style.place(relx=0.4, rely=0.2, relheight=0.1, relwidth=0.3)
    label_size = Label(root_font, text="Font Size:")
    label_size.place(relx=0.75, rely=0.1, relheight=0.1, relwidth=0.3)
    combobox_size = ttk.Combobox(root_font)
    combobox_size['values'] = ('8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                               '21', '22', '23', '24')
    combobox_size.place(relx=0.75, rely=0.2, relheight=0.1, relwidth=0.2)
    combobox_font.bind("<<ComboboxSelected>>", font)
    combobox_style.bind("<<ComboboxSelected>>", style)
    combobox_size.bind("<<ComboboxSelected>>", size)
    button_ok = Button(root_font, text="Ok", command=re_ok)
    button_ok.place(relx=0.5, rely=0.6, relheight=0.1, relwidth=0.2)
    button_cancel = Button(root_font, text="Cancel", command=re_cancel)
    button_cancel.place(relx=0.75, rely=0.6, relheight=0.1, relwidth=0.2)
    root_font.mainloop()


def opt_statusbar():
    pass


def opt_viewhelp():
    import webbrowser
    import platform
    op_sys = platform.system()
    term = "How to get notepad help in " + op_sys
    url = "https://www.google.com.tr/search?q={}".format(term)
    webbrowser.open_new_tab(url)


def opt_aboutnotepad():
    pass


# ******************************************************************************************

root = Tk()
root.title("Untitled-Notepad")
v = StringVar()

scrollbar1 = Scrollbar(root)
scrollbar2 = Scrollbar(root, orient=HORIZONTAL)
scrollbar1.pack(side=RIGHT, fill=Y)
scrollbar2.pack(side=BOTTOM, fill=X)
text1 = Text(root, yscrollcommand=scrollbar1.set,
             xscrollcommand=scrollbar2.set, font="Arial 10 ")
text1.pack(fill=BOTH, expand=True)
scrollbar1.config(command=text1.yview)
scrollbar2.config(command=text1.yview)

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New                  Ctrl+N", command=opt_new)
filemenu.add_command(label="Open..              Ctrl+O", command=opt_open)
filemenu.add_command(label="Save                  Ctrl+S", command=opt_save)
filemenu.add_command(label="Save As..", command=opt_saveas)
filemenu.add_separator()
filemenu.add_command(label="Page Setup..     Ctrl+P", command=opt_pagesetup)
filemenu.add_command(label="Print", command=opt_print)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=opt_exit)

editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Undo               Ctlr+Z", command=opt_undo)
editmenu.add_separator()
editmenu.add_command(label="Cut                  Ctlr+Z", command=opt_cut)
editmenu.add_command(label="Copy               Ctlr+C", command=opt_copy)
editmenu.add_command(label="Paste               Ctlr+P", command=opt_paste)
editmenu.add_command(label="Delete                  Del", command=opt_del)
editmenu.add_separator()
editmenu.add_command(label="Find..               Ctlr+F", command=opt_find)
editmenu.add_command(label="Find Next               F3")
editmenu.add_command(label="Replace..           Ctrl+H", command=opt_replace)
editmenu.add_command(label="Go To..            Ctrl+G", command=opt_goto)
editmenu.add_separator()
editmenu.add_command(label="Select All         Ctrl+A", command=opt_selectall)
editmenu.add_command(label="Time/Date             F5", command=opt_datetime)

formatmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Format", menu=formatmenu)
formatmenu.add_command(label="Word Wrap", command=opt_wordwrap)
formatmenu.add_command(label="Font..", command=opt_font)

viewmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="View", menu=viewmenu)
viewmenu.add_command(label="Status Bar", command=opt_statusbar)

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="help", menu=helpmenu)
helpmenu.add_command(label="View Help", command=opt_viewhelp)
helpmenu.add_separator()
helpmenu.add_command(label="About Notepad", command=opt_aboutnotepad)

root.config(menu=menubar)
root.mainloop()