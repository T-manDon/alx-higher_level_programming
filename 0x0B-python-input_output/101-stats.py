#!/usr/bin/python3
"""
Log Parsing
"""
def print_log_totals(total_file_size, code_counts):
    # Print the total file size and status code counts.
    print(f"File size: {total_file_size}")
    for code, count in code_counts.items():
        if count > 0:
            print(f"{code}: {count}")

if __name__ == '__main__':
    from sys import argv, stdin, stderr
    from collections import OrderedDict
    from datetime import datetime

    line_no = 0
    total_file_size = 0
    code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    try:
        for line in stdin:
            line_no += 1

            components = line.split('-', 1)
            if len(components) != 2:
                continue

            timestamp = components[1].split(']')[0].strip(' []')
            try:
                # Validate the timestamp format.
                datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S.%f')
            except ValueError:
                stderr.write(f"{argv[0]}: {line_no}: invalid timestamp\n")
                continue

            url_components = components[1].split('"')[1:]
            if url_components[0] != 'GET /projects/260 HTTP/1.1':
                stderr.write(f"{argv[0]}: {line_no}: unexpected HTTP request\n")
                continue

            status_code, file_size = url_components[1].strip().split(' ')
            
            if status_code.isdigit():
                code = int(status_code)
                code_counts[code] += 1

            if file_size.isdigit():
                total_file_size += int(file_size)

            if line_no % 10 == 0:
                # Print totals every 10 lines.
                print_log_totals(total_file_size, code_counts)
        
        print_log_totals(total_file_size, code_counts)

    except KeyboardInterrupt:
        # Handle keyboard interrupt by printing the totals.
        print_log_totals(total_file_size, code_counts)
        raise
