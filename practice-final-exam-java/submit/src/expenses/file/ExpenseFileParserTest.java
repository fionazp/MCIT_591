package expenses.file;

import static org.junit.Assert.assertEquals;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class ExpenseFileParserTest {

	//list to store lines from expenses_sample.txt file
	List<String> expensesListSample;
	
	//list to store lines from expenses.txt file
	List<String> expensesList;
		
	@BeforeEach
	void setUp() throws Exception {
		
		////////////////////////////////////////////////
		///// DO NOT MODIFY THE TEST CODE BELOW! ///////
		
		//load expenses_sample.txt file and get list of expenses
		this.expensesListSample = ExpenseFileReader.loadExpenses("expenses_sample.txt");
				
		//load expenses.txt file and get list of expenses
		this.expensesList = ExpenseFileReader.loadExpenses("expenses.txt");
		
		///// DO NOT MODIFY THE TEST CODE ABOVE! ///////
		////////////////////////////////////////////////
		
	}

	@Test
	void testParseExpenses() {
		
		////////////////////////////////////////////////
		///// DO NOT MODIFY THE TEST CODE BELOW! ///////
		
		//parse list of sample expenses into a list of expense maps
		List<Map<Integer, Double>> monthlyExpensesSample = ExpenseFileParser.parseExpenses(this.expensesListSample);
		
		//create arraylist with expected expense maps
		List<Map<Integer, Double>> expectedMonthlyExpensesSample = new ArrayList<Map<Integer, Double>>();
		
		Map<Integer, Double> sampleExpenseMap = new HashMap<Integer, Double>();
		sampleExpenseMap.put(1, 57.38);
		expectedMonthlyExpensesSample.add(sampleExpenseMap);
		
		sampleExpenseMap = new HashMap<Integer, Double>();
		sampleExpenseMap.put(2, 32.88);
		expectedMonthlyExpensesSample.add(sampleExpenseMap);
		
		sampleExpenseMap = new HashMap<Integer, Double>();
		sampleExpenseMap.put(3, 44.64);
		expectedMonthlyExpensesSample.add(sampleExpenseMap);
		
		//compare to actual expense maps
		assertEquals(expectedMonthlyExpensesSample, monthlyExpensesSample);
		
		///// DO NOT MODIFY THE TEST CODE ABOVE! ///////
		////////////////////////////////////////////////
		
		
		// TODO insert 1 additional test case
        // Hint(s): Parse and test list of expenses from expenses.txt
			
	}

}
