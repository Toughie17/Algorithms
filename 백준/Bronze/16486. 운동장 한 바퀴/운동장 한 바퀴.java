import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int width = sc.nextInt();
        int halfRound = sc.nextInt();
        sc.close();
        
        double pie = 3.141592;
        double result = (2 * pie * halfRound) + (2 * width);
        System.out.println(result);
    }
}