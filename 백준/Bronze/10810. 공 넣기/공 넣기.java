import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        int[] arr = new int[n];

        for (int p =0; p < m; p++) {
            int i = sc.nextInt();
            int j = sc.nextInt();
            int k = sc.nextInt();
            for (int t = i-1; t < j; t++) {
                arr[t] = k;
            }
        }
        sc.close();
        for (int num : arr) {
            System.out.print(num + " ");
        }
    }
}