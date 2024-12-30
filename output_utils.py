def generate_text(posts, search_term):
    text = f"Search Term: {search_term}\n\n"
    for subject, date, body in posts:
        date_str = date.split(' ')[0]  # Extract date (YYYY-MM-DD)
        text += f"{body}\n\n"
        text += "---\n\n"
    return text

def export_text(text, output_file):
    with open(output_file, 'w') as f:
        f.write(text)