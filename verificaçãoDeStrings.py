def count_letter_a(s):
    count = s.lower().count('a')
    return count

string = input("Informe uma string: ")

count = count_letter_a(string)
if count > 0:
    print(f"A letra 'a' aparece {count} vezes na string.")
else:
    print("A letra 'a' não aparece na string.")