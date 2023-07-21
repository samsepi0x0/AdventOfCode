import java.io.*;
import java.util.*;
class day2{
    public static void main(String args[])throws IOException{
        part1();

    }
    public static void part1()throws IOException{
        BufferedReader br = new BufferedReader(new FileReader("input_2.txt"));
        String line = "";
        int total_area = 0;
        int total_ribbon = 0;
        while((line=br.readLine())!=null){
            StringTokenizer st = new StringTokenizer(line, "x");
            int l = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            int h = Integer.parseInt(st.nextToken());
            int sq_area = (2*l*w) + (2*w*h) + (2*h*l);
            int m1 = Math.max(Math.max(l, w), h);
            int ribbon = 0;
            int vol = (l*w*h); // part 2
            int area = 1;
            if(m1 == l){
                area *= (w*h);
                ribbon += 2*(w+h); // part 2
            }
            else if(m1 == w){
                area *= (l*h);
                ribbon += 2*(l+h); // part 2
            }
            else if(m1 == h){
                area *= (l*w);
                ribbon += 2*(l+w); // part 2
            }
            total_area += sq_area + area;
            total_ribbon += ribbon + vol;
        }
        System.out.println("Area Required: " + total_area);
        System.out.println("Ribbon Required: " + total_ribbon);
    }
}