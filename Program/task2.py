Sentence = str.lower(input("Enter a sentence: "))

# Requests user input with the following text "Enter a sentence: "
# Converts input into lowercase (if applicable) through the string class using method lower()
# Stores this converted input into variable Sentence
 

Words = Sentence.split()
# Variable words is a instance of sentence but into split list e.g. ["Hello", "Word"]
Count = len(Words)
# Count is the total length of the setence (if there a space it dosnt count it)
Length = 0
# Length is set to 0 (default value)
Longest_Word = ""
# Longestword is set to "" (default value)

for word in Words:
    # using a foor loop to check through the entire of the list Words
    Length = Length + len(word)
    # We are adding the length of each word into variable Length
    if len(word) > len(Longest_Word):
        # Using a if statement, we check if the length of the current word in loop
        # is greater than the longest word, this run continously through each word
        # in the setence and sets it if its the longest word
        Longest_Word = word 



Average = 0
# Now I put the variable Average to make global

if Count > 0:
    # I check for if the user has inputted atleast one word before i calculate the average
    # I calculate the average using the length of each word devided by the total words
    Average = Length / Count


print("Word Count:", Count )

print("Average Word Count:", round(Average, 2) )

print("Longest Word:", Longest_Word )

# I print the word count, average word count and longest word
# When am printing the average word count, i use the method round() to round to 2 decimals



