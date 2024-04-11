import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        sc.close();
        int[] arr = new int[str.length()];

        for(int i = 0; i < arr.length; i++) {
            arr[i] = Integer.parseInt(str.substring(i,i+1));
        }

        for(int i =0; i < str.length(); i++) {
            int maxIdx = i;
            for (int j = i+1; j < str.length(); j++) {
                if(arr[j] > arr[maxIdx]) {
                    maxIdx = j;
                }
            }

            if (arr[i] < arr[maxIdx]) {
                int tmp = arr[i];
                arr[i] = arr[maxIdx];
                arr[maxIdx] = tmp;
            }
        }

        for(int n : arr) {
            System.out.print(n);
        }
    }
}