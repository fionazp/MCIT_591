package book.file;

import static org.junit.Assert.assertEquals;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import book.file.BookFileReader;

class BookFileReaderTest {
	
	// lists to store lines from different loaded book files
	List<String> catInTheHat;
	List<String> warAndPeace;
	List<String> siddhartha;

	@BeforeEach
	void setUp() throws Exception {
		
		////////////////////////////////////////////////
		///// DO NOT MODIFY THE TEST CODE BELOW! ///////
		
		//load and parse cat in the hat snippet book file
		this.catInTheHat = BookFileReader.parseFile("the_cat_in_the_hat_snippet.txt");
		
		//load and parse war and peace book file
		this.warAndPeace = BookFileReader.parseFile("war_and_peace.txt");
		
		//load and parse siddhartha book file
		this.siddhartha = BookFileReader.parseFile("siddhartha.txt");
    
		///// DO NOT MODIFY THE TEST CODE ABOVE! ///////
		////////////////////////////////////////////////
		
	}

	@Test
	void testParseFile() {

		////////////////////////////////////////////////
		///// DO NOT MODIFY THE TEST CODE BELOW! ///////
		
		//create array with first 10 expected lines of cat in the hat snippet
		String[] expectedLines1Array = {
			"Title: The Cat in the Hat",
			"Author: Dr. Seuss",
			"The sun did not shine.",
			"It was too wet to play.",
			"So we sat in the house",
			"All that cold, cold, wet day.",
			"I sat there with Sally.",
			"We sat there, we two.",
			"And I said, \"How I wish",
			"We had something to do!\""
		};
		List<String> expectedLines1 = new ArrayList<String>(Arrays.asList(expectedLines1Array));
		
		//compare to first 10 actual lines of cat in the hat snippet
		assertEquals(expectedLines1, this.catInTheHat.subList(0, 10));
		
		///// DO NOT MODIFY THE TEST CODE ABOVE! ///////
		////////////////////////////////////////////////
		
		
		// TODO insert 2 additional test cases
        // Hint(s): Test war and peace and siddhartha book files
	}
}
