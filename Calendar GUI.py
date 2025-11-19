from tkinter import *
import calendar

def showCalender():
    import tkinter as tk
    from tkinter import Toplevel
    year = int(year_field.get())
    cal_content = calendar.calendar(year)
    cal_window = Toplevel()
    cal_window.title(f"Calendar for {year}")
    cal_window.geometry("550x600")
    text = Text(cal_window)
    text.insert(INSERT, cal_content)
    text.pack()

if __name__ == '__main__':
    new = Tk()
    new.config(background='grey')
    new.title("Calendar")
    new.geometry("250x160")

    cal = Label(new, text="Calendar", bg='grey', font=("times", 28, "bold"))
    year = Label(new, text="Enter year", bg='dark grey')
    year_field = Entry(new)

    button = Button(new, text='Show Calendar', fg='Black', bg='Blue', command=showCalender)
    exit_button = Button(new, text='Exit', fg='Black', bg='Red', command=new.destroy)

    # Putting widgets in position
    cal.grid(row=1, column=1)
    year.grid(row=2, column=1)
    year_field.grid(row=3, column=1)
    button.grid(row=4, column=1)
    exit_button.grid(row=6, column=1)

    new.mainloop()