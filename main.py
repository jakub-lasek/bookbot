def main():
    with open("./books/frankenstein.txt") as f:
        file_content = f.read()
        words_count = count_words(file_content)
        letter_apperances = get_letters_apperances(file_content)
        sorted_count = get_letters_count_sorted(letter_apperances)
        get_letters_report(sorted_count)

def count_words(book_text):
    return len(book_text.split())

def get_letters_apperances(book_text):
    letters = {}

    for letter in book_text:
        if letter.isalpha():
            lower_case_letter = letter.lower()
            letter_count = letters.get(lower_case_letter)
            letters[lower_case_letter] = letter_count + 1 if letter_count != None else 1

    return letters

def get_letters_report(sorted_letters):
    for letter_count in sorted_letters:
        print(f"The '{letter_count["letter"]}' chracter was found {letter_count["count"]} times")

def sort_on(dict):
    return dict["count"];

def get_letters_count_sorted(letters_count):
    list_of_dicts = []

    for letter in letters_count:
        list_of_dicts.append({"letter": letter, "count": letters_count[letter]})


    list_of_dicts.sort(reverse=True, key=sort_on)

    return list_of_dicts


main()
