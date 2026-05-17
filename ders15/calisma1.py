"""
nums = [10, 0, -5, 8, 2, -3, 7, 0, 4] listində:

1. heç olmasa bir müsbət ədəd olub-olmadığını yoxlayın
2. bütün ədədlərin qeyri-mənfi olub-olmadığını yoxlayın
3. olan yalnız müsbət ədədləri çıxarın (tək sətirdə)
4. olan hər bir elementi indekslə birlikdə çap edin
5. uzunluğunu çap edin

Bu əməliyyatların hamısını main funksiyası içində edin.
"""

def main():
    nums = [10, 0, -5, 8, 2, -3, 7, 0, 4]
    has_positive = any([num > 0 for num in nums])
    all_positive = all([num > 0 for num in nums])
    print(has_positive)
    print(all_positive)


    positive_numbers = list(filter(lambda x: x > 0, nums))
    print(positive_numbers)


    for index, num in enumerate(nums):
        print(f'Indeks: {index}, Element: {num}')

    print(len(nums))

if __name__ == '__main__':
    main()