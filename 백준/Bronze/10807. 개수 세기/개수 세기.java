import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        //개수
        int count = sc.nextInt();
        sc.nextLine();
        String input = sc.nextLine();
        //공백 구분 정수
        int target = sc.nextInt();

        int result = 0;
        String[] numbers = input.split(" ");

        for (String number : numbers) {
            if (Integer.parseInt(number) == target) {
                result++;
            }
        }
        System.out.println(result);
        sc.close();
    }
}