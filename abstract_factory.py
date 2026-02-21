from abc import ABC, abstractmethod
class paymentgateway(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass



class PayPalGateway(paymentgateway):
    def process_payment(self, amount):
        print(f"Processing payment of {amount} through PayPal.")
    
class StripeGateway(paymentgateway):
    def process_payment(self, amount):
        print(f"Processing payment of {amount} through Stripe.")


class PaytmGateway(paymentgateway):
    def process_payment(self, amount):
        print(f"Processing payment of {amount} through Paytm.")

class RazorpayGateway(paymentgateway):
    def process_payment(self, amount):
        print(f"Processing payment of {amount} through Razorpay.")

class invoice(ABC):
    @abstractmethod
    def generate_invoice(self, amount):
        pass

class PDFInvoice(invoice):
    def generate_invoice(self, amount):
        print(f"Generating PDF invoice for {amount}.")

class GstInvoice(invoice):
    def generate_invoice(self, amount):
        print(f"Generating GST invoice for {amount}.")


class PaymentGatewayFactory:
    @staticmethod
    def create_gateway(gateway_type):
        if gateway_type == "paypal":
            return PayPalGateway()
        elif gateway_type == "stripe":
            return StripeGateway()
        else:
            raise ValueError("Invalid payment gateway type.")

# Usage
class processor(ABC):
    @abstractmethod
    def process(self, amount):
        pass

class IndianPaymentProcessor(processor):
    def __init__(self, gateway_type):
        self.gateway = PaymentGatewayFactory.create_gateway(gateway_type)
        self.invoice_processor = invoiceprocessor("gst")


    def process(self, amount):
        self.gateway.process_payment(amount)
        self.invoice_processor.generate(amount)

class USPaymentProcessor(processor):
    def __init__(self, gateway_type):
        self.gateway = PaymentGatewayFactory.create_gateway(gateway_type)
        self.invoice_processor = invoiceprocessor("pdf")

    def process(self, amount):
        self.gateway.process_payment(amount)
        self.invoice_processor.generate(amount)
        
class invoicefactory:
    @staticmethod
    def create_invoice(invoice_type):
        if invoice_type == "pdf":
            return PDFInvoice()
        elif invoice_type == "gst":
            return GstInvoice()
        else:
            raise ValueError("Invalid invoice type.")

class invoiceprocessor:
    def __init__(self, invoice_type):
        self.invoice = invoicefactory.create_invoice(invoice_type)

    def generate(self, amount):
        self.invoice.generate_invoice(amount)


class PaymentProcessor:
    def __init__(self, gateway_type):
        self.gateway = PaymentGatewayFactory.create_gateway(gateway_type)

    def process(self, amount):
        self.gateway.process_payment(amount)


# Example usage
payment_processor = PaymentProcessor("paypal")
payment_processor.process(100)
invoice_processor = invoiceprocessor("pdf")
invoice_processor.generate(100)
