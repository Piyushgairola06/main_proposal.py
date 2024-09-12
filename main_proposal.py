import time

def print_with_delay(message, delay=0.5):
    """Prints a message with a delay to simulate typing."""
    for char in message:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # New line

def proposal():
    print_with_delay("Hi [Crush's Name],")
    time.sleep(1)
    print_with_delay("I've been thinking a lot about us lately...")
    time.sleep(2)
    print_with_delay("There's something I need to ask you.")
    time.sleep(1)
    print_with_delay("Would you make me the happiest person in the world and be my partner?")
    time.sleep(2)
    print_with_delay("I promise to always be there for you and make you smile every day.")
    time.sleep(2)
    print_with_delay("So, what do you say? Will you be mine?")

if __name__ == "__main__":
    proposal()
