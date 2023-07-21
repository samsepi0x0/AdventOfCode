import java.io.*;
public class day5{
    public static void main(String args[]) throws IOException{
        part1();
        part2();
    }
    public static void part2() throws IOException{
        BufferedReader br = new BufferedReader(new FileReader("input_5.txt"));
        int count = 0;
        String line = "";
        while((line = br.readLine()) != null){
            boolean cond1 = false;
            boolean cond2 = false;

            for(int i = 0; i <= line.length() - 2; i++){
                char ch = line.charAt(i);
                char ch2 = line.charAt(i+1);
                for(int j = i + 2; j < line.length()-1; j++){
                    char copy_ch = line.charAt(j);
                    char copy_ch2 = line.charAt(j+1);
                    if(ch == copy_ch && ch2 == copy_ch2){
                        cond1 = true;
                        break;
                    }
                }
                if(cond1)
                    break;
            }

            for(int i = 0; i < line.length()-2; i++){
                char ch1 = line.charAt(i);
                char ch2 = line.charAt(i+1);
                char ch3 = line.charAt(i+2);
                if(ch1 == ch3){

                    cond2 = true;
                    break;
                }
            }
            if(cond1 && cond2)
                count += 1;
        }
        System.out.println("Nice Strings count (NEW WAY): " + count);
    }
    public static void part1() throws IOException{
        BufferedReader br = new BufferedReader(new FileReader("input_5.txt"));
        int count = 0;
        String line = "";
        while((line = br.readLine()) != null){
            int vowel_count = 0;
            for(int i = 0; i < line.length(); i++){
                char ch = line.charAt(i);
                if(ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u')
                    vowel_count += 1;
            }
            boolean cond2 = false;
            boolean cond3 = false;
            for(int i = 0; i < line.length()-1; i++){
                char ch = line.charAt(i);
                char ch2 = line.charAt(i+1);
                if(ch == ch2)
                    cond2 = true;
                if((ch == 'a' && ch2 == 'b') ||(ch == 'c' && ch2 == 'd') ||(ch == 'p' && ch2 == 'q') ||(ch == 'x' && ch2 == 'y'))
                    cond3 = true;
            }
            
            if(vowel_count >= 3 && cond2 && (!cond3)){
                count += 1;
            }
            line = "";
        }
        System.out.println("Nice Strings count (OLD WAY): " + count);
    }
}