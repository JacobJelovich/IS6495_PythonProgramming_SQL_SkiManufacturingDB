#Program file that defines the OrderLine class that represents the OrderLine table.

class OrderLine:

    #Constructor to get the Database
    def __init__(self, db_obj):
        self.db = db_obj

    #Method to add a product from an order to the order line when it is made
    def add_line_item(self, order_id, prod_id, qty, price):
        try:

            #Insert a product from an order into the line
            self.db.get_cursor.execute(
                "INSERT INTO Orderline (order_id, prod_id, quantity, price) VALUES (?, ?, ?, ?)",
                (order_id, prod_id, qty, price)
            )
            self.db.get_connection.commit()
        except Exception as ex:
            print(f"Error adding line item for product {prod_id}: {ex}")