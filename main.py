import sys
from vectorize import vectorize_and_save
from search import search_for_text
from chunk import chunk_text
from dotenv import load_dotenv


def menu():
    """Displays the main menu options."""
    print("\n--- Main Menu ---")
    print("1. Option 1: Vectorize()")
    print("2. Option 2: Search()")
    print("3. Exit")


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
    # Load environment variables from the .env file
    load_dotenv()
    main()
