# Decodify

Have you ever encountered with a suspicious text and try to decode it  in various formats in order to retrieve the
hidden information. Well, you don't need to do it manually anymore, just specify the data you found and decodify will
identify and decode the data for you.


## Requirements

To install and use this project, you will need to have Python 3.x and the following packages installed:


* base58      
* pybase62


## Installation

Run the following command on terminal or cli
```
git clone git@github.com:LiterallyEthical/decodify.git
```  

* Install the requirements with
```
    python -m pip install -r requirements.txt
```

## Features

* Supports decoding data using multiple algorithms including base64, base16, base32, base32hex, base58, base85, and a85.
* Allows for decoding of data up to a specified depth.
* Outputs decoded data to a file specified by the user, or to a default file named out.txt. 

## Supported Decoding Formats

|Format | Descripton |
| ----- | ---------- |
|base64 | Base64 encoding, as specified in RFC 4648 |
|base16 | Base16 (hexadecimal) encoding |
|base32 | 	Base32 encoding, as specified in RFC 4648|
|base32hex| Base32hex encoding, as specified in RFC 4648|
|base58| Base58 encoding, used in Bitcoin and other cryptocurrencies|
|base85| Ascii85 encoding, as specified in Adobe PostScript Language Reference|
|a85 | Ascii85 encoding, as specified in Adobe PostScript Language Reference (short) |
|base62 | Base62 encoded data (custom character set)|






## Usage

To use Decodify, simply run the decodify.py script with the encoded data as a positional argument. Decodify will attempt to decode the data using each supported algorithm in turn, up to a maximum depth specified with the -d or --depth option.

```shell
usage: decodify.py [-h] [-o FILE] [-d DEPTH] data

Decodes the given data using various algorithms

positional arguments:
  data                  The encoded data to decode

options:
  -h, --help            show this help message and exit
  -o FILE, --out_file FILE
                        The output file to write to the decoded data to
  -d DEPTH, --depth DEPTH
                        Maximum number of times to decode the data
```

## Examples

> Prior knowledge to encoding format is not required

To decode a base64 encoded string, simply run:

```
python decodify.py PkhlbGxvLCBmcmllbmQ=
```

To decode a double base58-encoded string and write the output to a file, run:

```
python decodify.py -o <filename> -d 2 FjK1dhkR8cRzznzK8KmwpX9Nnu
```
> By default it appends all the decoded datas to 'out.txt' file

## Contributing

Contributions are welcome. To contribute to the project, please fork the repository, make changes, and submit a pull request.

## License

Decodify is released under the MIT License. See LICENSE for details.

## Acknowledments

* pybase62
* argparse
* base64
* base58

Special thanks to the developers of these packages.

## Disclaimer

This tool is intended for legitimate and legal use only. Any unauthorized use of this tool is strictly prohibited.

