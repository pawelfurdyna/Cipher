# Program szyfrujący i deszyfrujący wiadomość tekstową:
#     - wiadomość zostanie przekonwertowania za pomocą słownika (kluczy i wartości) do alfabetu Morse'a,
#     - następnie . oraz - zamieni na ciąg 0 oraz 1,
#     - uzyskane łańcuchy zostaną złączone i podzielone w ten sposób aby można było je przedstawić w wartości systemu szesnastkowego,
#     - jeśli zostanie podana zaszyfrowana treść program ją odszyfruje.

import os
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename

morse = {"a": "01",
        "b": "1000",
        "c": "1010",
        "d": "100",
        "e": "0",
        "f": "0010",
        "g": "110",
        "h": "0000",
        "i": "00",
        "j": "0111",
        "k": "101",
        "l": "0100",
        "m": "11",
        "n": "10",
        "o": "111",
        "p": "0110",
        "q": "1101",
        "r": "010",
        "s": "000",
        "t": "1",
        "u": "001",
        "v": "0001",
        "w": "011",
        "x": "1001",
        "y": "1011",
        "z": "1100",
        "ą": "0101",
        "ć": "10100",
        "ę": "00100",
        "ł": "010011",
        "ń": "11011",
        "ó": "1110",
        "ś": "0001000",
        "ż": "110010",
        "ź": "11001",
        "A": "10110000",
        "B": "11000100",
        "C": "11010100",
        "D": "11001000",
        "E": "10100000",
        "F": "10010100",
        "G": "11101000",
        "H": "10000100",
        "I": "10010000",
        "J": "10111100",
        "K": "11011000",
        "L": "10100100",
        "M": "11110000",
        "N": "11010000",
        "O": "11111000",
        "P": "10110100",
        "Q": "11101100",
        "R": "10101000",
        "S": "10001000",
        "T": "11100000",
        "U": "10011000",
        "V": "10001100",
        "W": "10111000",
        "X": "11001100",
        "Y": "11011100",
        "Z": "11100100",
        "Ą": "10101100",
        "Ć": "11010010",
        "Ę": "10010010",
        "Ł": "10100111",
        "Ń": "11101110",
        "Ó": "11110100",
        "Ś": "10001001",
        "Ż": "11100101",
        "Ź": "11100110",
        "1": "01111",
        "2": "00111",
        "3": "00011",
        "4": "00001",
        "5": "00000",
        "6": "10000",
        "7": "11000",
        "8": "11100",
        "9": "11110",
        "0": "11111",
        ".": "010101",
        ",": "110011",
        "'": "011110",
        "\"": "010010",
        "_": "001101",
        ":": "111000",
        ";": "101010",
        "?": "001100",
        "!": "101000",
        "-": "100001",
        "+": "01010",
        "/": "10010",
        "(": "10110",
        ")": "101101",
        "=": "10001",
        "@": "011010",
        " ": "01001",
        "\n": "10101010",
        "\t": "01010101",
        "#": "01010001",
        "$": "01010010",
        "%": "01010011",
        "^": "01010100",
        "&": "01010111",
        "*": "01011000",
        "[": "01011001",
        "]": "01011010",
        "{": "01011011",
        "}": "01011100",
        "\\": "01011101",
        "<": "01011110",
        ">": "01011111"
}

def open_file():
    # otwórz plik
    filepath = askopenfilename(
    filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)

    # wyświetl treść pliku. Jeśli kodowanie jest inne niż UTF-8 użyj domyślnego kodowania
    try:
        with open(filepath, "r", encoding="UTF-8") as input_file:
                text = input_file.read().rstrip()
                txt_edit.insert(tk.END, text)
    except:
        try:
            with open(filepath, "r") as input_file:
                text = input_file.read().rstrip()
                txt_edit.insert(tk.END, text)
        #błąd - nie udało się dopasować systemu kodowania
        except:
            messagebox.showerror("Błąd", "Nieobsługiwany system kodowania znaków.\nObsługiwane systemy to ANSI oraz UTF-8.")


def save_file():
    # zapisz plik
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return

    # zapisz tekst z okna tekstowego
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)



def main():
    window.mainloop()

def Encrypt():
    message = txt_edit.get(1.0, tk.END).rstrip()

    morseMessage = ''
    morseCoding = ''

    # dla kazdego znaku w lancuchu wybierz odpowiednia wartosc po kluczu oraz przekaz dlugosc tej wartosci
    for char in message:
        try:
            morseMessage += morse[char]
        # zwróć komunikat o znaku, który nie został wprowadzony do słownika
        except KeyError:
            messagebox.showerror("Błąd", f'Podany znak "{char}" jest nieobsugiwany. Spróbuj użyć innego znaku.')
        morseCoding += str(len(morse[char]))
    
    # jesli dlugosc kodowania jest nieparzysta to dodaj 0 na koniec
    hexCoding = ""
    if len(morseCoding)%2 != 0:
        morseCoding += "0"
        
    # rozdziel kodowanie na pary cyfr tak aby przypominaly zapis szestnastkowy
    for i in range(0, len(morseCoding), 2):
        hexCoding += morseCoding[i:i+2] + " "

    # dodaj do kodowania 00 na koniec jako klucz podzialu
    hexCoding += "00"

    # zamien zapis binarny na szestnastkowy
    hexMessage = ConvertToHex(morseMessage)

    txt_edit.delete(1.0, tk.END)
    txt_edit.insert(1.0, hexCoding + " " + hexMessage)

