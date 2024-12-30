import time
import mailbox
import email
import unicodedata

def extract(mbox_file, search_term, max_time=None):
    posts = []
    mbox = mailbox.mbox(mbox_file)
    total_items = len(mbox)
    start_time = time.time()
    
    for i, msg in enumerate(mbox):
        if max_time and time.time() - start_time > max_time:
            break
        
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