import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();

        int[] alpha = new int[26];
        for (int i = 0; i < s.length(); i++) {
            int index = s.charAt(i) - 97;
            alpha[index]++;
        }

        for (int a : alpha) {
            System.out.print(a + " ");
        }
        sc.close();
    }
}