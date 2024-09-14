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

print('Hello1')


#git config --global user.name "anna" - задать имя конфигурации
# q-выйти
# git init - инициализация проекта
# git commit -m 'первый коммит'