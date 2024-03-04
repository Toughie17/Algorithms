import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        int b = scanner.nextInt();

        // 조건문
//        if (a > b) {
//            System.out.println('>');
//        } else if (a < b) {
//            System.out.println('<');
//        } else {
//            System.out.println("==");
//        }

        //삼항 연산자
        System.out.println( (a > b) ? '>' : (a < b) ?  '<' : "==");
    }
}