package book;

import java.util.List;
import java.util.Map;
import book.file.BookFileReader;

/**
 * Represents a book to be cataloged.
 * @author lbrandon
 *
 */
public class Book {

	/**
	 * Title of book.
	 */
	private String title;
	
	/**
	 * Author of book.
	 */
	private String author;
	
	/**
	 * Lines in book.
	 */
	private List<String> lines;
	
	/**
	 * Count of words in book.
	 */
	private int wordCount;
	
	/**
	 * Count of each word in book.
	 */
	private Map<String, Integer> wordCounts;
	
	/**
	 * Creates a book with the given list of lines.
	 * Parses the title and author of the book.
	 * Sets the total count of words, and the count of each word in the book.
	 * @param lines of text
	 */
	public Book(List<String> lines) {
		this.lines = lines;
		this.setTitleAndAuthor();
		this.countWords();
	}
	
	/**
	 * Parses the title and author of the book in the list of lines.
	 * 
	 * To get the title of the book, looks for "Title:" at the beginning of a line, and gets the text after it.
	 * Example: 
	 * - Title: Catcher in the Rye
	 * - "Catcher in the Rye" becomes the book title
	 * 
	 * To get the author of the book, looks for "Author:" at the beginning of a line, and gets the text after it.
	 * Example:
	 * - Author: J.D. Salinger
	 * - "J.D. Salinger" becomes the author
	 * 
	 * Note, there should only be, at most, one title and/or author of the book in the list of lines.
	 * i.e. "Title:" and/or "Author:" will never show up more than once in the list of lines.
	 */
	private void setTitleAndAuthor() {
		
		// TODO Implement method
		// Hint: Iterate over each line in the book and look for lines starting with "Title:" and "Author:"
		// If a line starts with "Title:", get the text after it, and set this.title.
		// -- Make sure to strip() the title of all leading and trailing whitespace.
		// If a line starts with "Author:", get the text after it, and set this.author.
		// -- Make sure to strip() the author's name of all leading and trailing whitespace.
		
	}
	
	/**
	 * Gets the book title.
	 * Returns null if title doesn't exist.
	 * @return the title
	 */
	public String getTitle() {
		// TODO Implement method

		return null;
	}

	/**
	 * Gets the book author.
	 * Returns null if author doesn't exist.
	 * @return the author
	 */
	public String getAuthor() {
		// TODO Implement method

		return null;
	}
	
	/**
	 * Counts the total number of words in the list of lines.
	 * Also counts the number of times each word appears in the list of lines.  
	 * Does not consider case when comparing words.  e.g. "Love" is the same word as "love".
	 * 
	 * For consistency, words should include a sequence of any of the following characters:
	 * a-z, A-Z, 0-9, _, %, +, -
	 * 
	 * Examples of valid words:
	 *  hello
	 *  HI
	 *  two-fold
	 *  34%
	 *  very_good
	 *  678
	 *  EdWaRd
	 *  1+2
	 */
	private void countWords() {
		
		// TODO Implement method
		// Hint: Iterate over each line in the book and look for valid words containing specific characters.
		// To do this, check for subsequences of any of the allowed characters above. (You can use a character 
		// class regular expression.)
		//
		// Initialize this.wordCounts as a TreeMap.  Add key:value pairs to this.wordCounts 
		// where each key is a word and the value is the count of the word.  Remember, ignore
		// case when counting the words. (You could convert them all to lowercase.)
		// Also, set the value of this.wordCount to the total number of words.
		
	}
	
	/**
	 * Gets total count of all words.
	 * @return count of all words
	 */
	public int getTotalWordCount() {
		// TODO Implement method

		return 0;
	}

	/**
	 * Gets unique count of words.
	 * Does not consider case when counting words.  e.g. "Love" is the same word as "love".
	 * 
	 * @return count of all words
	 */
	public int getUniqueWordCount() {
		// TODO Implement method

		return 0;
	}
	
	/**
	 * Gets the count of the given word.
	 * Returns 0 if the given word doesn't exist.
	 * @param word to count
	 * @return count of given word
	 */
	public int getSpecificWordCount(String word) {
		
		// TODO Implement method

		return 0;
	}
	
	/**
	 * Gets the book lines.
	 * @return lines in book
	 */
	public List<String> getLines() {
		return this.lines;
	}
	
	///// DO NOT CHANGE CODE IN MAIN METHOD! /////
	public static void main(String[] args) {
	    
		//load and parse book files
		List<String> catInTheHat = BookFileReader.parseFile("the_cat_in_the_hat_snippet.txt");
		List<String> warAndPeace = BookFileReader.parseFile("war_and_peace.txt");
		List<String> siddhartha = BookFileReader.parseFile("siddhartha.txt");
		
		//create instances of book with lists above
		Book catInTheHatBook = new Book(catInTheHat);
		Book warAndPeaceBook = new Book(warAndPeace);
		Book siddharthaBook = new Book(siddhartha);
			
		//get lines from books
		System.out.println("\nGET FIRST 3 LINES");
		System.out.println(catInTheHatBook.getLines().subList(0, 3));
		System.out.println(warAndPeaceBook.getLines().subList(0, 3));
		System.out.println(siddharthaBook.getLines().subList(0, 3));
				
		//get titles of books
		System.out.println("\nGET TITLES");
		String catInTheHatBookTitle = catInTheHatBook.getTitle();
		System.out.println(catInTheHatBookTitle);
		String warAndPeaceBookTitle = warAndPeaceBook.getTitle();
		System.out.println(warAndPeaceBookTitle);
		String siddharthaBookTitle = siddharthaBook.getTitle();
		System.out.println(siddharthaBookTitle);
		
		//get authors of books
		System.out.println("\nGET AUTHORS");
		String catInTheHatBookAuthor = catInTheHatBook.getAuthor();
		System.out.println(catInTheHatBookAuthor);
		String warAndPeaceBookAuthor = warAndPeaceBook.getAuthor();
		System.out.println(warAndPeaceBookAuthor);
		String siddharthaBookAuthor = siddharthaBook.getAuthor();
		System.out.println(siddharthaBookAuthor);
		
		//get total word counts from books
		System.out.println("\nGET TOTAL WORD COUNTS");
		System.out.println(catInTheHatBook.getTotalWordCount());
		System.out.println(warAndPeaceBook.getTotalWordCount());
		System.out.println(siddharthaBook.getTotalWordCount());
		
		//get total word counts from books
		System.out.println("\nGET UNIQUE WORD COUNTS");
		System.out.println(catInTheHatBook.getUniqueWordCount());
		System.out.println(warAndPeaceBook.getUniqueWordCount());
		System.out.println(siddharthaBook.getUniqueWordCount());
		
		//get specific word counts from books
		System.out.println("\nGET SPECIFIC WORD COUNTS");
		System.out.println(catInTheHatBook.getSpecificWordCount("sit"));
		System.out.println(warAndPeaceBook.getSpecificWordCount("love"));
		System.out.println(siddharthaBook.getSpecificWordCount("hate"));
	}
	
}
