
import junit.framework.TestCase;

public class TestsBowlingMachine extends TestCase {	
	
	BowlingMachine horrible, horribleSmall, horribleMedium, play1, twoplays, sparePlus, strike1;
	
	//@Override
	public void setUp() {
		horrible = new BowlingMachine
    			(
    			"[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]"
    			);
		horribleSmall = new BowlingMachine ( "[0,0]" );
		horribleMedium = new BowlingMachine ( "[1,0]" );
		play1 = new BowlingMachine ( "[1,2]" );
		twoplays = new BowlingMachine ( "[1,2],[4,6]" );
		sparePlus = new BowlingMachine ( "[4,6],[1,2]" );
		strike1 = new BowlingMachine ( "[10,0],[1,2]" );
		
	}
	
	//@Test
    public void testHorriblePlay() {
    	assertEquals(horrible.calculatePlay(), 0);    	
    }
    
    public void testOneHorriblePlay() {
    	assertEquals(horribleSmall.calculatePlay(), 0);  
    }
    
	public void testMediumHorriblePlay(){
		assertEquals(horribleMedium.calculatePlay(), 1);
	}

	public void testOnePlay(){
		assertEquals(play1.calculatePlay(), 3);
	}
	
	public void testTwoPlays(){
		assertEquals(twoplays.calculatePlay(), 13);
	}
	
	public void testSpareAndAnother(){
		assertEquals(sparePlus.calculatePlay(), 14 );
	}
	
	public void testStrike(){
		assertEquals(strike1.calculatePlay(), 16 );
	}
	
	
}
