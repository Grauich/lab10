def read_en_ru_dict(file_path):
    en_ru_dict = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            english, russian = line.strip().split(' - ')
            en_ru_dict[english] = russian.split(', ')
    return en_ru_dict

def create_ru_en_dict(en_ru_dict):
    ru_en_dict = {}
    for english, russian_words in en_ru_dict.items():
        for russian in russian_words:
            if russian not in ru_en_dict:
                ru_en_dict[russian] = []
            ru_en_dict[russian].append(english)
    return ru_en_dict

def write_ru_en_dict(file_path, ru_en_dict):
    with open(file_path, 'w', encoding='utf-8') as file:
        for russian in sorted(ru_en_dict.keys()):
            english_words = ', '.join(ru_en_dict[russian])
            file.write(f"{russian} – {english_words}\n")

en_ru_file_path = 'en-ru.txt'
ru_en_file_path = 'ru-en.txt'

en_ru_dict = read_en_ru_dict(en_ru_file_path)

ru_en_dict = create_ru_en_dict(en_ru_dict)

write_ru_en_dict(ru_en_file_path, ru_en_dict)
