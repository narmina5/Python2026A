"""
my_list = [12, -4, 0, 7, 5, -9, 3, 11] listində:

1. heç olmasa bir ədədin 5-ə bölünüb-bölünmədiyini yoxlayın
2. bütün ədədlərin müsbət olub-olmadığını yoxlayın
3. yalnız cüt ədədləri çıxarın (tək sətirdə, filter istifadə edərək)
4. map() ilə hər bir ədədin kvadratını yeni listdə saxlayın
5. həmin yeni listin maksimum, minimum və cəmini çap edin
6. həmin listi azalan sıralayın və tərs çevirin
7. enumerate() ilə yeni listin hər bir elementini indekslə birlikdə çap edin
8. listin uzunluğunu çap edin

Bütün bu əməliyyatları main funksiyası içində yerinə yetirin.
"""

def main():
    my_list = [12, -4, 0, 7, 5, -9, 3, 11]

    divided_by_five = any([num if num % 5 == 0 else num for num in range(len(my_list))])
    print(divided_by_five)

    all_positive = all(my_list)
    print(all_positive)

    filtered_list = list(filter(lambda num: num % 2 == 0, my_list))
    print(filtered_list)

    """1. method """
    num_second_power = list(map(lambda num: num**2, my_list))
    print(num_second_power)
    # ve ya
    """2. method """
    def second_power(num):
        return num ** 2
    second_power = list(map(second_power, my_list))
    print(second_power)

    print(f'Maximum: {max(second_power)}, Minimum: {min(second_power)}, Sum: {sum(second_power)}')

    sorted_list = sorted(second_power, reverse=True)
    print(sorted_list)

    for index, num in enumerate(sorted_list):
        print(f'Indeks: {index}, Element: {num}')

    print(len(sorted_list))


if __name__ == '__main__':
    main()