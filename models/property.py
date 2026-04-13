class Property:
    def __init__(self, id, address, suburb, price, bedrooms,
                 bathrooms, car_spaces, property_type, rental_income,
                 annual_expenses, yield_percentage, cashflow_monthly,
                 url, source, created_at, updated_at):
        self.id = id
        self.address = address
        self.suburb = suburb
        self.price = price
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.car_spaces = car_spaces
        self.property_type = property_type
        self.rental_income = rental_income
        self.annual_expenses = annual_expenses
        self.yield_percentage = yield_percentage
        self.cashflow_monthly = cashflow_monthly
        self.url = url
        self.source = source
        self.created_at = created_at
        self.updated_at = updated_at
