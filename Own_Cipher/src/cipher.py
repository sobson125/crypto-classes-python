import string


class Cipher:

    @staticmethod
    def __generate_square__(key):
        big_letters = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        square = []
        for char in key.upper():
            if char not in square and char in big_letters:
                square.append(char)

        for char in big_letters:
            if char not in square:
                square.append(char)

        return square

    @staticmethod
    def encode(text_to_encode, key):
        table = Cipher.__generate_square__(key)
        alphabet = string.ascii_letters
        text_with_j = "".join([char.upper() for char in text_to_encode if char in alphabet])
        text = text_with_j.replace('J', 'I')

        cleaned_up_text = ""

        for i in range(len(text) - 1):
            cleaned_up_text += text[i]

            if text[i] == text[i + 1]:
                cleaned_up_text += "X"

        cleaned_up_text += text[-1]

        if len(cleaned_up_text) % 2 != 0:
            if len(cleaned_up_text) - len(text_to_encode) == 0:
                cleaned_up_text += "X"

        encoded = ""

        for i in range(0, len(cleaned_up_text), 2):
            char1 = cleaned_up_text[i]
            char2 = cleaned_up_text[i + 1]
            row1, col1 = divmod(table.index(char1), 5)
            row2, col2 = divmod(table.index(char2), 5)

            if col1 == col2:
                encoded += table[((row1 + 1) % 5) * 5 + col1]
                encoded += table[((row2 + 1) % 5) * 5 + col2]
            elif row1 == row2:
                encoded += table[row1 * 5 + (col1 + 1) % 5]
                encoded += table[row2 * 5 + (col2 + 1) % 5]
            else:
                encoded += table[row1 * 5 + col2]
                encoded += table[row2 * 5 + col1]

        return encoded

    @staticmethod
    def decode(encoded_text, key):
        square = Cipher.__generate_square__(key)
        decoded = ""

        for i in range(0, len(encoded_text), 2):
            char1 = encoded_text[i]
            char2 = encoded_text[i + 1]
            row1, col1 = divmod(square.index(char1), 5)
            row2, col2 = divmod(square.index(char2), 5)

            if col1 == col2:
                decoded += square[((row1 - 1) % 5) * 5 + col1]
                decoded += square[((row2 - 1) % 5) * 5 + col2]
            elif row1 == row2:
                decoded += square[row1 * 5 + (col1 - 1) % 5]
                decoded += square[row2 * 5 + (col2 - 1) % 5]
            else:
                decoded += square[row1 * 5 + col2]
                decoded += square[row2 * 5 + col1]

        return decoded
