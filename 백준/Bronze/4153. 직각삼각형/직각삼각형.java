import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while(true) {
            int[] arr = new int[3];
            arr[0] = sc.nextInt();
            arr[1] = sc.nextInt();
            arr[2] = sc.nextInt();

            if (arr[0] == 0 && arr[1] ==0 && arr[2] ==0) {
                sc.close();
                break;
            }
            Arrays.sort(arr);
            int sum = (arr[0] * arr[0]) + (arr[1] * arr[1]);
            int max = arr[2] * arr[2];

            if(sum == max) {
                System.out.println("right");
            } else {
                System.out.println("wrong");
            }
        }
    }
}