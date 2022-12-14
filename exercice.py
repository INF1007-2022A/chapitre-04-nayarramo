#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_even_len(string: str) -> bool:
    result = len(string)%2 == 0
    return result


def remove_third_char(string: str) -> str:
    result = string[:2]+string[3:]
    return result


def replace_char(string: str, old_char: str, new_char: str) -> str:
    result = string.replace(old_char, new_char)
    return result


def get_number_of_char(string: str, char: str) -> int:
    nb = 0
    for letter in string:
        if ord(letter) == ord(char):
            nb+=1
    return nb


def get_number_of_words(sentence: str, word: str) -> int:
    nb = 0
    words = sentence.split()
    for w in words:
        if w == word:
            nb+=1
    return nb


def main() -> None:
    chaine = "Bonjour!"
    if is_even_len(chaine):
        print(f"Le nombre de caractère dans la chaine {chaine} est pair")
    else:
        print(f"Le nombre de caractère dans la chaine {chaine} est impair")

    chaine = "salut monde!"
    print(f"On supprime le 3e caratère dans la chaine: {chaine}. Résultat : {remove_third_char(chaine)}")

    chaine = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: {chaine}. Résultat : {replace_char(chaine, 'w', 'z')}")

    print(f"Le nombre d'occurrence de l dans {chaine} est : {get_number_of_char(chaine, 'l')}")
    
    chaine = "Baby shark doo doo doo doo doo doo"
    print(f"L'occurence du mot doo dans la chaine {chaine} est: {get_number_of_words(chaine, 'doo')}")


if __name__ == '__main__':
    main()
