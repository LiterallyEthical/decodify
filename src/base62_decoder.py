import base62
import string


def base62_decoder(data, out_file, depth=1):

    if isinstance(data, str):
        for i in range(depth):

            base62_chars = string.digits + string.ascii_uppercase + string.ascii_lowercase
            base62_map = {c: i for i, c in enumerate(base62_chars)}

            n = 0
            for c in data:
                n = n * 62 + base62_map[c]

            decoded_data = ""
            while n > 0:
                n, r = divmod(n, 256)
                decoded_data = chr(r) + decoded_data

            data = decoded_data

            try:
                with open(out_file, 'a') as file:
                    file.write(decoded_data + '\n')
                    print(
                        f"Decoded Data -->  {decoded_data}    (DecodingFormat: base62)")
            except:
                print(f"Could not decode {decoded_passwd} as UTF-8, skipping")

    else:

        data = int(data)
        decoded_data = base62.encode(data)

        try:
            with open(out_file, 'a') as file:
                file.write(decoded_data + '\n')
                print(
                    f"Decoded Data -->  {decoded_data}    (DecodingFormat: base62)")
        except:
            print(f"Could not decode {decoded_passwd} as UTF-8, skipping")
