import enum


class EncryptionType(enum.IntEnum):
    DECRYPT = 1,
    ENCRYPT = 2


class EncryptionUtils:
    @staticmethod
    def convert_str_to_enum(value: str) -> EncryptionType | None:
        if value.isdigit():
            numerical_value = int(value)
        else:
            return None

        try:
            enum_value = EncryptionType(numerical_value)
            return enum_value
        except:
            return None

    @staticmethod
    def decrypt(message: str, shift: int) -> str:
        return EncryptionUtils.__use_caesar(message, shift * -1)

    @staticmethod
    def encrypt(message: str, shift: int) -> str:
        return EncryptionUtils.__use_caesar(message, shift)

    @staticmethod
    def __use_caesar(message: str, shift: int):
        min_value = 97
        max_value = 122
        length_value = max_value - min_value + 1
        processed_message = ""
        for letter in message:
            index = ord(letter) - min_value
            if 0 <= index < length_value:
                new_index = (index + shift) % length_value
                processed_message += chr(min_value + new_index)
            else:
                processed_message += "?"

        return processed_message
