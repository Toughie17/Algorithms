import java.util.Scanner;
public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int row = sc.nextInt();
        int col = sc.nextInt();

        int[] aCol = new int[row*col];
        int[] bCol = new int[row*col];

        for(int i = 0; i < row*col; i++) {
            aCol[i] = sc.nextInt();
        }

        for(int i = 0; i < row*col; i++) {
            bCol[i] = sc.nextInt();
        }

        for (int i =0; i< row*col; i+=col) {
            for (int j =0; j < col; j++) {
                System.out.printf("%d ", aCol[i +j] + bCol[i +j]);
            }
            System.out.println();
        }
        sc.close();
    }
}