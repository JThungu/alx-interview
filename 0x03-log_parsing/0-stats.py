#!/usr/bin/python3
import sys

total_file_size = 0
status_code_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        try:
            # Parsing the line
            _, _, _, _, _, status_code, file_size = line.strip().split()

            # Update total file size
            total_file_size += int(file_size)

            # Update status code count
            status_code = int(status_code)
            if status_code in status_code_count:
                status_code_count[status_code] += 1

        except ValueError:
            # Skip lines with incorrect format
            continue

        # Print statistics after every 10 lines
        if line_count % 10 == 0:
            print(f"File size: {total_file_size}")
            for code in sorted(status_code_count.keys()):
                if status_code_count[code] > 0:
                    print(f"{code}: {status_code_count[code]}")

except KeyboardInterrupt:
    pass  # Allow the script to exit gracefully on CTRL + C

finally:
    # Print the final statistics
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_count.keys()):
        if status_code_count[code] > 0:
            print(f"{code}: {status_code_count[code]}")

