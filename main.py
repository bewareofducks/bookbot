def word_count(text):
    words = text.split() # splits the text into words
    length = len(words) # length = how many words are in text
    return(f"{length} words were found in the text") # returns the function to be used later



def char_count(text):
    lower_text = text.lower() # convert text to lowercase
    filtered_text = "" # creates new string that only holds letts

    for char in lower_text:
        if char.isalpha():
            filtered_text += char # adds only letters
            
    count = {}  # empty dictionary to hold counts

    char.list = []
    for char, num in count.items():
        
    
    for char in filtered_text: #loop through each character in text
        if char in count: # if character is already in dictionary
            count[char] += 1 # increment by 1
        else:
            count[char] = 1 # else, add it with a count of 1
    
    return count # returns the function to be used later

def main():
    with open("books/frankenstein.txt") as f: # opens and reads frankenstein.txt
        file_contents = f.read()
    print(word_count(file_contents)) 
    print(char_count(file_contents)) 

main()

    



