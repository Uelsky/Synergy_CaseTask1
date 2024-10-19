from pyexpat.errors import messages


def encrypt_vigenere(message, key):
    result = ""
    for i in range(len(message)):
        char = message[i]
        key_char = key[i % len(key)]
        num_char = ord(char) - ord("А")
        num_key_char = ord(key_char) - ord("А")
        new_num = (num_char + num_key_char) % 34
        if new_num < 0:
            new_num += 34
        result += chr(new_num + ord("А"))
    return result

if __name__ == "__main__":
    with open("message.txt", 'r', encoding='utf-8') as file:
        reader = file.readlines()
        for i in range(len(reader)):
            message = reader[i]
            key = "cинергия"
            encrypted_message = encrypt_vigenere(message, key)
            print(f"Зашифрованный абзац {i + 1}:", encrypted_message)