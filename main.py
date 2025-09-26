from stats import get_word_count, count_letters, sort_dict
import sys

def get_book_text(path_to_file):
	with open(path_to_file) as f:
		file_contents = f.read()
		f.close()
	return file_contents

def main():
	if len(sys.argv) < 2:
		print('Usage: python3 main.py <path_to_book>')
		sys.exit(1)

	contents = get_book_text(sys.argv[1])
	num_words = get_word_count(contents)
	letters = count_letters(contents)
	sorted_letters = sort_dict(letters)
	print('============ BOOKBOT ============')
	print(f'Analyzing book found at {sys.argv[1]}...')
	print('----------- Word Count ----------')
	print(f'Found {num_words} total words')
	print('--------- Character Count -------')
	for item in sorted_letters:
		print(f'{item}: {sorted_letters[item]}')

main()
