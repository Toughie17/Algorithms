import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int sum = 0;

        char[] arr = sc.next().toCharArray();
        for(char a : arr) {
//            sum += a - 48;
            sum += Character.getNumericValue(a);
        }
        System.out.println(sum);
    }
}