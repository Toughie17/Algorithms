import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        sc.close();
        int[] result = new int[k];
        int count = 0;

        for (int i = 1; i <= n; i++) {
            if(n % i == 0) {
                if (count < k) {
                    result[count] = i;
                    count++;
                }
            }
            if(count > k) {
                break;
            }
        }

        if(result[k-1] != 0) {
            System.out.println(result[k-1]);
        } else {
            System.out.println(0);
        }
    }
}