import java.io.*;
import java.util.*;
public class day6{
    public static void main(String args[])throws IOException{
        part1();    
        part2();
    }
    public static void part2() throws IOException{
        BufferedReader br = new BufferedReader(new FileReader("input_6.txt"));
        String line;
        int arr[][] = new int[1000][1000];
        for(int i = 0; i < 1000; i++)
            for(int j = 0; j < 1000; j++)
                arr[i][j] = 0;
        while((line=br.readLine())!= null){
            StringTokenizer st = new StringTokenizer(line);
            String firstToken = st.nextToken();
            boolean toggle = false;
            boolean cond = false; //false is off, true is on
            if(firstToken.equalsIgnoreCase("turn")){
                toggle = false;
                String condition = st.nextToken();
                if(condition.equalsIgnoreCase("on")){
                    cond = true;
                } else {
                    cond = false;
                }
            } else {
                toggle = true;
            }
            StringTokenizer start = new StringTokenizer(st.nextToken(), ",");
            int x_0 = Integer.parseInt(start.nextToken());
            int y_0 = Integer.parseInt(start.nextToken());
            st.nextToken();
            StringTokenizer end = new StringTokenizer(st.nextToken(),",");
            int x_n = Integer.parseInt(end.nextToken());
            int y_n = Integer.parseInt(end.nextToken());
            //System.out.println(x_0 + "\t" + y_0 + "\t" + x_n + "\t" + y_n);

            for(int i = x_0; i <= x_n; i++){
                for(int j = y_0; j <= y_n; j++){
                    if(toggle){
                        arr[i][j] += 2; 
                    } else {
                        if(cond)
                            arr[i][j] += 1;
                        else{
                            arr[i][j] -= 1;
                            if(arr[i][j] < 0)
                                arr[i][j] = 0;
                        }
                    }
                }
            }
        }
        int count = 0;
        for(int i = 0; i < 1000; i++){
            for(int j = 0; j < 1000; j++){
                count += arr[i][j];
            }
        }
        System.out.println("On Brightness: " + count);
 
    }
    public static void part1() throws IOException{
        BufferedReader br = new BufferedReader(new FileReader("input_6.txt"));
        String line;
        int arr[][] = new int[1000][1000];
        for(int i = 0; i < 1000; i++)
            for(int j = 0; j < 1000; j++)
                arr[i][j] = 0;
        while((line=br.readLine())!= null){
            StringTokenizer st = new StringTokenizer(line);
            String firstToken = st.nextToken();
            boolean toggle = false;
            boolean cond = false; //false is off, true is on
            if(firstToken.equalsIgnoreCase("turn")){
                toggle = false;
                String condition = st.nextToken();
                if(condition.equalsIgnoreCase("on")){
                    cond = true;
                } else {
                    cond = false;
                }
            } else {
                toggle = true;
            }
            StringTokenizer start = new StringTokenizer(st.nextToken(), ",");
            int x_0 = Integer.parseInt(start.nextToken());
            int y_0 = Integer.parseInt(start.nextToken());
            st.nextToken();
            StringTokenizer end = new StringTokenizer(st.nextToken(),",");
            int x_n = Integer.parseInt(end.nextToken());
            int y_n = Integer.parseInt(end.nextToken());
            //System.out.println(x_0 + "\t" + y_0 + "\t" + x_n + "\t" + y_n);

            for(int i = x_0; i <= x_n; i++){
                for(int j = y_0; j <= y_n; j++){
                    if(toggle){
                        arr[i][j] = 1 - arr[i][j]; 
                    } else {
                        if(cond)
                            arr[i][j] = 1;
                        else
                            arr[i][j] = 0;
                    }
                }
            }
        }
        int count = 0;
        for(int i = 0; i < 1000; i++){
            for(int j = 0; j < 1000; j++){
                if(arr[i][j] == 1)
                    count += 1;
            }
        }
        System.out.println("On Lights: " + count);
    }
}