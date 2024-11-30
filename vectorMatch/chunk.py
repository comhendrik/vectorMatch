def chunk_text(file_path, chunk_size=50):
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