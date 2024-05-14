from Day008.Utils.EncryptionUtils import EncryptionType, EncryptionUtils


def prompt_encryption_type() -> EncryptionType:
    encryption_type = 0
    while encryption_type == 0:
        encryption_type_input = input(
            f"Type '{EncryptionType.DECRYPT}' to decrypt, type '{EncryptionType.ENCRYPT}' to encrypt: ")
        enum_value = EncryptionUtils.convert_str_to_enum(encryption_type_input)
        if enum_value is not None:
            return enum_value
        else:
            print(f"Error: input should be numerical between {EncryptionType.DECRYPT} and {EncryptionType.ENCRYPT}")


def prompt_shift() -> int:
    shift = 0
    while shift == 0:
        value = input("Type the shift number: ")
        if value.isdigit():
            return int(value)


def main():
    encryption_type = prompt_encryption_type()
    message = input("Type your message:\n")
    shift = prompt_shift()

    match encryption_type:
        case EncryptionType.DECRYPT:
            processed_message = EncryptionUtils.decrypt(message, shift)
        case EncryptionType.ENCRYPT:
            processed_message = EncryptionUtils.encrypt(message, shift)
        case _:
            processed_message = ""

    print(f"The processed message is [{processed_message}]")


main()
