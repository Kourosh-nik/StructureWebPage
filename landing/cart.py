from decimal import Decimal

CART_SESSION_ID = 'cart'

class Cart:
    def __init__(self, request):
        self.session = request.session

        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}

        self.cart = cart
        self.cart_length = 0

    @property
    def project_ids(self):
        # return list(self.cart.keys())
        return self.cart.keys()

    @property
    def get_total_price(self):
            return sum(int(item['price']) * item['quantity'] for item in self.cart.values())

    def __getitem__(self, item):
        return self.cart[item]

    def __iter__(self):
        for item in self.cart.values():
            yield item

    def update_cart_length(self):
        """Calculate the total number of items in the cart."""
        self.cart_length = sum(item['quantity'] for item in self.cart.values())

    def add(self, project_id, project_price, quantity, update):
        if project_id not in self.cart:
            self.cart[project_id] = {
                'project_id':project_id,
                'quantity': 0,
                'price': project_price
            }

        if update:
            self.cart[project_id]['quantity'] = quantity
        else:
            self.cart[project_id]['quantity'] += quantity

        self.__save()

    def remove(self, project_id):
        if project_id in self.cart:
            del self.cart[project_id]
            self.__save()

    def __save(self):
        self.session[CART_SESSION_ID] = self.cart
        self.session.modified = True

    def clear(self):
        self.session[CART_SESSION_ID] = {}
        self.session.modified = True