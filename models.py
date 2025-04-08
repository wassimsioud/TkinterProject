import json
import os

class StockModel:
    def __init__(self):
        self.data_file = "stock_data.json"
        self.stock_data = self.load_data()
    
    def load_data(self):
        """Load stock data from JSON file"""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                return json.load(f)
        return {}
    
    def save_data(self):
        """Save stock data to JSON file"""
        with open(self.data_file, 'w') as f:
            json.dump(self.stock_data, f, indent=4)
    
    def add_item(self, item_id, name, quantity, price, category):
        """Add new item to stock"""
        self.stock_data[item_id] = {
            'name': name,
            'quantity': quantity,
            'price': price,
            'category': category
        }
        self.save_data()
    
    def update_item(self, item_id, name, quantity, price, category):
        """Update existing item"""
        if item_id in self.stock_data:
            self.stock_data[item_id] = {
                'name': name,
                'quantity': quantity,
                'price': price,
                'category': category
            }
            self.save_data()
            return True
        return False
    
    def delete_item(self, item_id):
        """Delete item from stock"""
        if item_id in self.stock_data:
            del self.stock_data[item_id]
            self.save_data()
            return True
        return False
    
    def get_item(self, item_id):
        """Get item details"""
        return self.stock_data.get(item_id)
    
    def get_all_items(self):
        """Get all items"""
        return self.stock_data.items()
    
    def search_items(self, search_term):
        """Search items by name or ID"""
        search_term = search_term.lower()
        return {
            k: v for k, v in self.stock_data.items()
            if search_term in k.lower() or search_term in v['name'].lower()
        }