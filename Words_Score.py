## ----------------Words_Score-------------- ##


vowels = ["a","e","i","o","u","y"] ## Vowels We looking for in a each single word


def get_user_input():
    words_list = []
    words_list = input("Enter your sentence: ").lower().split()
    return words_list


def solve(List):
    words_score = 0 # The total score of the input
    for word in List : # loop through the list and get every word
        vowel_count = 0 
        for char in word: # loop through each word character by character  
            i = word.index(char) # get the index of that character
            if word[i] in vowels: # check if that caharacter in my vowels list...if it's a vowel then increment the vowel_count by one 
                vowel_count += 1 
        
        if vowel_count % 2 == 0: # if the vowel_count is even (the word has a even number of vowels)
            words_score += 2 # increment by two as its score should be 2
        else:
            words_score += 1 # otherwise the score of the word should be one

    return(words_score)            


def print_score(score):
    print(f"your words score is : {score}")



def main():
    while True:
        word_list = get_user_input()
        the_score = solve(word_list)
        print_score(the_score)
        
        another_round = input("Enter any for another round or (q/Q) to quit: ").lower()
        if another_round == "q":
           break

    print("End of the program")


if __name__ == "__main__":
    main()    