def ConvertToHex(mess):
    # jesli dlugosc wiadomosci w zapisie binarnym nie jest podzielna przez 8 to dopisz brakujace znaki na koncu lancucha jako 0
    while len(mess)%8 != 0:
        mess += "0"

    hexMess = ""
    
    # wybierz 8 kolejnych znakow z lancucha
    # zamien na int w zapisie binarnym,
    # zamien na zapis heksagonalny,
    # zamien na lancuch znakow oraz obetnij dwa pierwsze znaki (0x)
    for i in range(0, len(mess), 8):
        convertToHex = str(hex(int(mess[i:i+8], 2)))[2:]

        # jeśli po zamienieniu na zapis szestnastkowy zostal jeden znak to dopisz 0 przed nim
        if len(convertToHex) == 1:
            convertToHex = "0" + convertToHex

        hexMess += convertToHex + " "

    # zwroc i obetnij biale znaki na koncu lancucha
    return hexMess.strip()

def Decrypt():
    message = txt_edit.get(1.0, tk.END).rstrip()
    
    # podziel lancuch na liste 
    message = message.split(" ")


    morseCoding = ""
    binNumber = ""
    morseMessage = ""
    code = True

    # pobierz kolejne wartosci z listy
    for hex in message:
        # jesli pojawi sie pierwszy raz 00 oznacza to koniec kodowania
        if hex == "00":
            code = False

        # jesli code jest prawdziwe to zlacz wartosci kodowania
        if code:
            morseCoding += hex

        # jesli code jest falszywe dodaj 0x przed wartosc
        # zamien na int w zapisie szestnastkowym
        # zamien na zapis binarny
        # zamien na lancuch oraz obetnij dwa pierwsze znaki (0b)
        else:
            hexNumber = "0x" + hex
            try:
                binNumber = str(bin(int(hexNumber, 16)))[2:]
            # zwróć błąd o znakach, które zostały źle wprowadzone
            except ValueError:
                messagebox.showerror("Błąd", f'Nie udało się przekonwertować następującego ciągu znaków {hex}')

            # jesli lancuch jest krotszy od 8 znakow dodaj 0 na poczatek lancucha
            while len(binNumber) % 8 != 0:
                binNumber = "0" + binNumber
            morseMessage += binNumber
    
    # obetnij pierwsze 8 znakow pozostale po znaku podzialu
    morseMessage = morseMessage[8:]

    # jesli na koncu lancucha pozostalo 0 -> obetnij je
    if morseCoding[-1] == "0":
        morseCoding = morseCoding[:-1]

    message = ""
    morseList = []
    i = 0

    # zapisz do listy poszczegolne kombinacje znakow morsa powstale po podzieleniu wiadomosci z zapisu binarnego wedlug kolejnych cyfr kodowania
    for code in morseCoding:
        try:
            morseList.append(morseMessage[i:i + int(code)])
        # zwróć błąd o znakach, które zostały źle wprowadzone
        except ValueError:
            messagebox.showerror("Błąd", f'Nie udało się przekonwertować następującego ciągu znaków {code}')
        i += int(code)
    
    # odczytaj kolejne wartosci z listy i porownaj po kolei z kluczami ze slownika
    # po znaleziemiu odpowiedniej wartosci klucza, zapisz klucz do wiadomosci
    for elem in morseList:
        for key in morse.keys():
            if morse[key] == elem:
                message += key

    txt_edit.delete(1.0, tk.END)
    txt_edit.insert(1.0, message)

# utwórz okno, tytuł oraz rozmiar
window = tk.Tk()
window.title("Cipher")
window.rowconfigure(0, minsize=400, weight=1)
window.columnconfigure(1, minsize=400, weight=1)

# pole tekstowe
txt_edit = tk.Text(window)

# przyciski
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="Otwórz", command=open_file)
btn_save = tk.Button(fr_buttons, text="Zapisz jako...", command=save_file)
btn_encrypt = tk.Button(fr_buttons, text="Zaszyfruj", command=Encrypt)
btn_decrypt = tk.Button(fr_buttons, text="Odszyfruj", command=Decrypt)

# ustawienie przycisków, ich szerokości oraz odstępów pomiędzy nimi
btn_open.grid(row=0, column=0, sticky="ew", padx=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5, pady=10)
btn_encrypt.grid(row=2, column=0, sticky="ew", padx=5)
btn_decrypt.grid(row=3, column=0, sticky="ew", padx=5, pady=10)

# rozciągnięcie panelu z przeciskami pionowo w 1 kolumnie oraz uzupełnienie pozostałego miejsca polem tekstowym
fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

if __name__ == "__main__":
    main()