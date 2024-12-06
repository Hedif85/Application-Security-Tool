import hashlib

def hash_file(filename):
    """Generate SHA256 hash of a file."""
    try:
        with open(filename, "rb") as file:
            file_data = file.read()
            sha256_hash = hashlib.sha256(file_data).hexdigest()
            print(f"SHA256 Hash of {filename}: {sha256_hash}")
    except FileNotFoundError:
        print(f"Error: File {filename} not found!")

# Ask user for a file to hash
file_to_check = input("Enter the file path to check its hash: ")
hash_file(file_to_check)


