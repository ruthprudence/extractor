import time
import json
import mailbox
import email
import unicodedata
import os

def extract_posts(mbox_file, search_term):
    posts = []
    mbox = mailbox.mbox(mbox_file)
    total_items = len(mbox)
    start_time = time.time()
    
    for i, msg in enumerate(mbox):
        parsed_msg = email.message_from_string(msg.as_string())
        subject = parsed_msg['Subject']
        body = ''
        if parsed_msg.is_multipart():
            for part in parsed_msg.walk():
                if part.get_content_type() == 'text/plain':
                    body = part.get_payload(decode=True).decode('utf-8', errors='ignore')
                    break
        else:
            body = parsed_msg.get_payload(decode=True).decode('utf-8', errors='ignore')
        body = unicodedata.normalize('NFKD', body)
        if search_term in body:
            posts.append((subject, body))
        
        # Display progress
        elapsed_time = time.time() - start_time
        percentage_completed = (i + 1) / total_items * 100
        print(f"Processed {i+1}/{total_items} ({percentage_completed:.2f}%). Elapsed: {elapsed_time:.2f}s", end='\r', flush=True)
    
    print()  # Newline for readability
    return posts

def generate_text(posts, search_term):
    text = f"Search Term: {search_term}\n\n"
    for subject, body in posts:
        text += f"{subject}\n\n"
        text += f"{body}\n\n"
        text += "---\n\n"
    return text

def export_text(text, output_file):
    with open(output_file, 'w') as f:
        f.write(text)

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
    posts = extract_posts(mbox_file, search_term)
    text = generate_text(posts, search_term)
    export_text(text, f"{search_term}.txt")
    print(f"Total posts processed: {len(posts)}")

if __name__ == "__main__":
    main()