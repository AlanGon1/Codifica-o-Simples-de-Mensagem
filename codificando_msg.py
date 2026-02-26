def zenit_polar_replace(text):
    # Aplicar a codificação Z-E-N-I-T P-O-L-A-R utilizando o método replace
    replacements = [('z', 'p'), ('e', 'o'), ('n', 'l'), ('a', 'r'),  # minúsculas
                    ('Z', 'P'), ('E', 'O'), ('N', 'L'), ('A', 'R')]  # Maiúsculas
    for old, new in replacements:
        text = text.replace(old, new)
    return text

def main():
    phrase = "the quick brown fox jumps over the lazy dog"
    phrase_title = phrase.title() # Primeira letra de cada palavra maiúscula

    # Dividir a frase em palavras
    words = phrase_title.split()

    # Processar cada palavra na lista usando ZENIT POLAR
    coded_words = [zenit_polar_replace(word) for word in words]

    # Juntar todas as palavras codificadas em uma frase.
    coded_phrase = " ".join(coded_words)
    print("Original:", phrase)
    print("Title:", phrase_title)
    print("Coded:", coded_phrase)

if __name__ == '__main__':
    main()
