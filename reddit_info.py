from text_to_speech import save

title = """People of Reddit, test tiele?"""
answer = """Hello Test test blah blah blah"""

text = title+",,,,,,,,,,,,"+answer#"Haunted house actors of Reddit, "+title+",,,,,,,,,,,,"+
language = "en"  # Specify the language (IETF language tag)
output_file = "reddit.mp3"  # Specify the output file (only accepts .mp3)

def create_file():
    save(text, language, file=output_file, lang_check=True)