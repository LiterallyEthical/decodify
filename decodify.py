import base64
import base58
import argparse
from src.base62_decoder import base62_decoder
from src.base_decoders import base_decoders


def ascii_banner():
    print("""    ____                      ___ ____     
   / __ \___  _________  ____/ (_) __/_  __
  / / / / _ \/ ___/ __ \/ __  / / /_/ / / /
 / /_/ /  __/ /__/ /_/ / /_/ / / __/ /_/ / 
/_____/\___/\___/\____/\__,_/_/_/  \__, /  
                                  /____/  \n""")


def main(args):
    base_formats = {"base64": base64.b64decode, "base16": base64.b16decode, "base32": base64.b32decode,
                    "base32hex": base64.b32hexdecode, "base85": base64.b85decode, "a85": base64.a85decode, "base58": base58.b58decode}

    for decoding_format, decoder_func in base_formats.items():
        try:
            base_decoders(args.data, args.out_file,
                          decoding_format, decoder_func, args.depth)

        except:
            pass

    try:
        base62_decoder(args.data, args.out_file, args.depth)

    except:
        pass


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Decodes the given data using various algorithms')
    parser.add_argument('data',
                        help='The encoded data to decode')
    parser.add_argument(
        '-o', '--out_file', default='out.txt', metavar='FILE', help='The output file to write to the decoded data to')
    parser.add_argument('-d', '--depth', type=int, default=1,
                        help='Maximum number of times to decode the data')

    args = parser.parse_args()

    ascii_banner()
    main(args)
