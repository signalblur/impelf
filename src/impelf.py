import sys
import hashlib
from elftools.elf.elffile import ELFFile
from elftools.elf.dynamic import DynamicSection

def get_imported_symbols_and_libraries(elf_file):
    imported_symbols = []
    libraries = []

    for section in elf_file.iter_sections():
        if isinstance(section, DynamicSection):
            for tag in section.iter_tags():
                if tag.entry.d_tag == 'DT_NEEDED':
                    libraries.append(tag.needed)
                elif tag.entry.d_tag == 'DT_STRTAB':
                    string_table = elf_file.get_section_by_offset(tag.entry.d_val)
                    break

    for section in elf_file.iter_sections():
        if hasattr(section, 'iter_symbols'):
            for symbol in section.iter_symbols():
                if symbol.name and symbol.entry.st_info.type == 'STT_FUNC':
                    imported_symbols.append(symbol.name)

    return imported_symbols, libraries

def create_hash(imported_symbols, libraries):
    hash_data = ''.join(sorted(imported_symbols) + sorted(libraries))
    return hashlib.md5(hash_data.encode('utf-8')).hexdigest()

def main():
    
    if len(sys.argv) < 2:
        print(f'Usage: {sys.argv[0]} <path_to_elf_file>')
        sys.exit(1)

    with open(sys.argv[1], 'rb') as f:
        elf_file = ELFFile(f)
        imported_symbols, libraries = get_imported_symbols_and_libraries(elf_file)
        elf_hash = create_hash(imported_symbols, libraries)
        print(elf_hash)


if __name__ == '__main__':
    main()