#s = aaabcca

# def strcounter(s):
#     for sym in set(s):
#         counter = 0
#         for sub_sym in s:
#             if sym == sub_sym:
#                 counter +=1
#         print(sym, counter)
#
#
# s = 'aaabbc'


# strcounter(s)


def strcounter(s):
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym,0)+1

    print(syms_counter)

s = 'aaabbc'
strcounter(s)

print('Второй коммит')

# git config --global user.name "anna" - задать имя конфигурации
# git config --global user.email "anna"
# q - выйти
# git init - инициализация проекта
# git add . - добавить под коммит все новые файлы
# git commit -m 'первый коммит'
# git branch origin main - 'делает главную ветку main