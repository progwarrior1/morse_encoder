
import random

words_ = ['mirror', 'hat', 'flight', 'dog', 'bag']
answers = []
morse_dict = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
}


def get_word():
    return random.choice(words_)


def print_stat(answers):
    print('всего задачек', len(answers))
    print('отвечено верно', answers.count(True))
    print('отвечено неверно', answers.count(False))


def morse_encode(words):
    result = ''
    for i in words:
        result += morse_dict.get(i, '')
    return result


def main():
    print('поиграем нажмите enter')
    input()
    for time in range(1, len(words_) + 1):
        current_word = get_word()
        current_encode = morse_encode(current_word)
        print(f'слово {time}{current_encode}')
        print(current_word)
        user_input = input()
        if user_input == current_word:
            print('верно')
            answers.append(True)

        else:
            print(f'нет не верно, это {current_word}')
            answers.append(False)
    print_stat(answers)
main()