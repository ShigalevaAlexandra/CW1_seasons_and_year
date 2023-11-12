# Разработка приложения, которое определяет время года по номеру месяца.

vremena_goda = {'--> ЗИМА': (1, 2, 12),
                '--> ВЕСНА': range(3, 6),
                '--> ЛЕТО': range(6, 9),
                '--> ОСЕНЬ': range(9, 12)}

month = int(input("Введите номер месяца (1 - 12): "))

if month not in range(1, 13):
    print("Такого месяца не существует)")

for key in vremena_goda.keys():
    if month in vremena_goda[key]:
        print(key)