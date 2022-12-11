from tkinter import *
from tkinter import messagebox
import sys
from coupon_checker import verify_coupon
from termcolor import colored


class TextRedirector(object):
    def __init__(self, widget, tag="stdout"):
        self.widget = widget
        self.tag = tag
        self.widget.configure(state="disabled")
		# self.widget.

    def write(self, str):
        self.widget.configure(state="normal")
        self.widget.insert("end", str, (self.tag,))
        self.widget.see(END)
        self.widget.configure(state="disabled")


def print_stdout():
	'''Illustrate that using 'print' writes to stdout'''
	print(colored('hello', 'red'))

def print_stderr():
	'''Illustrate that we can write directly to stderr'''
	# sys.stderr.write("this is stderr\n")
	pass


def focus1(event):
	customer_id_field.focus_set()


def focus2(event):
	coupon_field.focus_set()
	


def focus3(event):
	# set focus on the customer_tier_field box
	price_field.focus_set()
	

# Function to set focus
# def focus4(event):
# 	# set focus on the contact_no_field box
# 	customer_tier_field.focus_set()

def focus5(event): 
	db_select_field.focus_set()

def clear():
	# clear the content of text entry box
	customer_id_field.delete(0, END)
	coupon_field.delete(0, END)
	price_field.delete(0, END)
	# customer_tier_field.delete(0, END)


# Function to take data from GUI
# window and write to an excel file
def clear_box():
	# print("I am called")
	text.configure(state="normal")
	text.delete('1.0', END)
	text.configure(state="disabled")

def insert():
	# print(variable.get())
	# if user not fill any entry
	# then print "empty input"
	if (customer_id_field.get() == "" and
		coupon_field.get() == "" and
		price_field.get() == ""
		# customer_tier_field.get() == "" 
		):
		# print_stdout()
		# print_stderr()
		# print(verify_coupon("black_friday_101BYP", 'sullivanjoe', 200))
		print("empty input")
	else:
		print(f"Performing everythin in {variable.get()}")
		a,b = verify_coupon(coupon_field.get(), customer_id_field.get(), price_field.get(),variable.get())
		print("********************************************")
		if b is None:
			messagebox.showerror(title="Coupon not valid", message=a)
		else:
			messagebox.showerror(title="Vollaa!!!", message=f"Final Price: {a}\n Discount applicable: {b}")
		customer_id_field.focus_set()

		# call the clear() function
		clear()


# Driver code
if __name__ == "__main__":
	
	# create a GUI window
	window = Tk()
	icon = PhotoImage(file = 'image/coupon.png')
	window.iconphoto(False, icon)
	# window.attributes('-fullscreen',True)
	window.title("Coupon System")
	window.configure(background="lightgray")
	# window.resizable(width=True,height=True)
	width= window.winfo_screenwidth()               
	height= window.winfo_screenheight()
	window.geometry("%dx%d" % (width, height))
	
	
	root = Frame().grid()
	history = Frame().grid()
	window.grid_columnconfigure(0, weight = 1)
	window.grid_columnconfigure(1, weight = 1)
	window.grid_rowconfigure(0, weight = 1)
	
	root = Frame(window, bg = "grey")
	root.grid(row = 0, column = 0, sticky = "nesw")
	history = Frame(window, bg = "white")
	history.grid(row = 0, column = 1, sticky = "nesw")
	heading = Label(history, text="Result", bg="grey")
	heading.grid(row=0, column=0)

	# set the background colour of GUI window
	# window.configure(background='grey')
	heading.grid_propagate(True)
	text = Text(heading, height=60,width=80,font=("Helvetica", 16))
	text.place_configure(relheight=0.8)
	text.config(state=NORMAL)
	text.pack(fill="both", expand=True)
	text.see(END)
	# text.grid_size(y = 20, height = 25, width = 200)
	text.tag_configure("stderr", foreground="#b22222")
	sys.stdout = TextRedirector(text, "stdout")
	# sys.stderr = TextRedirector(text, "stderr")
	# set the title of GUI window
	# root.title("registration form")

	# set the configuration of GUI window
	# root.geometry("800x800")


	# create a Form label
	heading = Label(root, text="Coupon Applier POC", bg="grey")

	# create a Name label
	customer_id = Label(root, text="Customer Id", bg="grey")

	# create a Course label
	price = Label(root, text="Price", bg="grey")

	# create a Semester label
	coupon = Label(root, text="Coupon", bg="grey")

	# create a Form No. label
	# customer_tier= Label(root, text="Customer Tier", bg="grey")

	db_select = Label(root, text="Select Database", bg="grey")

	# # create a Contact No. label
	# contact_no = Label(root, text="Contact No.", bg="grey")

	# # create a Email id label
	# email_id = Label(root, text="Email id", bg="grey")

	# # create a address label
	# address = Label(root, text="Address", bg="grey")

	# grid method is used for placing
	# the widgets at respective positions
	# in table like structure .
	
	heading.grid(row=0, column=1)
	customer_id.grid(row=1, column=0)
	coupon.grid(row=2, column=0)
	price.grid(row=3, column=0)
	# customer_tier.grid(row=4, column=0)
	db_select.grid(row=4,column=0)

	customer_id_field = Entry(root)
	coupon_field = Entry(root)
	price_field = Entry(root)
	# customer_tier_field = Entry(root)

	OPTIONS = [
	"MongoDB",
	"CouchBase",
	"Postgres"
	]
	variable = StringVar(root)
	variable.set(OPTIONS[0])
	db_select_field= OptionMenu(root, variable, *OPTIONS)
	customer_id_field.bind("<Return>", focus1)

	# whenever the enter key is pressed
	# then call the focus2 function
	coupon_field.bind("<Return>", focus2)

	# whenever the enter key is pressed
	# then call the focus3 function
	price_field.bind("<Return>", focus3)

	# whenever the enter key is pressed
	# then call the focus4 function
	# customer_tier_field.bind("<Return>", focus4)

	db_select_field.bind("<Return>", focus5)


	customer_id_field.grid(row=1, column=1, ipadx="100")
	coupon_field.grid(row=2, column=1, ipadx="100")
	price_field.grid(row=3, column=1, ipadx="100")
	# customer_tier_field.grid(row=4, column=1, ipadx="100")
	db_select_field.grid(row=4, column=1, ipadx="100")

	submit = Button(root, text="Get Cashback", fg="grey",
							bg="grey", command=insert,pady=10)


	clear_box_button = Button(history, text="Clear textbox", fg="grey",
							bg="grey", command=clear_box,pady=5)
	submit.grid(row=6, column=1,pady=10)

	clear_box_button.place_configure(rely=0.95,relx=0.4)

	# start the GUI
	root.mainloop()
