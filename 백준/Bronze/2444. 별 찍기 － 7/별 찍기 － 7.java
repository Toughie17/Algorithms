import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int countUp =sc.nextInt();
        sc.close();
        for (int i =0; i < countUp; i++) {
            for(int l =0; l < countUp - i - 1; l++) {
                System.out.print(" ");
            }
            for(int s = 0; s < 2 * i + 1; s++) {
                System.out.print("*");
            }
//            for(int r =0; r < countUp -i; r++) {
//                System.out.print(" ");
//            }
            System.out.println();
        }
        for (int i =countUp - 1; i > 0; i--) {
            for(int l =0; l < countUp - i ; l++) {
                System.out.print(" ");
            }
            for(int s = 0; s < 2 * i - 1; s++) {
                System.out.print("*");
            }
//            for(int r =0; r < countUp -i; r++) {
//                System.out.print(" ");
//            }
            if(i > 1) {
                System.out.println();
            }
        }
    }
}