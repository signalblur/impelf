# ImpELF

## Archived - I did not realize an implementation of this had already been created and was more widely used. Please refer to telfhash - https://github.com/trendmicro/telfhash

As someone that primarily does linux detection, I was frustrated that there wasn't an equivalent of an imphash for linux ELF binaries. So, I decided to make one myself. **Introducing** ImpELF. ImpELF is a Python-based ELF hashing utility that generates unique fingerprints for ELF binaries using their imported functions and libraries, aiding in malware analysis and similarity detection.

## Installation

First, ensure that you have Python 3.x installed on your system. You can download the latest version of Python from [the official website](https://www.python.org/downloads/).

Next, install the `pyelftools` library using pip:

```bash
pip install pyelftools
```

## Usage

Save the ImpELF script from the previous response as a file, e.g., impelf.py.

Run the ImpELF script on an ELF binary:

```
python impelf.py /path/to/your/elf_file
```

The script will output the ImpELF hash for the given ELF binary.

## Implementation and Example

By analyzing an ELF binaries dynamic symbols (imported functions) and libraries, we can create a hash similar to the PE file's imphash. Suppose we have an ELF binary with the following imported symbols and libraries:

Imported symbols:

* `printf`
* `malloc`
* `strcpy`
* `strcmp`

Libraries:

* `libc.so.6`
* `libm.so.6`

Using impelf.py, the `get_imported_symbols_and_libraries` function extracts the imported symbols and libraries from the ELF binary. The imported symbols and libraries are then returned as *two* separate lists.

After obtaining the lists of imported symbols and libraries, the create_hash function is called with these two lists as arguments. In this function, the symbols and libraries are first sorted:

Sorted imported symbols:

* `malloc`
* `printf`
* `strcmp`
* `strcpy`

Sorted libraries:

* `libc.so.6`
* `libm.so.6`

Then, the sorted imported symbols list is concatenated with the sorted libraries list to create a single string:

Example Concatenated string: `mallocprintfstrcmpstrcpylibc.so.6libm.so.6`

Finally, the concatenated string is hashed using the MD5 hashing algorithm (or another algorithm of your choice) to create the final ELF hash:

ELF hash: `4e4d4d4e8f8a96d30b9dab9d6deac8b3`

Keep in mind that the specific example provided here might not match the actual output you would get when running the script, as the output will depend on the specific ELF binary being analyzed. The example is meant to illustrate the process of sorting and concatenating the symbols and libraries before hashing.

## License

This project is licensed under the Mozilla Public License 2.0 (MPL-2.0). By using or contributing to this project, you agree to the terms of the license.


## Contributing

Contributions are welcome! If you have a bug report, feature request, or would like to contribute code, please open an issue or create a pull request on the GitHub repository.

* Fork the repository on GitHub.
* Create a new branch for your changes.
* Commit your changes and push them to your fork.
* Create a pull request with a description of your changes.

We appreciate your help in improving ImpELF!
