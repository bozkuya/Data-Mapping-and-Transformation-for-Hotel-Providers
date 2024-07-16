class Category:
    def __init__(self, category_id, category_name):
        self.category_id = category_id
        self.category_name = category_name

class Chain:
    def __init__(self, chain_id, chain_name):
        self.chain_id = chain_id
        self.chain_name = chain_name

class Hotel:
    def __init__(self, hotel_id, hotel_name, category, chain, location):
        self.hotel_id = hotel_id
        self.hotel_name = hotel_name
        self.category = category
        self.chain = chain
        self.location = location