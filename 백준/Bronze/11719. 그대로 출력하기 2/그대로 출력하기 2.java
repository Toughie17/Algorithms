import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String t = null;
        while ((t = br.readLine()) != null) {
            bw.write(t);
            bw.newLine();
        }
        bw.flush();
    }
}