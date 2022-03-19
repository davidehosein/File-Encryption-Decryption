import os # For interacting with the operating system e.g. checking if a file exists, joining directories etc.
import sys # For exiting the program.

from cryptography.fernet import Fernet # For encrypting and decrypting files using a key.
from cryptography.fernet import InvalidToken # For displaying an error message if the key is invalid.

class FileEncryptionDecryption:
    '''Class containing functionality for encrypting and decrypting files.'''

    def generate_key(self, keyfile_path):
        '''Generates the key and save it to a file.'''
        self.key = Fernet.generate_key() # Generates a key for encrypting and decrypting a file.

        with open(keyfile_path, 'wb') as f: # Creates a file in write-binary mode.
            f.write(self.key) # Writes the key to the file.

        # Displays a message that the key is successfully generated and stored in the "key" directory.
        print(f'\n"{self.keyfile_name}" is successfully generated and stored in the "key" directory.')
        # Displays a message to keep the key file in a safe location, since this is the ONLY key that can be used for decryption.
        print(f'Please keep "{self.keyfile_name}" safely, as this is the ONLY key that can be used to decrypt the file.\n')

    def load_key(self, keyfile_path):
        '''Loads the key from the key file.'''
        with open(keyfile_path, 'rb') as f: # Opens the key file in read-binary mode.
            key = f.read() # Reads the key from the key file.
            return key # Returns the key.

    def create_path_of_keyfile(self):
        '''Creates a relative path to store the key file.'''
        while True: # Creates an infinite loop.
            # Prompts the user to enter the name of the key file.
            self.keyfile_name = input('What would you like to name the key file (with the ".key" extension): ')
            # Joins the "key" directory to the name of the key file, to create the relative path of the key file.
            keyfile_path = os.path.join('key', self.keyfile_name)  

            if keyfile_path.endswith('.key'): # Checks if the path of the key file ends with the ".key" extension.
                if os.path.exists(keyfile_path): # Checks if the path of the key file exist.
                    print(f'"{self.keyfile_name}" already exists.\n') # Displays a message stating that the key file already exist.

                    while True: # Creates an infinite loop.
                        # Prompts the user if to overwrite the key file.
                        replace_key = input(f'Would you like to overwrite "{self.keyfile_name}" (y/n)? ') 
                        if replace_key.lower() == 'y': # Converts the input into lowercase and checks if the value is "y".       
                            print(f'Overwriting "{self.keyfile_name}"') 
                            return keyfile_path # Returns the path of the key file.
                        elif replace_key.lower() == 'n': # Converts the input into lowercase and checks if the  value is "n".
                            print('Please enter another name for the key.\n') # Displays a message to enter another name for the key.
                            # Invokes the current method to prompt the user to re-enter the name of the key file.
                            self.create_path_of_keyfile() 
                        else:
                            print('Invalid value. Please try again.\n') # Displays a message if the user did not enter "y" or "n".
                else:
                    return keyfile_path # Returns the path of the key file.
            else:
                # Displays a message that the name of the key file does not end with the ".key" extension.
                print(f'"{self.keyfile_name}" does not end with the ".key" extension.\n')

    def create_path_of_encrypted_file(self):
        '''Creates a relative path to store the encrypted file.'''
        names = self.filename.split('.') # Splits the filename into its name and extension(s), and store the results in a list.

        # Creates the total extension for the encrypted file.
        if len(names) > 1: # Checks if the "names" list contain more than 1 item.
            extensions = names[1:] # Returns the second item until the last item in the "names" list.
            full_extension = '' # Empty string to store the full extension of the encrypted file.
            for extension in extensions: # Loops through the "extensions" list.
                full_extension += f'.{extension}' # Concatenates the current extension to the "full_extension" string.
            full_extension += '.encrypted' # Concatenates the ".encrypted" extension to the end of the "full_extension" string.
        else:
            # Displays a message that the entered filename is not a file, and that only files can be encrypted.
            print(f'"{self.filename}" is NOT a file. You can only encrypt files and NOT directories.\n')
            self.start() # Restarts the program.
            
        while True: # Creates an infinite loop.
            # Prompts the user to enter the name of the encrypted file.
            self.encrypted_filename = input(f'What would you like to name the encrypted file (with the "{full_extension}" extension): ')
            # Joins the "encrypted" directory to the name of the encrypted file, to create the relative path of the encrypted file.
            encrypted_filepath = os.path.join('encrypted', self.encrypted_filename)  

            if encrypted_filepath.endswith(full_extension): # Checks if the the path of the encrypted file ends with the extension.
                if os.path.exists(encrypted_filepath): # Checks if the path of the encrypted file exist.
                    print(f'"{self.encrypted_filename}" already exists.\n') # Displays a message that the encrypted file already exist.

                    while True: # Creates an infinite loop.
                        # Prompts the user to overwrite the encrypted file.
                        replace_encrypted_file = input(f'Would you like to overwrite {self.encrypted_filename} (y/n)? ') 
                        if replace_encrypted_file.lower() == 'y': # Converts the input into lowercase and checks if the value is "y".
                            print(f'Overwriting "{self.encrypted_filename}"\n')        
                            return encrypted_filepath # Returns the path of the encrypted file.
                        elif replace_encrypted_file.lower() == 'n': # Converts the input into lowercase and checks if the  value is "n".
                            # Displays a message to enter another name for the encrypted file.
                            print('Please enter another name for the encrypted file.\n') 
                            # Invokes the current method to prompt the user to re-enter the name of the encrypted file.
                            self.create_path_of_encrypted_file() 
                        else:
                            print('Invalid value. Please try again.\n') # Displays a message if the user did not enter "y" or "n".
                else:
                    return encrypted_filepath # Returns the path of the encrypted file.
            else:
                # Displays a message that the name of the encrypted file does not end with the extension.
                print(f'"{self.encrypted_filename}" does not end with the "{full_extension}" extension.\n')
        
    def get_path_of_key_file(self):
        '''Returns the relative path of the key file.'''
        while True: # Creates an infinite loop.
            # Prompts the user to enter the name of the key file in the "key" directory.
            self.keyfile_name = input('Enter the name of the key file (with the ".key" extension): ')
            # Joins the "key" directory to the name of the key file, to create the relative path of the key file.
            keyfile_path = os.path.join('key', self.keyfile_name)

            if keyfile_path.endswith('.key'): # Checks if the path of the key file ends with the ".key" extension.
                if os.path.exists(keyfile_path): # Checks if the path of the key file exist.
                    return keyfile_path # Returns the path of the key file.
                else:
                    # Displays a message that the key file does not exist.
                    print(f'"{self.keyfile_name}" does not exist. Please ensure that the key is present in the "keys" directory.\n')  
            else:
                # Displays a message that the name of the key file does not end with the ".key" extension.
                print(f'"{self.keyfile_name}" does not end with the ".key" extension.\n') 
            
    def get_path_of_encrypted_file(self):
        '''Returns the relative path of the encrypted file.'''
        while True: # Creates an infinite loop.
            # Prompts the user to enter the name of the encrypted file in the "encrypted" directory.
            self.encrypted_filename = input('Enter the name of the encrypted file (with the ".encrypted") extension: ' )
            # Joins the "encrypted" directory to the name of the encrypted file, to create the relative path of the encrypted file.
            encrypted_filepath = os.path.join('encrypted', self.encrypted_filename)

            if encrypted_filepath.endswith('.encrypted'): # Checks if the path to the encrypted file ends with the ".encrypted" extension.
                if os.path.exists(encrypted_filepath): # Checks if the path of the encrypted file exist.
                      return encrypted_filepath # Returns the path of the encrypted file.
                else:
                    # Displays a message that the encrypted file does not exist.
                    print(f'"{self.encrypted_filename}" does not exist. Please ensure that the encrypted file is present in the "encrypted" directory.\n')
            else:
                # Displays a message that the name of the encrypted file does not end with the ".encrypted" extension.
                print(f'"{self.encrypted_filename}" does not end with the ".encrypted" extension.\n')

    def get_path_of_file(self):
        '''Returns the relative path of the file to be encrypted.'''
        while True: # Creates an infinite loop.
            # Prompts the user to enter the name of the file to be encrypted in the "file" directory.
            self.filename = input('Enter the name of the file to be encrypted (with extension): ')

            # Joins the "file" directory to the name of the file to create a relative path of the file.
            filepath = os.path.join('file', self.filename)

            if os.path.exists(filepath): # Checks if the path of the file to be encrypted exist.
                # Checks if the input is a file, and NOT a directory.
                names = self.filename.split('.') # Splits the filename into its name and extension(s), and store the results in a list.
                if len(names) > 1: # Checks if the "names" list contain more than 1 item.
                    return filepath # Returns the path of the file to be encrypted.
                else:
                    # Displays a message that the entered filename is not a file, and that only files can be encrypted.
                    print(f'"{self.filename}" is NOT a file. You can only encrypt files and NOT directories.\n')
            else:
                # Displays a message that the file to be encrypted does not exist.
                print(f'"{self.filename}" does not exist. Please ensure that the file to be encrypted is present in the "files" directory.\n')
           
    def get_path_of_decrypted_file(self, ):
        '''Returns the relative path of the decrypted file.'''
        # Removes the ".encrypted" extension from the name of the encrypted file.
        self.decrypted_filename = self.encrypted_filename.replace('.encrypted', '') 

        names = self.decrypted_filename.split('.') # Splits the filename into its name and extension(s), and store the results in a list.
        # Creates the total extension for the decrypted file.
        if len(names) > 1: # Checks if the "names" list contain more than 1 item.
            extensions = names[1:] # Returns the second item until the last item in the "names" list.
            full_extension = '' # Empty string to store the full extension of the encrypted file.
            for extension in extensions: # Loops through the "extensions" list.
                full_extension += f'.{extension}' # Concatenates the current extension to the "full_extension" string.
        else:
            # Display a message that the encrypted item is not a file, and that only files can be encrypted.
            print(f'"{self.encrypted_filename}" is NOT a file. You can only encrypt files and NOT directories.\n')
            self.start() # Restart the program.

        while True:
            # Prompt the user to enter the name of the decrypted file.
            self.decrypted_filename = input(f'What would you like to name the decrypted file (with the "{full_extension}" extension)? ')
            # Joins the "decrypted" directory to the name of the decrypted file, to create the relative path of the decrypted file.
            decrypted_filepath = os.path.join("decrypted", self.decrypted_filename)

            if self.decrypted_filename.endswith(full_extension): # Checks if the decrypted filename ends with the extension.
                if os.path.exists(decrypted_filepath): # Checks if the path of the decrypted file exist.
                    print(f'"{self.decrypted_filename}" already exists.') # Displays a message that the decrypted file already exist.
                    while True: # Creates an infinite loop.
                        # Prompts the user if to overwrite the decrypted file.
                        replace_decrypted_file = input('Would you like to overwrite the decrypted file (y/n)? ') 
                        if replace_decrypted_file.lower() == 'y': # Converts the input into lowercase and checks if the value is "y".
                            print(f'Overwriting "{self.decrypted_filename}"\n')        
                            return decrypted_filepath # Returns the path of the decrypted file.
                        elif replace_decrypted_file.lower() == 'n': # Converts the input into lowercase and checks if the  value is "n".
                            while True:
                                # Prompt the user to enter the new name of the decrypted file with its extension.
                                new_decrypted_filename = input(f'What would you like to name the decrypted file (with the "{full_extension}" extension)? ')
                                # Joins the "decrypted" directory to the name of the decrypted file, to create the relative path of the decrypted file.
                                new_decrypted_filepath = os.path.join('decrypted', new_decrypted_filename) 

                                # Checks if the new decrypted file name and the previous decrypted filename does not match.
                                if new_decrypted_filepath != decrypted_filepath:
                                    if new_decrypted_filename.endswith(full_extension): # Checks if the new decrypted filename ends with the extension.
                                        self.decrypted_filename = new_decrypted_filename # Assigns the name of the decrypted file to the new name of the decrypted file.
                                        return new_decrypted_filepath # Returns the relative path of the decrypted file.
                                    else:
                                        # Displays a message that the new decrypted filename does not end with the extension.
                                        print(f'"{new_decrypted_filename}" does not end with "{full_extension}". Please try again.\n')
                                else:
                                    # Displays a message that the new name of the decrypted file cannot be the same as the old name of the decrypted file.
                                    print('The new name of the decrypted file CANNOT be the same as the old name of the decrypted file.\n')
                        else:
                            print('Invalid value. Please try again.\n') # Displays a message if the user did not enter "y" or "n".
                else:
                    return decrypted_filepath # Returns the relative path of the decrypted file.
            else:
                # Displays a message that the name of the decrypted file does not end with the extension.
                print(f'"{self.decrypted_filename}" does not end with the "{full_extension}" extension.\n')


    def display_encryption_instructions(self):
        '''Displays the instructions for encrypting a file.'''
        print('\nINSTRUCTIONS TO ENCRYPT FILE:')
        print('1. Place the file to be encrypted in the "file" directory.')
        print('2. Enter the name for the key file. The key will be generated and stored in the "key" directory.')
        print('3. Enter the name of the file to be encrypted. Ensure that this file is present in the "file" directory.')
        print('4. The file will be encrypted and stored in the "encrypted" directory.')
        print('NOTE: Do NOT lose the key file, as this is the ONLY key that can be used to decrypt the file.\n')

    def display_decryption_instructions(self):
        '''Displays the instructions for decrypting a file.'''
        print('\nINSTRUCTIONS TO DECRYPT FILE:')
        print('1. Place the encrypted file in the "encrypted" directory.')
        print('2. Place the key file in the "key" directory.')
        print('3. Enter the name of the key file to be used for decrypting the file.')
        print('4. Enter the name of the encrypted file in the "encrypted" directory.')
        print('5. The file will be decrypted and stored in the "decrypted" directory.')
        print('NOTE: Do NOT lose the key file, as this is the ONLY key that can be used to decrypt the file.\n')

    def encrypt_file(self):
        '''Encrypts the file, and store the encrypted file in the "encrypted" directory.'''
        self.keyfile_path = self.create_path_of_keyfile() # Obtains the relative path of where to store the key file.
        self.generate_key(self.keyfile_path) # Generates the key file using the path of the key, and store it in a file.
        self.fernet = Fernet(self.key) # Creates a "Fernet" object for encryption/decryption. 
        self.filepath = self.get_path_of_file() # Obtains the relative path of the file to be encrypted.
        self.encrypted_filepath = self.create_path_of_encrypted_file() # Creates the path of the encrypted file.

        try:
            with open(self.filepath, 'rb') as f: # Opens the file to be encrypted in read-binary mode.
                data = f.read() # Reads the contents of the encrypted file.
        except FileNotFoundError:
            # Displays an error message if the path of the file to be encrypted does not exist.
            print(f'"{self.filepath}" does not exist.\n')
            self.start() # Restarts the program.
        except:
            print('Some other error occured.\n') # Displays an error message if some other error occured.
            self.start() # Restarts the program.

        print(f'Encrypting "{self.filename}"') # Displays a message that the file is being encrypted.
        encrypted_data = self.fernet.encrypt(data) # Encrypts the data.

        with open(self.encrypted_filepath, 'wb') as f: # Creates the encrypted file in write-binary mode.
            f.write(encrypted_data) # Writes the content to the encrypted file.

        # Displays a message that the file was successfully encrypted and that the encrypted file is stored in the "encrypted" directory.
        print(f'"{self.filename}" is successfully encrypted. The encrypted file "{self.encrypted_filename}" is stored in the "encrypted" directory.\n') 

    def decrypt_file(self):
        '''Decrypts the encrypted file, and store the decrypted file in the "decrypted" direcrtory.'''
        self.keyfile_path = self.get_path_of_key_file() # Obtains the relative path of the key file.
        self.key = self.load_key(self.keyfile_path) # Reads the contents of the key file.
        self.fernet = Fernet(self.key) # Creates a "Fernet" object for encryption/decryption.
        self.encrypted_file_path = self.get_path_of_encrypted_file() # Obtains the relative path of the encrypted file.
        self.decrypted_file_path = self.get_path_of_decrypted_file() # Obtains the relative path of the decrypted file.

        try:
            with open(self.encrypted_file_path, 'rb') as f: # Opens the encrypted file in read-binary mode:
                encrypted_data = f.read() # Reads the contents of the encrypted file.
        except FileNotFoundError:
            # Display a message the the encrypted file does not exist.
            print(f'"{self.encrypted_file_path}" does not exist.\n') 
            self.start() # Restarts the program.
        except:
            print('Some other error occured.\n') # Displays an error message if some other error occured.
            self.start() # Restarts the program.

        try:
            print(f'Decrypting "{self.encrypted_filename}"') # Displays a message that the file is being decrypted.
            decrypted_data = self.fernet.decrypt(encrypted_data) # Decrypts the encrypted data.
            
            with open(self.decrypted_file_path, 'wb') as f: # Creates the decrypted file in write-binary mode.
                f.write(decrypted_data) # Writes the contents to the decrypted file.

            # Displays a message the the file is successfulyl decrypted and that the decrypted file is stored in the "decrypted" directory.
            print(f'"{self.encrypted_filename}" is succesfully decrypted. The decrypted file "{self.decrypted_filename}" is stored in the "decrypted" directory.\n')
        except InvalidToken:
            # Displays an error message if the decryption key is invalid.
            print(f'"{self.keyfile_name}" is invalid. Please ensure that the key is valid for decryption.\n')
            self.start() # Restarts the program.
        # except:
        #     print('Some other error occured.\n') # Displays an error message if some other error occured.
        #     self.start() # Restarts the program.

    def start(self):
        '''Starts the program.'''
        while True: # Creates an infinite loop.
            # Prompts the user to select if they would like to encrypt or decrypt a file.
            choice = input('Would you like to (E)ncrypt or (D)ecrypt a file? (Enter \"Q\" to exit the program.): ') 
            if choice.lower() == 'e': # Converts the user input into lowercase and checks if the value is "e".
                self.display_encryption_instructions() # Displays the instructions for encrypting a file.
                self.encrypt_file() # Invokes the "encrypt_file" method for encrypting the file.
            elif choice.lower() == 'd': # Converts the user input to lowercase and checks if the value is "d".
                self.display_decryption_instructions() # Displays the instructions for decrypting a file.
                self.decrypt_file() # Invokes the "decrypt_file" method for decrypting the file.
            elif choice.lower() == 'q': # Converts the user input to lowercase and checks if the value is "n".
                print('Program terminated...\n') # Displays a message that the program is terminated.
                sys.exit() # Terminates the program.
            else:
                # Displays a message that the input is an invalid value.
                print('Invalid value. Please try again.\n') 


if __name__ == '__main__':
    file_encrypter_decrypter = FileEncryptionDecryption() # Creates a "FileEncryptionDecryption" object.
    file_encrypter_decrypter.start() # Starts the encryption/decryption program.