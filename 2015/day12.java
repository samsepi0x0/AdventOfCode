import java.io.*;
import java.util.*;

public class day12{
    public static void main(String args[])throws IOException{
        BufferedReader br = new BufferedReader(new FileReader("input_12.txt"));
        String line = br.readLine();
        day12 obj = new day12();
        // int part1 = obj.solvePart1(line);
        obj.solvePart2(line);
    }
    public int solvePart1(String s){
        String line = "";
        for(int i = 0; i < s.length(); i++){
            char ch = s.charAt(i);
            if (ch == '-' || Character.isDigit(ch)){
                line += ch;
            } else {
                line += " ";
            }
        }
        int sum = 0;
        StringTokenizer st = new StringTokenizer(line);
        while(st.hasMoreTokens()){
            String temp = st.nextToken();
            sum += Integer.parseInt(temp);
        }
        System.out.println("Sum of all numbers: " + sum);
        return sum;
    }
    public void solvePart2(String s){
        // NO JSON in java right now so will switch to python for the time being.
    }
}