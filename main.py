from bs4 import BeautifulSoup
import requests
from tkinter import * 
import random

url = "https://www.pizzeriamilan.nu/"
page = requests.get(url)

    # Creating the soup
soup = BeautifulSoup(page.content, 'html.parser')

    # Initializing the list
h2_list = []

    # Getting all the h2 tags
h2_tags = soup.find_all("div", {"class": "text-wrap"})

    # Appending h2 text to the list
for h2 in h2_tags:
    h2_list.append(h2.find("h2").text)

    # Manipulating the list
h2_list = [item.replace("\n", "").replace("\r", "") for item in h2_list]

    # Printing the list
print(h2_list)


# Function to randomly select an item. 
def random_item(): 
	# Select an item randomly. 
	x = random.choice(h2_list) 
	# Set the label to display the item. 
	label.config(text = x) 

# Create a window. 
root = Tk() 

# Set the title of the window. 
root.title("Random Food picker at Pizzeria Milan") 

# Create a label to display the randomly 
# selected item. 
label = Label(root, font = ('Helvetica', 20)) 
label.pack() 

# Create a button to generate a random item. 
button = Button(root, text = "Get food item", 
				command = random_item, 
				bg = "white", fg = "black") 
button.pack(fill = X) 

root.geometry("400x100")
# Run the main loop. 
root.mainloop()