import tkinter as tk
from tkinter import ttk
from views.dashboard import DashboardTab
from views.add_item import AddItemTab
from views.view_stock import ViewStockTab
from models import StockModel

class StockManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stock Management System")
        self.root.geometry("900x600")
        
        # Initialize model
        self.model = StockModel()
        
        # Create notebook
        self.notebook = ttk.Notebook(self.root)
        
        # Create tabs
        self.tabs = {
            "dashboard": DashboardTab(self.notebook, self.model),
            "add_item": AddItemTab(self.notebook, self.model),
            "view_stock": ViewStockTab(self.notebook, self.model)
        }
        
        # Add tabs to notebook
        self.notebook.add(self.tabs["dashboard"].frame, text="Dashboard")
        self.notebook.add(self.tabs["add_item"].frame, text="Add/Update Item")
        self.notebook.add(self.tabs["view_stock"].frame, text="View Stock")
        
        self.notebook.pack(expand=True, fill='both')
        
        # Connect tab callbacks
        self.setup_callbacks()

    def setup_callbacks(self):
        """Connect callbacks between tabs"""
        self.tabs["add_item"].on_item_added = self.tabs["view_stock"].refresh_data
        self.tabs["view_stock"].on_edit_request = self.tabs["add_item"].load_item_data

if __name__ == "__main__":
    root = tk.Tk()
    app = StockManagementApp(root)
    root.mainloop()