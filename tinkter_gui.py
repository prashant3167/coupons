# import openpyxl and tkinter modules
# from openpyxl import *
from tkinter import *

# globally declare wb and sheet variable

# opening the existing excel file

# create the sheet object
# sheet = wb.active


# def excel():
	
# 	return
# 	# resize the width of columns in
# 	# excel spreadsheet
#	 sheet.column_dimensions['A'].width = 30
#	 sheet.column_dimensions['B'].width = 10
#	 sheet.column_dimensions['C'].width = 10
#	 sheet.column_dimensions['D'].width = 20
#	 sheet.column_dimensions['E'].width = 20
#	 sheet.column_dimensions['F'].width = 40
#	 sheet.column_dimensions['G'].width = 50

#	 # write given data to an excel spreadsheet
#	 # at particular location
#	 sheet.cell(row=1, column=1).value = "Name"
#	 sheet.cell(row=1, column=2).value = "Course"
#	 sheet.cell(row=1, column=3).value = "Semester"
#	 sheet.cell(row=1, column=4).value = "Form Number"
#	 sheet.cell(row=1, column=5).value = "Contact Number"
#	 sheet.cell(row=1, column=6).value = "Email id"
#	 sheet.cell(row=1, column=7).value = "Address"


# Function to set focus (cursor)
def focus1(event):
	# set focus on the coupon_field box
	customer_id_field.focus_set()
	# coupon_field.focus_set()


# Function to set focus
def focus2(event):
	# set focus on the price_field box
	coupon_field.focus_set()
	


# Function to set focus
def focus3(event):
	# set focus on the customer_tier_field box
	price_field.focus_set()
	

# Function to set focus
def focus4(event):
	# set focus on the contact_no_field box
	customer_tier_field.focus_set()



# Function to set focus
# def focus5(event):
# 	# set focus on the email_id_field box
# 	email_id_field.focus_set()


# # Function to set focus
# def focus6(event):
# 	# set focus on the address_field box
# 	address_field.focus_set()


# Function for clearing the
# contents of text entry boxes
def clear():
	
	# clear the content of text entry box
	customer_id_field.delete(0, END)
	coupon_field.delete(0, END)
	price_field.delete(0, END)
	customer_tier_field.delete(0, END)
	# contact_no_field.delete(0, END)
	# email_id_field.delete(0, END)
	# address_field.delete(0, END)


# Function to take data from GUI
# window and write to an excel file
def insert():
	
	# if user not fill any entry
	# then print "empty input"
	if (customer_id_field.get() == "" and
		coupon_field.get() == "" and
		price_field.get() == "" and
		customer_tier_field.get() == "" 
		# and
		# contact_no_field.get() == "" and
		# email_id_field.get() == "" and
		# address_field.get() == ""
		):
			
		print("empty input")
	else:
		print(customer_id_field.get())
		print(coupon_field.get())
		print(price_field.get())
		print(customer_tier_field.get())
		# print(contact_no_field.get())
		# print(email_id_field.get())
		# print(address_field.get())

		# assigning the max row and max column
		# value upto which data is written
		# in an excel sheet to the variable
		# current_row = sheet.max_row
		# current_column = sheet.max_column

		# get method returns current text
		# as string which we write into
		# excel spreadsheet at particular location
		

		# save the file
		# wb.save('C:\\Users\\Admin\\Desktop\\excel.xlsx')

		# set focus on the customer_id_field box
		customer_id_field.focus_set()

		# call the clear() function
		clear()


# Driver code
if __name__ == "__main__":
	
	# create a GUI window
	window = Tk()
	window.title("Coupon Mongo")
	window.configure(background="lightgray")
	window.resizable(width=True,height=True)
	window.geometry("1042x521")
	
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
	window.configure(background='grey')

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
	customer_tier= Label(root, text="Customer Tier", bg="grey")

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
	customer_tier.grid(row=4, column=0)
	# contact_no.grid(row=5, column=0)
	# email_id.grid(row=6, column=0)
	# address.grid(row=7, column=0)

	# create a text entry box
	# for typing the information
	_field = Entry(root)
	customer_id_field = Entry(root)
	coupon_field = Entry(root)
	price_field = Entry(root)
	customer_tier_field = Entry(root)
	# email_id_field = Entry(root)
	# address_field = Entry(root)

	# bind method of widget is used for
	# the binding the function with the events

	# whenever the enter key is pressed
	# then call the focus1 function
	customer_id_field.bind("<Return>", focus1)

	# whenever the enter key is pressed
	# then call the focus2 function
	coupon_field.bind("<Return>", focus2)

	# whenever the enter key is pressed
	# then call the focus3 function
	price_field.bind("<Return>", focus3)

	# whenever the enter key is pressed
	# then call the focus4 function
	customer_tier_field.bind("<Return>", focus4)

	# whenever the enter key is pressed
	# then call the focus5 function
	# contact_no_field.bind("<Return>", focus5)

	# whenever the enter key is pressed
	# then call the focus6 function
	# email_id_field.bind("<Return>", focus6)

	# grid method is used for placing
	# the widgets at respective positions
	# in table like structure .
	customer_id_field.grid(row=1, column=1, ipadx="100")
	coupon_field.grid(row=2, column=1, ipadx="100")
	price_field.grid(row=3, column=1, ipadx="100")
	customer_tier_field.grid(row=4, column=1, ipadx="100")
	# contact_no_field.grid(row=5, column=1, ipadx="100")
	# email_id_field.grid(row=6, column=1, ipadx="100")
	# address_field.grid(row=7, column=1, ipadx="100")

	# call excel function
	# excel()

	# create a Submit Button and place into the root window
	submit = Button(root, text="Get Cashback", fg="grey",
							bg="grey", command=insert)
	submit.grid(row=8, column=1,ipady="10")

	# start the GUI
	root.mainloop()
