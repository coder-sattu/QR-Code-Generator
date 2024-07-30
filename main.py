import qrcode
from PIL import Image  # Make sure you have Pillow installed for showing images

# Taking UPI ID as input
upi_id = input("Enter your UPI ID: ")

# Define the payment URL based on the UPI ID and the payment app
phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234&tid=1234567890&pid=1234567890&am=100&cu=INR&tn=Payment'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234&tid=1234567890&pid=1234567890&am=100&cu=INR&tn=Payment'
googlepay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234&tid=1234567890&pid=1234567890&am=100&cu=INR&tn=Payment'

# Create QR Codes for each payment app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
googlepay_qr = qrcode.make(googlepay_url)

# Save the QR codes to image files
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
googlepay_qr.save('googlepay_qr.png')

# Display the QR codes
phonepe_qr.show()
paytm_qr.show()
googlepay_qr.show()
