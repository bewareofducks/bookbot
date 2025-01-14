def word_count(text):
    words = text.split() # splits the text into words
    return len(words) 
    



def char_count(text):
    lower_text = text.lower() # convert text to lowercase
    filtered_text = "" # creates new string that only holds letts

    for char in lower_text:
        if char.isalpha():
            filtered_text += char # adds only letters
            
    count = {}  # empty dictionary to hold counts

    for char in filtered_text: #loop through each character in text
        if char in count: # if character is already in dictionary
            count[char] += 1 # increment by 1
        else:
            count[char] = 1 # else, add it with a count of 1
    
    # converting to list of dictionaries
    char_list = []  # new list to hold dictionaries
    for char, num in count.items():
        char_dict = {"char": char, "num": num}  # create dictionary for this character
        char_list.append(char_dict)  # add it to the list

    def sort_on(dict):
        return dict["num"]

    char_list.sort(reverse=True, key=sort_on)

    return char_list

def main():
    with open("books/frankenstein.txt") as f: # opens and reads frankenstein.txt
        file_contents = f.read()

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count(file_contents)} words found in the document\n") 


    char_list = char_count(file_contents)
    for char_dict in char_list:
          print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")
    
    print("--- End report ---")

main()

    



