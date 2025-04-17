def count_words(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read().lower()  

        words = text.split()  
        word_count = {}

        for word in words:
            word = word.strip(",.?!;:()[]{}\"'")  
            if word:
                word_count[word] = word_count.get(word, 0) + 1

        sorted_words = sorted(word_count.items())

        print("\nWord Count:")
        for word, count in sorted_words:
            print(f"{word}: {count}")

    except FileNotFoundError:
        print("Error: File not found. Please check the filename.")
    except Exception as e:
        print("An error occurred:", e)

filename = input("Enter the file name: ")
count_words(filename)