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
    """Retrieves data based on query and answer with a combining the query, data and a llm"""
    text = input("\nQuery: ").strip()
    search_for_text(text)


def main():

    # Load environment variables from the .env file
    load_dotenv()

    # Defining the text in a 3D-like style using spacing
    text_lines = [
        "",
        "",
        "",
        "",
        " V   V  EEEEE  CCCC  TTTTT   OOO   RRRR    M   M  AAAAA  TTTTT  CCCC  H   H",
        "  V V   E      C       T    O   O  R   R   MM MM  A   A    T   C      H   H",
        "   V    EEEE   C       T    O   O  RRRR    M M M  AAAAA    T   C      HHHHH",
        "  V V   E      C       T    O   O  R  R    M   M  A   A    T   C      H   H",
        " V   V  EEEEE  CCCC    T     OOO   R   R   M   M  A   A    T   CCCC   H   H"
        "",
        "",
        "",
        "",
    ]

    # Loop to simulate 3D printing with varying spaces for the depth illusion
    print("\033[H\033[J", end="")
    # Print the text with increasing spaces for depth effect
    for line in text_lines:
        print(" " + line)




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
