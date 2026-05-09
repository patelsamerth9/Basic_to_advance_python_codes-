import qrcode
import os
def generate_qr():
    data = input("Enter the website URL or text for the QR code: ")
    filename = input("Enter filename to save (e.g., my_code.png): ")
    if not filename.endswith('.png'):
        filename += '.png'
    qr = qrcode.QRCode(
        version=1, 
        error_correction=qrcode.constants.ERROR_CORRECT_H, 
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"Success! QR code saved as '{filename}'")
if __name__ == "__main__":
    generate_qr()
