class Flashcards:
    def __init__(self):
        self.vocab = {"hello": "hola", "goodbye": "adiós", "thank you": "gracias"}
        self.correct_count = 0
        self.total_attempts = 0

    def practice(self):
        for term, translation in self.vocab.items():
            user_translation = input(f"What's the translation of '{term}'? ")
            self.total_attempts += 1
            if user_translation.lower() == translation:
                print("Correct!\n")
                self.correct_count += 1
            else:
                print(f"Wrong! The correct translation is '{translation}'.\n")
        self.show_summary()

    def show_summary(self):
        print(f"Practice session completed!\nCorrect answers: {self.correct_count}/{self.total_attempts}")

if __name__ == "__main__":
    flashcards = Flashcards()
    print("Welcome to Language Flashcards!\nLet's practice:")
    flashcards.practice()
