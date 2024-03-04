import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int x = scanner.nextInt();
        scanner.nextLine();

        String arr = scanner.nextLine();
        String[] inputArr = arr.split(" ");

        int[] numbers = new int[n];
        for(int i = 0; i < n; i++) {
            numbers[i] = Integer.parseInt(inputArr[i]);
        }

        for (int number : numbers) {
            if (number < x) {
                System.out.printf("%d ",number);
            }
        }
        scanner.close();
    }
}