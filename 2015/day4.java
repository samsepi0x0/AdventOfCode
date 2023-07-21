import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
public class day4{
    public static String getMd5(String input)
    {
        try {
 
            // Static getInstance method is called with hashing MD5
            MessageDigest md = MessageDigest.getInstance("MD5");
 
            // digest() method is called to calculate message digest
            // of an input digest() return array of byte
            byte[] messageDigest = md.digest(input.getBytes());
 
            // Convert byte array into signum representation
            BigInteger no = new BigInteger(1, messageDigest);
 
            // Convert message digest into hex value
            String hashtext = no.toString(16);
            while (hashtext.length() < 32) {
                hashtext = "0" + hashtext;
            }
            return hashtext;
        }
 
        // For specifying wrong message digest algorithms
        catch (NoSuchAlgorithmException e) {
            throw new RuntimeException(e);
        }
    }
    public static void main(String args[]) throws NoSuchAlgorithmException
    {
        String s = "iwrupvqb";
        int i = 1;
        while(true){
            String temp = s + i;
            String hash = getMd5(temp);
            // if(hash.startsWith("00000")){
            //     break;
            // }
            if(hash.startsWith("000000")){
                break;
            }
            i += 1;
        }
        System.out.println("Value: " + i);
    }
}