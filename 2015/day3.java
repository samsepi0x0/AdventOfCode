import java.io.*;
import java.util.*;
public class day3{
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new FileReader("input_3.txt"));
        String line = br.readLine();
        part1(line);
        part2(line);
    }
    public static void part1(String line){
        ArrayList<ArrayList<Integer>> arr = new ArrayList<ArrayList<Integer>>();
        int x = 0;
        int y = 0;
        arr.add(new ArrayList<Integer>(Arrays.asList(x,y)));
        for(int i = 0; i < line.length(); i ++){
            char ch = line.charAt(i);
            if(ch == '^')
                y += 1;
            else if(ch == 'v')
                y -= 1;
            else if(ch == '>')
                x += 1;
            else
                x -= 1;
            arr.add(new ArrayList<Integer>(Arrays.asList(x,y)));
        }
        Set<ArrayList<Integer>> t = new HashSet<ArrayList<Integer>>();
        for(ArrayList<Integer> s: arr){
            t.add(s);
        }
        System.out.println("Houses Visited: " + t.size());
    }
    public static void part2(String line){
        ArrayList<ArrayList<Integer>> arr = new ArrayList<ArrayList<Integer>>();
        int x = 0;
        int y = 0;
        int x_r = 0;
        int y_r = 0;
        arr.add(new ArrayList<Integer>(Arrays.asList(x,y)));
        for(int i = 0; i < line.length(); i ++){
            if(i % 2 == 0){
                char ch = line.charAt(i);
                if(ch == '^')
                    y += 1;
                else if(ch == 'v')
                    y -= 1;
                else if(ch == '>')
                    x += 1;
                else
                    x -= 1;
                arr.add(new ArrayList<Integer>(Arrays.asList(x,y)));
            } else {
                char ch = line.charAt(i);
                if(ch == '^')
                    y_r += 1;
                else if(ch == 'v')
                    y_r -= 1;
                else if(ch == '>')
                    x_r += 1;
                else
                    x_r -= 1;
                arr.add(new ArrayList<Integer>(Arrays.asList(x_r,y_r)));    
            }
        }
        Set<ArrayList<Integer>> t = new HashSet<ArrayList<Integer>>();
        for(ArrayList<Integer> s: arr){
            t.add(s);
        }
        System.out.println("Houses Visited: " + t.size());
    }
}