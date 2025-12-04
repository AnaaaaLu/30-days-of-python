# 

text = input("Please enter a word or text: ").strip()

characterCount = len(text)
wordCount = len(text.split())

print(f"Character Count: {characterCount}")
print(f"Word Count: {wordCount}")