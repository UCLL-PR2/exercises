from student import *
import unittest

class TestOrderHistory(unittest.TestCase):
    def setUp(self):
        # Create some items
        self.i1 = Item("Widget", 10.99)
        self.i2 = Item("Thingamajig", 5.99)
        self.i3 = Item("Doodad", 15.99)
        self.i4 = Item("Gizmo", 20.99)
        
        # Create some orders
        self.o1 = Order([self.i1, self.i2])
        self.o2 = Order([self.i3, self.i4])
        
        # Create some customers
        self.c1 = Customer("Alice", [self.o1, self.o2])
        self.c2 = Customer("Bob", [self.o2])
        
        # Create an order history
        self.oh = OrderHistory({
            "Alice": self.c1,
            "Bob": self.c2
        })
    
    def test_total_sales(self):
        self.assertEqual(self.oh.get_total_sales(), 90.94)
    
    def test_customer_names(self):
        self.assertEqual(self.oh.get_customer_names(), ["Alice", "Bob"])
    
    def test_top_spender(self):
        self.assertEqual(self.oh.get_top_spender(), "Alice")
    
    def test_total_spent(self):
        self.assertEqual(round(self.c1.get_total_spent(),2), 53.96)
    
    def test_order_count(self):
        self.assertEqual(self.c1.get_order_count(), 2)
    
    def test_average_order_size(self):
        self.assertEqual(round(self.c1.get_average_order_size(),2), 26.98)
    
    def test_item_names(self):
        self.assertEqual(self.o1.get_item_names(), ["Widget", "Thingamajig"])
        self.o1.add_item(self.i3)
        self.assertEqual(self.o1.get_item_names(), ["Widget", "Thingamajig", "Doodad"])
        self.o1.remove_item(self.i2)
        self.assertEqual(self.o1.get_item_names(), ["Widget", "Doodad"])

if __name__ == '__main__':
    unittest.main()
