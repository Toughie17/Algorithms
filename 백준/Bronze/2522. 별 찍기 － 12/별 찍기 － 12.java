import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.close();
        for (int i =0; i < 2 * n -1; i++) {
            for (int j = 0; j < n; j++) {
                if((i < n && i + j >= n - 1) || (i >= n && i - j < n)){
                    System.out.print("*");
                } else {
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
    }
}