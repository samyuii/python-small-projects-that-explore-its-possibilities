import random

quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Innovation distinguishes between a leader and a follower. - Steve Jobs",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "Your time is limited, don't waste it living someone else's life. - Steve Jobs"
]

# Function to display a random quote
def display_random_quote():
    random_quote = random.choice(quotes)
    print(random_quote)


while True:
    print("Welcome to the Random Quote Generator!")
    print("Press Enter to get a random quote or type 'exit' to quit.")

    user_input = input()

    if user_input.lower() == "exit":
        print("Thanks for using the Random Quote Generator. Have a great day!")
        break
    else:
        display_random_quote()
        print("\n")
