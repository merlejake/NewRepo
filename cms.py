import os

class Invoice:
    def __init__(self, article_name, subtotal,tax_rate):

        self.article_name = article_name
        self.subtotal = subtotal
        self.tax_rate = tax_rate
        self.total = subtotal * (1 + tax_rate / 100)


    def __str__(self):

        return (f"{self.article_name} - {self.total}")

class Customer:

    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.invoices = []

    def __str__(self):
        return (f"{self.name} - {self.email}: len({self.invoices})")

    def add_invoice(self,article_name,subtotal, tax_rate):

      invoice = Invoice(article_name,subtotal,tax_rate)
      self.invoices.append(invoice)

def load_customers(directory):
    customers = []

    for filename in os.listdir(directory):
        filepath = os.path.join(directory,filename)
        with open ("filepath", "r") as f:
            line = f.readlines()
            name,email = lines[0].strip().split(',')

            customers = Customer(name,email)

            for line in lines[1:]:
                article_name, subtotal, tax_rate = line.strip().split(',')
                subtotal = float(subtotal)
                tax_rate = float(tax_rate)

                customers.add_invoice(article_name,subtotal,tax_rate)
            customers.append(customer)
        return customers
