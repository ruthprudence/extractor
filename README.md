# Email Extraction Tool
## Overview
This tool extracts email posts from a mailbox file (.mbox) based on a user-provided search term. It displays progress, handles encoding issues, and exports results to a text file.
## Design Choices
### Modularization
The code is broken into three modules:
1. __extract_entries.py__: Main script handling user input, search term validation, and processing.
1. __extract_posts.py__: Module responsible for extracting posts from the mailbox file.
1. __output_utils.py__: Module for generating and exporting output text.
### Trade-Offs
- __Performance vs. Readability__: We prioritized readability and maintainability over performance, using clear variable names and functions.
- __Error Handling__: We focused on handling common errors, such as encoding issues, but may not cover all edge cases.
### Future Improvements
- __Optimize Performance__: Investigate parallel processing or more efficient algorithms.
- __Enhance Error Handling__: Expand error handling to cover more scenarios.
- __User Interface__: Develop a more intuitive user interface.
### Technical Details
- __Python 3.x__: Written in Python 3.x for compatibility and ease of use.
- __mailbox and email Libraries__: Utilized for parsing mailbox files and email messages.
- __unicodedata__: Used for handling encoding issues.
### Usage
1. Run python3 extract_entries.py to start the tool.
1. Enter a search term (or type 'quit' to exit).
1. Optionally, provide a time limit (in seconds) as a command-line argument (e.g., python3 extract_entries.py 10).

### License
This project is licensed under the MIT License.

## Contact
For questions, feedback, or contributions, please reach out.