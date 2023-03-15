def base_decoders(encoded_data, out_file, decoding_format, decoder_func,  depth=1):

    decoded_data = ''

    for i in range(depth):

        if not isinstance(encoded_data, bytes):
            encoded_data = encoded_data.encode('utf-8')

        try:
            decoded_data = decoder_func(encoded_data)
            encoded_data = decoded_data
        except:
            pass

        try:
            if isinstance(decoded_data, bytes):
                decoded_data = decoded_data.decode('utf-8')
        except:
            pass

        if decoded_data != '' or decoded_data != Null:
            try:
                with open(out_file, 'a') as file:
                    file.write(decoded_data + '\n')
                    print(
                        f"Decoded Data -->  {decoded_data} (DecodingFormat: {decoding_format})")
            except:
                pass
