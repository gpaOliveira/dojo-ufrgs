import java.awt.List;
import java.util.ArrayList;


public class BowlingMachine {

	private String completePlay;
	
	public BowlingMachine(String completePlay) {
		this.setCompletePlay(completePlay);
	}
	
	public int calculatePlay()
	{
		ArrayList<Integer> playScore = new ArrayList<Integer>();
		//ArrayList<String> plays = new ArrayList<String>();
		String plays[];
		
		boolean wasSpare = false;
		boolean wasStrike = false;
		
		plays = completePlay.split("],");
		for(int i = 0; i < plays.length; i++){
		
			int scoreBuffer = 0;
			String firstPlay = plays[i].substring(1, plays[i].indexOf(","));
			String secondPlay = plays[i].substring(plays[i].indexOf(",")+1,4);
			
			int score1 = Integer.parseInt(firstPlay);
			int score2 = Integer.parseInt(secondPlay);
			
			if(wasStrike)
			{
				playScore.add( score1 );
				playScore.add( score2 );
			}
			
			if (wasSpare) {
				playScore.add( score1 );
			}
			
			playScore.add( score1 );
			playScore.add( score2 );			

			scoreBuffer += score1 + score2;
			
			if (score1 == 10)
			{
				wasStrike = true;
			}
			else
			{
				wasStrike = false;				
				
				if (scoreBuffer == 10) {
					wasSpare = true; //yeah cris^2
				} else {
					wasSpare = false;
				}
			}	
			
		}
		
		int sum = 0;
		
		for(Integer i:playScore){
			sum += i;
		}	
		
		return sum;
		
		/*
		if(completePlay == "[1,2]")
			return 3;		
		else if (completePlay == "[1,0]")
			return 1;
		else
			return 0;
		*/
	}

	private void setCompletePlay(String completePlay) {
		this.completePlay = completePlay;
	}

	private String getCompletePlay() {
		return completePlay;
	}
	
	
}
