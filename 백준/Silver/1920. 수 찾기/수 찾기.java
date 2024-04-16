import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] A = new int[n];
        for (int i =0; i < n; i++) {
            A[i] = sc.nextInt();
        }
        Arrays.sort(A);
        int m = sc.nextInt();
        for(int i =0; i < m; i++) {
            int target = sc.nextInt();
            int start = 0;
            int end = A.length - 1;
            boolean find = false;

            while(start <=end) {
                int mid = (start + end) / 2;
                int mid_value = A[mid];

                if (mid_value > target) {
                    end = mid -1;
                } else if (mid_value < target) {
                    start = mid + 1;
                } else {
                    find = true;
                    break;
                }
            }
            if(find) {
                System.out.println(1);
            } else {
                System.out.println(0);
            }
        }
        sc.close();
    }
}