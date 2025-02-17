eng_letters = "ABCEHKMOPTXaceoypx"
rus_letters = "АВСЕНКМОРТХасеоурх"
text = open('text.txt', 'r')
to_encode = open('to_encode.txt', 'r')
def encode(text, to_encode):
    encoded = open('encoded.txt', 'w')
    simbol = to_encode.read(1)
    while simbol != '':
        bits = str(bin(ord(simbol)))[1:]
        while bits != '':
            sim = text.read(1)
            if sim == '':
                break
            if sim not in eng_letters:
                encoded.write(sim)
            else:
                if bits[0] == '1':
                    encoded.write(rus_letters[eng_letters.index(sim)])
                else:
                    encoded.write(sim)
                bits = bits[1:]
        simbol = to_encode.read(1)
    encoded.close()
def decode(to_encode_len):
    encoded = open('encoded.txt', 'r')
    decoded = open('decoded.txt', 'w')
    cnt = 0
    while cnt <= to_encode_len:
        simbol = encoded.read(1)
        bits = ''
        while simbol != '':

            if simbol in rus_letters:
                bits += '1'
            elif simbol in eng_letters:
                bits += '0'
            if len(bits) == 8:
                print(chr(int(bits, 2)))
                bits = ''
                cnt += 1
            simbol = encoded.read(1)

    encoded.close()
    decoded.close()
choose = input("Что вы хотите сделать: 1 - зашифровать, 2 - расшифровать: ")
if choose == '1':
    encode(text, to_encode)
    print("Текст зашифрован в encoded.txt")
elif choose == '2':
    size = int(input("Введите длину зашифрованного сообщения: "))
    decode(size)
text.close()
to_encode.close()
