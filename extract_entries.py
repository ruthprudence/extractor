import sys
from extract_posts import extract
from output_utils import generate_text, export_text

import time
import sys
import extract_posts
import output_utils

def get_search_term():
    while True:
        search_term = input("Enter search term (or type 'quit' to exit): ")
        if search_term.lower() == 'quit':
            print("Exiting...")
            exit()
        if len(search_term) > 0:
            return search_term
        print("Please enter a non-empty search term.")

def main():
    mbox_file = '/Users/ruth/Desktop/GMail_Backup/allMail.mbox'
    search_term = get_search_term()
    print(f"Searching for: {search_term}")
    
    if len(sys.argv) > 1:
        max_time = int(sys.argv[1])
    else:
        max_time = None
    
    posts = extract_posts.extract(mbox_file, search_term, max_time)
    posts.sort(key=lambda x: x[1])  # Sort by date
    output_text = output_utils.generate_text(posts, search_term)
    output_utils.export_text(output_text, f"{search_term}.txt")
    print(f"Total posts processed: {len(posts)}")

if __name__ == "__main__":
    main()