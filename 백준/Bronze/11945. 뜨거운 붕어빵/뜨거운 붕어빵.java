import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int row = sc.nextInt();
        int col = sc.nextInt();

        if (col > 0) {
            for(int i = 0; i < row; i++) {
                char[] arr = sc.next().toCharArray();
                for(int j = col-1; j>=0; j--) {
                    System.out.print(arr[j]);
                }
                System.out.println();
            }
        }
    }
}