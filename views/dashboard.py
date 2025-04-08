import tkinter as tk
from tkinter import ttk

class DashboardTab:
    def __init__(self, parent, model):
        self.model = model
        self.frame = ttk.Frame(parent)
        self.create_widgets()
    
    def create_widgets(self):
        """Create dashboard widgets"""
        # Summary labels
        ttk.Label(self.frame, text="Stock Summary", font=('Arial', 14, 'bold')).pack(pady=10)
        
        # Update dashboard with current data
        self.update_dashboard()
    
    def update_dashboard(self):
        """Update dashboard with current data"""
        # Clear existing widgets (except the title)
        for widget in self.frame.winfo_children()[1:]:
            widget.destroy()
        
        # Total items
        total_items = len(self.model.stock_data)
        ttk.Label(self.frame, text=f"Total Items: {total_items}").pack()
        
        # Low stock items
        low_stock = sum(1 for item in self.model.stock_data.values() if item['quantity'] < 10)
        ttk.Label(self.frame, text=f"Low Stock Items: {low_stock}", 
                 foreground="red" if low_stock > 0 else "black").pack()
        
        # Recent activity
        ttk.Label(self.frame, text="Recent Activity", font=('Arial', 12)).pack(pady=10)
        
        # Add some sample activity
        activity_frame = ttk.Frame(self.frame)
        activity_frame.pack()
        
        activities = [
            "System initialized",
            f"Loaded {total_items} items",
            "Ready for operations"
        ]
        
        for activity in activities:
            ttk.Label(activity_frame, text=f"• {activity}").pack(anchor='w')