import string

chars = ' ' + string.punctuation + string.digits + string.ascii_letters

chars_list = list(chars)

keys = ['v', '#', 'O', 'n', ']', 'U', '}', 'y', "'", 'e', 'j', 'f', '*', 'i', 'A', 't', 'Q', '7', 'x', 'M', 'q', '"', '\\', ' ', 'l', 'H', '[', '-', 'b', '|', 'w', 's', '`', '9', 'I', 'J', 'F', 'R', ';', '0', 'p', '=', 'k', 'h', 'K', '/', 'Z', '2', 'm', ',', 'o', 'u', '^', '{', '~', 'X', '>', 'C', ')', '+', 'W', '5', 'T', 'Y', 'N', 'a', 'r', 'B', ':', '_', 'P', '<', '$', 'V', 'd', 'z', '?', '.', '8', 'D', 'E', '!', '4', 'G', '3', '&', 'S', 'L', 'g', 'c', '1', '%', '6', '@', '(']


plain_token = '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'
plain_email = 'szati95@wp.pl'



def code_encrypted(code):
    encrypt_dict = {}
    for i in range(len(chars_list)):
        encrypt_dict[chars_list[i]] = keys[i]
    plain_code_encrypted = ''
    for cod in code:
        plain_code_encrypted += encrypt_dict[str(cod)]
    return plain_code_encrypted



def code_decrypted(code):
    decrypt_dict = {}
    for i in range(len(keys)):
        decrypt_dict[keys[i]] = chars_list[i]
    plain_code_decrypted = ''
    for cod in code:
        plain_code_decrypted += decrypt_dict[str(cod)]
    return plain_code_decrypted


email_encrypted = code_encrypted(plain_email)

token_encrypted = code_encrypted(plain_token)

print(email_encrypted)

print(token_encrypted)