import java.io.*;
import java.util.*;
import java.lang.Thread;

class day11{
    public static void main(String args[])throws IOException{
        day11 obj = new day11();
        obj.solve("vzbxkghb"); // part1
        obj.solve("vzbxxyzz"); // part2
    }
    public void solve(String s)throws IOException{
        int n = s.length();
        int indexer = n - 1;
        String anim= "|/-\\";
        int start = (int)('h') - 97;

        for(int i = 0; ; i++){
            String data = "\r" + anim.charAt(i % anim.length()) + " ";
            System.out.write(data.getBytes());

            char[] ch = s.toCharArray();
            int j = 1;    
            // increment the string.
            ch[n-1] += 1;
            // if(ch[n-1] > 'z'){
            //     ch[n-1-1] = ch[n-1-1] + (ch[n-1] / 122);
            //     if (ch[n-1-1] > 'z'){
            //         ch[n-1-2] = ch[n-1-2] + (ch[n-1-1] / 122);
            //         if (){

            //         }
            //         ch[n-1-2] = 'a';
            //     }
            //     ch[n-1] = 'a';
            // }

            while(ch[n-j] > 'z'){
                ch[n-j-1] += 1;
                ch[n-j] = 'a';
                j += 1;
            }
            
            s = new String(ch);
            // System.out.println("New: " + s);
            
            if (checkConditions(s)){
                System.out.println("New Password: " + s);
                break;
            }
        }

    }
    public boolean checkConditions(String s){
        int n = s.length();
        char stored = ' ';
        boolean check1, check2, check3;
        check1 = check2 = check3 = false;
        for(int i = 0; i < n; i++){
            if (s.charAt(i) == 'i' || s.charAt(i) == 'o' || s.charAt(i) == 'l')
                return false;
            if (i < n-2){
                char ch1 = s.charAt(i);
                char ch2 = s.charAt(i+1);
                char ch3 = s.charAt(i+2);

                if (ch1 + 1 == ch2 && ch1 + 2 == ch3)
                    check1 = true;
            }
        }
        check2 = true;
        for(int i = 0; i < n-1; i += 1){
            if (s.charAt(i) == s.charAt(i+1)){
                if (stored == ' '){
                    stored = s.charAt(i);
                    i += 1;
                    continue;
                } else if (s.charAt(i) != stored){
                    check3 = true;
                    break;
                }
            }
        }
        return check1 & check2 & check3;
    }
}