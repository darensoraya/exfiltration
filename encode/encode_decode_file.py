import argparse

from string import ascii_lowercase, ascii_uppercase, digits
from chepy import Chepy
from chepy.extras import characters

# Déterminer la suite de caractère pour l'encodage
def base64_char_sets() -> dict:
    chepy_dict = characters.base64_char_sets()
    chepy_dict['custom_ascii'] = ascii_lowercase + '-' + digits + '^' + ascii_uppercase + '/'
    return chepy_dict

# Methode pour encoder le contenu du fichier avec chepy
def base64_encode_decode_chepy(file_in, file_out, action, encode_format):
    custom = base64_char_sets()[encode_format]
    if action == 'decode':
        c = Chepy(file_in).read_file().base64_decode(custom=custom)
        c.write_binary(file_out)
    else:
        c = Chepy(file_in).read_file().base64_encode(custom=custom)
        c.write_binary(file_out)


def main():
    parser = argparse.ArgumentParser(description='Encode and Decode base 64 with an optional custom alphabet')
    parser.add_argument('-a', '--action', help='encode|decode file', dest='action', choices=['encode', 'decode'],
                        default='encode', required=False)
    parser.add_argument('-i', '--file-in', help='Input file that needs to be encoded', dest='file_in', required=False,
                        default='test_2.pdf')
    parser.add_argument('-f', '--format', help='Encode format', dest='format', choices=list(base64_char_sets().keys()),
                        default='custom_ascii', required=False)
    args = parser.parse_args()

    file_in_e = args.file_in
    action = args.action
    encode_format = args.format
    file_out_e = "Document.pdf." + action + 'd'
    print('{} -- {} - {} --> {}'.format(file_in_e,action,encode_format,file_out_e))
    base64_encode_decode_chepy(file_in_e, file_out_e, action, encode_format)
    file_in_d = file_out_e
    action = "decode"
    file_out_d = "Document." + action + ".pdf"
    print('{} -- {} - {} --> {}'.format(file_in_d, action, encode_format, file_out_d))
    base64_encode_decode_chepy(file_in_d, file_out_d, action, encode_format)
    print('Finished')


if __name__ == '__main__':
    main()
