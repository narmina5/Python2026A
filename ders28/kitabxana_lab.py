"""
Dərs 28 — Cursor AI lab
Kitabxana CLI: fayldan kitab siyahısı oxuyur və axtarış edir.

Səhvlər (tələbələr Cursor ilə tapıb düzəldəcək):
1. search_books — filter məntiqi səhvdir (case-sensitive / substring)
2. load_books — books.txt tapılmayanda proqram çökür
"""

BOOKS_FILE = "books.txt"


def load_books(path: str = BOOKS_FILE) -> list[dict]:
    """Hər sətir: basliq|muellif|il"""
    books = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split("|")
            if len(parts) != 3:
                continue
            title, author, year = parts
            books.append(
                {
                    "title": title.strip(),
                    "author": author.strip(),
                    "year": year.strip(),
                }
            )
    return books


def search_books(books: list[dict], query: str) -> list[dict]:
    """Başlıq və ya müəllif üzrə axtarış."""
    q = query.strip()
    result = []
    for book in books:
        # BUG: yalnız tam uyğunluq yoxlayır; "python" axtarışında "Python əsasları" tapılmır
        if book["title"] == q or book["author"] == q:
            result.append(book)
    return result


def print_books(books: list[dict]) -> None:
    if not books:
        print("Heç bir kitab tapılmadı.")
        return
    for i, b in enumerate(books, start=1):
        print(f"{i}. {b['title']} — {b['author']} ({b['year']})")


def main() -> None:
    books = load_books()
    print("=== Kitabxana (Cursor lab) ===")
    print(f"Yüklənən kitab sayı: {len(books)}\n")

    while True:
        print("1 — Bütün kitablar")
        print("2 — Axtarış")
        print("x — Çıxış")
        choice = input("Seçim: ").strip().lower()

        if choice == "x":
            print("Sağ ol!")
            break
        if choice == "1":
            print_books(books)
        elif choice == "2":
            query = input("Axtarış sözü: ")
            found = search_books(books, query)
            print_books(found)
        else:
            print("Yanlış seçim.")


if __name__ == "__main__":
    main()