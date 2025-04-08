import tkinter as tk
from tkinter import ttk, messagebox

class ViewStockTab:
    def __init__(self, parent, model):
        self.model = model
        self.frame = ttk.Frame(parent)
        self.on_edit_request = None  # Callback to be set by main app
        self.create_widgets()
        self.refresh_data()
    
    def create_widgets(self):
        """Create view stock widgets"""
        # Search frame
        search_frame = ttk.Frame(self.frame)
        search_frame.pack(fill='x', padx=10, pady=10)
        
        ttk.Label(search_frame, text="Search:").pack(side='left')
        self.search_entry = ttk.Entry(search_frame)
        self.search_entry.pack(side='left', expand=True, fill='x', padx=5)
        ttk.Button(search_frame, text="Search", command=self.search_items).pack(side='left', padx=5)
        ttk.Button(search_frame, text="Show All", command=self.refresh_data).pack(side='left')
        
        # Treeview
        self.tree = ttk.Treeview(self.frame, columns=('ID', 'Name', 'Quantity', 'Price', 'Category'), show='headings')
        
        # Configure columns
        for col in ['ID', 'Name', 'Quantity', 'Price', 'Category']:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100 if col != 'Name' else 200)
        
        self.tree.pack(expand=True, fill='both', padx=10, pady=10)
        
        # Action buttons
        button_frame = ttk.Frame(self.frame)
        button_frame.pack(pady=10)
        
        ttk.Button(button_frame, text="Delete Selected", command=self.delete_item).pack(side='left', padx=5)
        ttk.Button(button_frame, text="Edit Selected", command=self.edit_item).pack(side='left', padx=5)
        ttk.Button(button_frame, text="Refresh", command=self.refresh_data).pack(side='left', padx=5)
    
    def refresh_data(self):
        """Refresh treeview with all items"""
        self.tree.delete(*self.tree.get_children())
        for item_id, details in self.model.get_all_items():
            self.tree.insert('', 'end', values=(
                item_id,
                details['name'],
                details['quantity'],
                f"${details['price']:.2f}",
                details['category']
            ))
    
    def search_items(self):
        """Search items based on search term"""
        search_term = self.search_entry.get()
        results = self.model.search_items(search_term)
        
        self.tree.delete(*self.tree.get_children())
        for item_id, details in results.items():
            self.tree.insert('', 'end', values=(
                item_id,
                details['name'],
                details['quantity'],
                f"${details['price']:.2f}",
                details['category']
            ))
    
    def delete_item(self):
        """Delete selected item"""
        selected = self.tree.selection()
        if not selected:
            messagebox.showerror("Error", "No item selected!")
            return
        
        item_id = self.tree.item(selected[0])['values'][0]
        if messagebox.askyesno("Confirm", f"Delete item {item_id}?"):
            if self.model.delete_item(item_id):
                self.refresh_data()
                messagebox.showinfo("Success", "Item deleted successfully!")
    
    def edit_item(self):
        """Request to edit selected item"""
        selected = self.tree.selection()
        if not selected:
            messagebox.showerror("Error", "No item selected!")
            return
        
        item_id = self.tree.item(selected[0])['values'][0]
        if self.on_edit_request:
            self.on_edit_request(item_id)