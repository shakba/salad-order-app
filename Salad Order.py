import tkinter as tk

class SaladOrderApp:
    def __init__(self, master):
        self.master = master
        master.title("Salad Order App")

        # Create a list of ingredients
        self.ingredients = [
            "Cucumber", "Tomato", "Lettuce", "Cabbage", "Onion",
            "Yellow Peppers", "Green Peppers", "Red Peppers",
            "Lemon", "Olive Oil", "Salt", "Pepper"
        ]

        # Create a variable to store the selected ingredients
        self.selected_ingredients = []

        # Create a label and a listbox for the ingredients
        self.label_ingredients = tk.Label(master, text="Ingredients:")
        self.label_ingredients.pack()

        self.listbox_ingredients = tk.Listbox(master, selectmode=tk.MULTIPLE)
        for ingredient in self.ingredients:
            self.listbox_ingredients.insert(tk.END, ingredient)
        self.listbox_ingredients.pack()

        # Create a button to add the selected ingredients to the salad
        self.button_add_ingredients = tk.Button(master, text="Add to Salad", command=self.add_ingredients)
        self.button_add_ingredients.pack()

        # Create a label to display the selected ingredients
        self.label_selected_ingredients = tk.Label(master, text="Selected Ingredients:")
        self.label_selected_ingredients.pack()

        self.listbox_selected_ingredients = tk.Listbox(master)
        self.listbox_selected_ingredients.pack()

        # Create a button to clear the selected ingredients
        self.button_clear_ingredients = tk.Button(master, text="Clear Selection", command=self.clear_ingredients)
        self.button_clear_ingredients.pack()

        # Create a button to place the order
        self.button_place_order = tk.Button(master, text="Place Order", command=self.place_order)
        self.button_place_order.pack()

    def add_ingredients(self):
        # Get the selected ingredients from the listbox
        selected = self.listbox_ingredients.curselection()

        # Add the selected ingredients to the list of selected ingredients
        for index in selected:
            ingredient = self.listbox_ingredients.get(index)
            if ingredient not in self.selected_ingredients:
                self.selected_ingredients.append(ingredient)
                self.listbox_selected_ingredients.insert(tk.END, ingredient)

    def clear_ingredients(self):
        # Clear the selected ingredients from the listbox and the list of selected ingredients
        self.selected_ingredients.clear()
        self.listbox_selected_ingredients.delete(0, tk.END)

    def place_order(self):
        # Display a message box with the selected ingredients
        if self.selected_ingredients:
            message = "Your salad with the following ingredients has been ordered:\n"
            for ingredient in self.selected_ingredients:
                message += "- " + ingredient + "\n"
            tk.messagebox.showinfo("Order Placed", message)
        else:
            tk.messagebox.showerror("Error", "Please select at least one ingredient.")

root = tk.Tk()
app = SaladOrderApp(root)
root.mainloop()
