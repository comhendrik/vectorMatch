import sys
from vectorize import vectorize_and_save
from search import search_for_text
def menu():
    """Displays the main menu options."""
    print("\n--- Main Menu ---")
    print("1. Option 1: Vectorize()")
    print("2. Option 2: Search()")
    print("3. Exit")


def chunk_text(file_path, chunk_size=1024):
    """
    Reads a text file and chunks its content into manageable pieces.

    Parameters:
        file_path (str): The path to the text file.
        chunk_size (int): The size of each chunk in characters (default is 1024).

    Returns:
        list: A list of text chunks.
    """
    try:
        # Ensure the file is opened and closed properly with a context manager
        with open(file_path, 'r', encoding='utf-8') as file:
            # Read the entire file content
            content = file.read()

        # Chunk the content into specified sizes
        chunks = [content[i:i + chunk_size] for i in range(0, len(content), chunk_size)]
        return chunks

    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return []
    except IOError as e:
        print(f"Error: An I/O error occurred: {e}")
        return []

def vectorize():
    """Gets file name for chunking text"""
    file_path = input("\nInput file to vectorize: ").strip()
    print("Loading...")
    chunks = chunk_text(file_path)
    print("Finished chunking")
    print("Start embedding")
    vectorize_and_save(chunks)



def search():
    """Displays some example information."""
    text = input("\nInput to search for similar vector entries: ").strip()
    search_for_text(text)


def perform_calculation():
    """Performs a simple calculation."""
    try:
        num1 = float(input("\nEnter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 + num2
        print(f"The result of adding {num1} and {num2} is {result}.")
    except ValueError:
        print("Invalid input! Please enter numeric values.")


def main():
    while True:
        menu()
        try:
            choice = input("\nSelect an option (1-3): ").strip()

            if choice == "1":
                vectorize()
            elif choice == "2":
                search()
            elif choice == "3":
                print("\nExiting the program. Goodbye!")
                sys.exit()
            else:
                print("\nInvalid choice! Please select a valid option.")
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Exiting.")
            sys.exit()


if __name__ == "__main__":
    main()
