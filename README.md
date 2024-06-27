# README

## Overview

This simple Python script contains functions to read text from a file and find patterns such as times, URLs, and dates in the text. Additionally, it includes unit tests to verify the functionality of these functions.

## Functions

### `read_file(filename)`

- **Description**: Reads a file and returns its content as a list of lines.
- **Parameters**: `filename` (str) - The name of the file to read.
- **Returns**: A list of lines from the file.

### `find_times(string_list)`

- **Description**: Finds all valid times in a list of strings.
- **Parameters**: `string_list` (list) - A list of strings to search for times.
- **Returns**: A list of valid times in the format `HH:MM am/pm`.

### `find_urls(string_list)`

- **Description**: Finds all valid URLs in a list of strings.
- **Parameters**: `string_list` (list) - A list of strings to search for URLs.
- **Returns**: A list of valid URLs starting with `http://` or `https://`.

### `find_dates(string_list)`

- **Description**: Finds all valid dates in a list of strings.
- **Parameters**: `string_list` (list) - A list of strings to search for dates.
- **Returns**: A list of valid dates in various formats (`MM/DD/YYYY`, `MM-DD-YYYY`, `DD.MM.YYYY`).

## Unit Tests

The script includes unit tests to verify the correctness of the functions using the `unittest` framework. The tests are defined in the `TestAllMethods` class and cover the following:

- `test_find_times`: Tests the `find_times` function.
- `test_find_urls`: Tests the `find_urls` function.
- `test_find_dates`: Tests the `find_dates` function.

## Usage

To run the script and execute the unit tests, use the following command:

```bash
python script_name.py
```

Replace `script_name.py` with the actual name of the script file.

The unit tests will output the results to the console, showing which tests passed and which failed.

## File Structure

- `script_name.py`: The main script file containing the functions and unit tests.
- `alice_in_wonderland.txt`: A sample text file used for testing (ensure this file is in the same directory as the script).

## Notes

- Ensure that the required text file (`alice_in_wonderland.txt`) is present in the same directory as the script.
- The regex patterns used in the functions are designed to handle common formats for times, URLs, and dates, but may need adjustments for specific use cases.