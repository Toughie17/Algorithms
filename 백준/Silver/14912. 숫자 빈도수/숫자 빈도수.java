import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int d = sc.nextInt();

        int[] count = new int[10];

        for(int i = 1; i <= n; i++) {
            char[] tmp = Integer.toString(i).toCharArray();

            for(int j = 0; j < tmp.length; j++){
                int index = Character.getNumericValue(tmp[j]);
                count[index]++;
            }
        }
        System.out.println(count[d]);
    }
}