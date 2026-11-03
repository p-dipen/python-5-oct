# Positional and keyword arguments
from pydantic import validate_call

@validate_call
def nPrintln(message: str, n: int):
    """Print a message a specific number of times.

    Args:
        message (str): the text or content to print
        n (int): the number of times
    """
    for i in range(n):
        print(message)

nPrintln( 4, 'a')