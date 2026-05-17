"""
Bu tapşırıqda siz, Python istifadə edərək, iki oyunçunun oynaya biləcəyi  (X və O) oyununu yaratmalısınız. Oyun yalnız terminalda işləyəcək və hər iki oyunçu növbə ilə öz hərəkətlərini edəcəklər.
Oyun taxtası 3x3 ölçüsündə və hər xana boş olmalıdır.
Hər iki oyunçu (X və O) növbə ilə oyun taxtasında hərəkətlərini edəcəklər.İpucu: taxtadakı dəyərləri list of list kimi tuta bilərsiniz: [["", "", ""],      ["", "", ""],      ["", "", ""]]
Hər iki oyunçu növbə ilə hərəkət edəcək və oyunçu müəyyən bir xananı seçərək oraya öz işarəsini (X və ya O) qoyacaq.
Oyunçular hərəkətlərini  ilə seçməlidir (0-dan 2-ə qədər).
Oyunçu hərəkət etməzdən əvvəl, seçilən xananın boş olduğuna əmin olmalıdır.
Hər iki oyunçu xanalarına X və O işarələri ilə ardıcıl düzülməlidir (horizontallı, vertikallı və ya diaqonal).
Oyunçu qələbə qazandıqda, oyun dərhal bitəcək və qələbə elan olunacaq.
Bütün xanalar dolarsa və heç bir oyunçu qalib gəlməzsə, oyun bitəcək.
Hər iki oyunçu oyunu bitirənə qədər növbə ilə hərəkətlərini edəcək.
Hər bir hərəkətdən sonra oyun taxtası ekranda yenidən göstəriləcək.
Hər bir hərəkətdən sonra oyun taxtası təzələnməlidir (ekran yenilənməlidir).
Terminalda oyun təmiz və sadə şəkildə göstərilməlidir.
 qələbəni və ya bərabərə qalmağı elan edin.
Oyunçu yalnız boş xanaya hərəkət edə bilər.
Hər bir oyunçuya növbə ilə oyun taxtasında hərəkət etməsi xahiş olunmalıdır.
Python istifadə edərək Tic-Tac-Toe oyununun kodunu yazın.Oyun taxtası 3x3 ölçüsündə olmalı və növbə ilə hərəkət etməli olan iki oyunçu olmalıdır.Oyun hər iki oyunçunun növbə ilə oynanmasını təmin etməlidir (Ilk X başlayır).Oyun bitdikdən sonra qalib və ya bərabər nəticəsi göstərilməlidir.
"""


def make_move(player):
    while True:
        try:
            row = int(input(f"Make move (row) - {player}: "))
            column = int(input(f"Make move (col.) - {player}: "))
        except ValueError:
            print("Dogru deyer daxil edin!")
        else:
            row -= 1
            column -= 1
            if 0 <= row <= 2 and 0 <= column <= 2:
                if taxta[row][column] == "":
                    taxta[row][column] = player
                    show_board()
                    break
                else:
                    print("O xana tutulub, basqa xanaya daxil edin!")
            else:
                print("Deyer dogru deyil!")


def show_board():
    for i in taxta:
        print(i)

    print("=======================")


def check_winner(player):
    for i in range(0, 3):
        if taxta[i][0] == taxta[i][1] == taxta[i][2] != "":
            print(f'{player} qazandi')
            return True
        if taxta[0][i] == taxta[1][i] == taxta[2][i] != "":
            print(f'{player} qazandi')
            return True

    if taxta[0][0] == taxta[1][1] == taxta[2][2] != "":
        print(f'{player} qazandi')
        return True
    if taxta[0][2] == taxta[1][1] == taxta[2][0] != "":
        print(f'{player} qazandi')
        return True

    return False


if __name__ == "__main__":
    taxta = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]
    ]
    player = "X"
    move_count = 0
    show_board()
    while True:
        make_move(player)
        move_count += 1
        if check_winner(player):
            print("Game over!")
            break
        elif move_count == 9:
            print("Draw!")
            break

        if player == "X":
            player = "O"
        else:
            player = "X"
