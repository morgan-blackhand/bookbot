def main():
    # File path for the book
    file_path = "frankenstein.txt"
    
    # Read the book contents
    with open(file_path, "r") as f:
        book_text = f.read()
    
    # Count the words in the book
    word_count = count_words(book_text)
    print(f"The book contains {word_count} words.")
    
    # Count characters in the book
    character_count = count_characters(book_text)
    print("Character frequencies:")
    for char, count in character_count.items():
        print(f"'{char}': {count}")

# Function to count words in a string
def count_words(text):
    # Split the text into words and return the length of the resulting list
    words = text.split()
    return len(words)

# Function to count character occurrences in a string
def count_characters(text):
    # Convert text to lowercase
    text = text.lower()
    
    # Initialize a dictionary to store character counts
    char_count = {}
    
    # Loop through each character in the text
    for char in text:
        # Only count alphabetic characters (optional: add more conditions for digits or punctuation)
        if char.isalpha():  # To count only letters
            char_count[char] = char_count.get(char, 0) + 1
    
    return char_count

if __name__ == "__main__":
    main()
