#!/usr/bin/python3
def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints its content to stdout.
    
    Args:
        filename (str): The name of the file to read. Default is an empty string.
    
    Examples:
        >>> with open("test_file.txt", "w", encoding="utf-8") as f:
        ...     _ = f.write("Hello, world!\n")
        >>> read_file("test_file.txt")
        Hello, world!
    """
    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line, end='')