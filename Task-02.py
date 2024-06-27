def encrypt_image(path, key):
   
        # Open file for reading purpose
        with open(path, 'rb') as fin:
            image = fin.read()

        # Converting image into byte array to perform encryption easily on numeric data
        image = bytearray(image)

        # Performing XOR operation on each value of bytearray
        for index, values in enumerate(image):
            image[index] = values ^ key

        # Opening file for writing purpose
        with open(path, 'wb') as fin:
            # Writing encrypted data in image
            fin.write(image)

        print('Encryption Done...')



def decrypt_image(path, key):
   
        # Open file for reading purpose
        with open(path, 'rb') as fin:
            image = fin.read()

        # Converting image into byte array to perform decryption easily on numeric data
        image = bytearray(image)

        # Performing XOR operation on each value of bytearray
        for index, values in enumerate(image):
            image[index] = values ^ key

        # Opening file for writing purpose
        with open(path, 'wb') as fin:
            # Writing decrypted data in image
            fin.write(image)

        print('Decryption Done...')

    


def main():
    while True:
        # Take path of image as input
        path = input(r'Enter path of Image : ')

        # Taking key as input
        key = int(input('Enter Key for encryption/decryption of Image : '))

        # Asking user whether to encrypt or decrypt
        choice = input('Do you want to encrypt or decrypt the image? (e/d): ').lower()

        if choice == 'e':
            encrypt_image(path, key)
        elif choice == 'd':
            decrypt_image(path, key)
        else:
            print('Invalid choice! Please enter "e" for encryption or "d" for decryption.')

        # Asking user if they want to process another image
        another = input('Do you want to process another image? (y/n): ').lower()
        if another != 'y':
            break


if __name__ == "__main__":
    main()