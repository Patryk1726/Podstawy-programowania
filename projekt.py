import random

class Milionerzy:
    def __init__(self):
        #1-przechowywuje pytania i odpowiadajace im odpowiedzi
        self.pytania = {
            "1. Jaki jest stolica Francji?": {"A": "Berlin", "B": "Madryt", "C": "Paryż", "D": "Londyn", "Poprawna": "C"},
            "2. Który pierwiastek chemiczny ma symbol 'O'?": {"A": "Tlen", "B": "Azot", "C": "Wodór", "D": "Sód", "Poprawna": "A"},
            "3. Ile wynosi 2 do potęgi 5?": {"A": "8", "B": "16", "C": "32", "D": "64", "Poprawna": "C"},
            "4. Kto napisał dramat 'Romeo i Julia'?": {"A": "William Shakespeare", "B": "Charles Dickens", "C": "Jane Austen", "D": "Leo Tolstoy", "Poprawna": "A"},
            "5. Jakie jest największe jezioro na świecie?": {"A": "Jezioro Bajkał", "B": "Jezioro Erie", "C": "Jezioro Michigan", "D": "Jezioro Wiktorii", "Poprawna": "A"},
            "6. Który kraj jest największym producentem kawy na świecie?": {"A": "Brazylia", "B": "Kolumbia", "C": "Etiopia", "D": "Wietnam", "Poprawna": "A"},
            "7. Która planeta jest znana jako 'Czerwona Planeta'?": {"A": "Mars", "B": "Jowisz", "C": "Wenus", "D": "Saturn", "Poprawna": "A"},
            "8. Kto był pierwszym prezydentem Stanów Zjednoczonych?": {"A": "George Washington", "B": "Thomas Jefferson", "C": "Abraham Lincoln", "D": "John Adams", "Poprawna": "A"},
        }

    def losuj_pytanie(self):
        #2-losuje jedno pytanie z dostępnego zestawu
        return random.choice(list(self.pytania.items()))

    def zadaj_pytanie(self, pytanie):
        #wyświetla pytanie i opcje odpowiedzi a następnie pobiera odpowiedź od gracza
        print(pytanie)
        for opcja, odpowiedz in pytanie[1].items():
            if opcja != "Poprawna":
                print(f"{opcja}: {odpowiedz}")
        odpowiedz_gracza = input("Podaj odpowiedź (A, B, C, D): ")
        return odpowiedz_gracza.upper()

    def sprawdz_odpowiedz(self, pytanie, odpowiedz):
        #sprawdza czy udzielona odpowiedź jest poprawna
        return pytanie[1]["Poprawna"] == odpowiedz

    def graj(self):
        #główna funkcja odpowiedzialna za przeprowadzenie gry
        punkty = 0
        for _ in range(8):  #3-dostosowywanie liczby pytań
            pytanie = self.losuj_pytanie()
            odpowiedz_gracza = self.zadaj_pytanie(pytanie)

            if self.sprawdz_odpowiedz(pytanie, odpowiedz_gracza):
                print("Poprawna odpowiedź! Zdobywasz punkt.")
                punkty += 1
            else:
                print("Błędna odpowiedź. Koniec gry.")
                break

        if punkty == 8:
            print("Gratulacje! Wygrałeś milion!")
        else:
            print(f"Zdobyte punkty: {punkty}")

if __name__ == "__main__": 
    #przechowuje nazwe modulu
    gra = Milionerzy()
    print("Witaj w grze Milionerzy! Odpowiedz na 8 pytań, aby wygrać milion.")
    gra.graj()
