import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        while(true) {
            String input = br.readLine();
            if (input.equals("END")) {
                return;
            }

            char[] arr = input.toCharArray();

            for(int i = arr.length-1; i >= 0; i--) {
                bw.write(arr[i]);
            }
            bw.write("\n");
            bw.flush();
        }
    }
}