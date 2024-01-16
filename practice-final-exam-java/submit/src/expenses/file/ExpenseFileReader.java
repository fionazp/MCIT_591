package expenses.file;

import java.util.List;

/**
 * Manages the loading and parsing of expense files.
 * @author lbrandon
 *
 */
public class ExpenseFileReader {

	/**
	 * Loads the given filename and adds each line to a list.
	 * Ignores lines with only whitespace.
	 * @param fileName to load
	 * @return list of lines from the file
	 */
	public static List<String> loadExpenses(String fileName) {
		
		// TODO Implement method
		// Hint: Load and read each line in the file
		// Strip each line of leading and trailing whitespace
		// If a line is made up entirely of whitespace, ignore it
		// Return a list of lines
		
		return null;
	}
	
	///// DO NOT CHANGE CODE IN MAIN METHOD! /////
	public static void main(String[] args) {
		
		//load expenses_sample.txt file and get list of expenses
		List<String> expensesListSample = ExpenseFileReader.loadExpenses("expenses_sample.txt");
		
		//print sample expenses
		System.out.println("SAMPLE EXPENSES\n");
		for (String line : expensesListSample) {
			System.out.println(line);
		}
		
		//blank line
		System.out.println();
		
		//load expenses.txt file and get list of expenses
		List<String> expensesList = ExpenseFileReader.loadExpenses("expenses.txt");
		
		//print expenses 
		System.out.println("EXPENSES\n");
		for (String line : expensesList) {
			System.out.println(line);
		}
	}
}