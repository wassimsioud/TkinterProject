import tkinter as tk
from tkinter import ttk, messagebox

class AddItemTab:
    def __init__(self, parent, model):
        self.model = model
        self.frame = ttk.Frame(parent)
        self.create_widgets()
        self.on_item_added = None  # Callback to be set by main app
    
    def create_widgets(self):
        """Create form widgets"""
        form_frame = ttk.Frame(self.frame)
        form_frame.pack(pady=20, padx=20, fill='x')
        
        # Form fields
        fields = [
            ("Item ID:", "item_id_entry"),
            ("Item Name:", "item_name_entry"),
            ("Quantity:", "quantity_entry"),
            ("Price:", "price_entry"),
            ("Category:", "category_entry")
        ]
        
        for i, (label_text, attr_name) in enumerate(fields):
            ttk.Label(form_frame, text=label_text).grid(row=i, column=0, sticky='w', pady=5)
            entry = ttk.Entry(form_frame)
            entry.grid(row=i, column=1, sticky='ew', pady=5)
            setattr(self, attr_name, entry)
        
        # Buttons
        button_frame = ttk.Frame(self.frame)
        button_frame.pack(pady=10)
        
        ttk.Button(button_frame, text="Add Item", command=self.add_item).pack(side='left', padx=5)
        ttk.Button(button_frame, text="Update Item", command=self.update_item).pack(side='left', padx=5)
        ttk.Button(button_frame, text="Clear Form", command=self.clear_form).pack(side='left', padx=5)
    
    def add_item(self):
        """Handle add item action"""
        item_id = self.item_id_entry.get()
        name = self.item_name_entry.get()
        quantity = self.quantity_entry.get()
        price = self.price_entry.get()
        category = self.category_entry.get()
        
        if not all([item_id, name, quantity, price, category]):
            messagebox.showerror("Error", "All fields are required!")
            return
        
        try:
            quantity = int(quantity)
            price = float(price)
        except ValueError:
            messagebox.showerror("Error", "Quantity must be integer and price must be number!")
            return
        
        if item_id in self.model.stock_data:
            messagebox.showerror("Error", "Item ID already exists!")
            return
        
        self.model.add_item(item_id, name, quantity, price, category)
        messagebox.showinfo("Success", "Item added successfully!")
        self.clear_form()
        
        # Notify other tabs about the change
        if self.on_item_added:
            self.on_item_added()
    
    def update_item(self):
        """Handle update item action"""
        # Similar to add_item but with update logic
        pass
    
    def clear_form(self):
        """Clear all form fields"""
        for entry in [self.item_id_entry, self.item_name_entry, 
                     self.quantity_entry, self.price_entry, self.category_entry]:
            entry.delete(0, tk.END)
    
    def load_item_data(self, item_id):
        """Load item data into form for editing"""
        item = self.model.get_item(item_id)
        if item:
            self.clear_form()
            self.item_id_entry.insert(0, item_id)
            self.item_name_entry.insert(0, item['name'])
            self.quantity_entry.insert(0, str(item['quantity']))
            self.price_entry.insert(0, str(item['price']))
            self.category_entry.insert(0, item['category'])