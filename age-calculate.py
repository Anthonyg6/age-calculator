#  create class called Person
#  create init method
#  init method has 2 attributes (name, birthdate)
#  create and object from the Person class
from PIL import Image, ImageTk
import datetime
import tkinter as tk

window = tk.Tk()

window.geometry("500x500")

window.title("Age Calculator App")

# Year label creation , grid placement , Entry form and grid placement for entry

year_label = tk.Label(text="Year")
year_label.grid(column=0, row=1)

year_entry = tk.Entry()
year_entry.grid(column=1, row=1)

# Month label creation , grid placement , Entry form and grid placement for entry

month_label = tk.Label(text="Month")
month_label.grid(column=0, row=2)

month_entry = tk.Entry()
month_entry.grid(column=1, row=2)

# Days label creation , grid placement , Entry form and grid placement for entry

days_label = tk.Label(text="Day")
days_label.grid(column=0, row=3)

days_entry = tk.Entry()
days_entry.grid(column=1, row=3)


def calculate_age():
    print(year_entry.get())
    print(month_entry.get())
    print(days_entry.get())

    # datetime.date requires an INT to be returned so any data that is in a string format, just wrap it up in an int() function and it will convert it to an integar
    anthony = Person('Anthony', datetime.date(
        int(year_entry.get()), int(month_entry.get()), int(days_entry.get())))
    anthony.age()

    text_answer = tk.Text(window, height=20, width=25)
    text_answer.grid(column=1, row=5)

    answer_text = "{fullname} is {age} years old!".format(
        fullname=anthony.fullname, age=anthony.age())

    text_answer.insert(tk.END, answer_text)


calculate_btn = tk.Button(text="Calculate Now", command=calculate_age)
calculate_btn.grid(column=1, row=4)


class Person:
    def __init__(self, fullname, birthdate):
        self.fullname = fullname
        self.birthdate = birthdate

        # age method that creates a today age object that holds todays date
        # an age object that stores todays.year - the self.birthdate.year date & then we return the age
        #
    def age(self):
        today = datetime.date.today()
        # attaching the .year attribute to the today object & the birthdate object we are telling python to ignore the months and days of todays date and the birthdate so that we only return the year number. ".year attribute does not require () after. It will throw an error"
        age = today.year - self.birthdate.year
        return age


# person = Person('Anthony Gallegos', datetime.date(1993, 5, 31))

# print(person.fullname)
# print(person.birthdate)
# print(person.age())

image = Image.open('../images/coding.jpg')
image.thumbnail((200, 200), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
label_image = tk.Label(image=photo)
label_image.grid(column=1, row=0)

window.mainloop()
