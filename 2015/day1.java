import java.io.*;
class day1{
	public static void main(String args[])throws IOException{
		BufferedReader br = new BufferedReader(new FileReader("input_1.txt"));
		String line = br.readLine();

		System.out.println(line);
		part1(line);
		part2(line);
	}
	public static void part1(String line){
		int score = 0;
		for(int i = 0; i < line.length(); i++){
			char ch = line.charAt(i);
			if(ch == '(')
				score += 1;
			else
				score -= 1;
		}
		System.out.println("Score: " + score);
	}
	public static void part2(String line){
		int score = 0;
		int i = 0;
		for(i = 0; i < line.length(); i++){
			char ch = line.charAt(i);
			if(ch == '(')
				score += 1;
			else if(ch == ')'){
				score -= 1;
				if(score == -1)
					break;
			}
		}
		System.out.println("Position: " + (i+1));
	}
}
