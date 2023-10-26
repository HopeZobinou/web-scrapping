import os

def search_word_in_file(file_path, word):
    file_name = os.path.basename(file_path)

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        text = file.read()
        word_count = len(text.split())
        word_frequency = text.count(word)
        return file_name, word_count, word_frequency

if __name__ == "__main__":
    #Path: "c:/Users/hopez/Documents/Data440/Homework3"

    folder_path = "c:/Users/hopez/Documents/Data440/Homework3/processed_html"
    word = 'iPhone'

    file_list = []
    word_count_list = []
    word_freq_list = []

    for root, dirs, files in os.walk(folder_path): #Loops through each file in the folder
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                result = search_word_in_file(file_path, word)
                if result[2] > 0:  # Only add files where the word is found
                    file_list.append(result[0])
                    word_count_list.append(result[1])
                    word_freq_list.append(result[2])

    for file_name, word_count, word_frequency in zip(file_list, word_count_list, word_freq_list):
        print(f"File: {file_name}, Word Count: {word_count}, Word Frequency: {word_frequency}")
    