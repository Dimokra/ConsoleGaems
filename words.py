import random

Words = ["Арбуз", "Банан", "Игра", "Питон", "Микроволновка"]

def pick_word(arr):
    return random.choice(arr)

def play_game():
    word = pick_word(Words)
    word_letters = list(word.lower())
    guessed_letters = []
    attempts = 0
    max_attempts = 3  
    
    print("Ввод")

    while True:
        display_word = ""
        missing_count = 0
        
        for letter in word_letters:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
                missing_count += 1
        
        print(f"\nСлово: {display_word}")
        print(f"Осталось попыток: {max_attempts - attempts}") 
        
        if missing_count == 0:
            print(f"Успех.")
            break
        
        if attempts >= max_attempts:  
            print(f"Проигрыш! Слово было: {word}")
            break
            
        guess = input("Введите букву: ").lower()
        
        if len(guess) != 1:
            print("Пожалуйста, введите только одну букву.")
            continue
            
        if guess in guessed_letters:
            print("Эта буква уже была.")
            continue

        guessed_letters.append(guess)
        
        if guess in word_letters:
            print("Есть такая буква.")
        else:
            print("Нет такой буквы.")
            attempts += 1  

play_game()