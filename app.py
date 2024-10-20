import qrcode

def generate_qr(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.show()
    img.save("qr_code.png")

def main():
    print("QR Code Generator")
    print("1. Generate QR Code for a URL")
    print("2. Generate QR Code for text")

    choice = input("Please choose an option (1 or 2): ")

    if choice == "1":
        url = input("Enter the URL: ")
        generate_qr(url)
        print("QR code for the URL has been generated and saved as 'qr_code.png'.")
    elif choice == "2":
        text = input("Enter the text: ")
        generate_qr(text)
        print("QR code for the text has been generated and saved as 'qr_code.png'.")
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()
