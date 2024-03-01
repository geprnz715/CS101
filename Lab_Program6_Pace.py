# returns count words separated by a space
def word_count(text):
    return len(text.split())

# returns longest word in given input
def find_longest_word(text):
    words = text.split()
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

# returns number of occurences of substring in text
def count_substring(text, substring):
    count = text.count(substring)
    return count

# returns a list of each word in input w/o multiples
def extract_unique_words(text):
    words = text.split()
    list = []
    for word in words:
        if not word in list: list.append(word)
    return list

# runs main program loop
def main():
    from sys import exit
    import time
    # processes that occur only on startup
    print('Welcome to the Text Processing Program!\n')
    text = input('Enter a text: ')
    print(f'\nOriginal Text:\n{text}\n')

    #processes that occur until user exits; text manipulation
    while True:
        print('Text Analysis Options:\n1. Word Count\n2. Longest Word\n3. \
Count of Substring\n4. Unique Words\n5. Exit\n')
        choice = int(input('Enter the number of the analysis option (1-5): '))
        print()
        if choice == 1:
            print(f'Word Count: {word_count(text)}\n')
        elif choice == 2:
            print(f'Longest Word: {find_longest_word(text)}\n')
        elif choice == 3:
            sub = str(input('Enter a substring to count: '))
            print(f'Count of Substring: {count_substring(text, sub)}\n')
        elif choice == 4:
            print(f'Unique Words: {extract_unique_words(text)}\n')
        elif choice == 5:
            print('Thank you for using the Text Processing Program!')
            time.sleep(2)
            exit()
        else:
            print('Invalid option, enter a digit (1-5).\n')

if __name__ == '__main__':
    main()
