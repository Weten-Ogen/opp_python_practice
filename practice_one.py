class CreditCard:
    """A cosumer credit card."""
    
    def __init__(self, customer, bank, acnt, limit):
        """Create a new instance of the class.
            
            The initial balance
            
            customer--> the name of the customer
            bank  --> the name of the bank
            acnt -->  the account identifier
            limit --> credit limit (measured in dollars)
        """
        
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self.limit = limit
        self.balance = 0
        
    def get_customer(self):
            """Return name of the customer."""
            return self._customer
        
    def get_bank(self):
            