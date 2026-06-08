while True:
    yas = input("Yasinizi daxil edin: ")
    if yas.isdigit():
        print(f'Yasiniz: {yas}')
        break
    else:
        print("Duzgun deyer daxil et")