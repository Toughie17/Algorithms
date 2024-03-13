import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        for(int i =0; i < 3; i++) {
            int h = sc.nextInt();
            int m = sc.nextInt();
            int s = sc.nextInt();

            int ho =sc.nextInt();
            int mo = sc.nextInt();
            int so =sc.nextInt();

            int enterTotalSec = s + m*60 + h*3600;
            int outTotalSec = so + mo*60 + ho*3600;
            int totalWorkSeconds = outTotalSec - enterTotalSec;

            int workingHour = totalWorkSeconds / 3600;
            int workingMinutes = (totalWorkSeconds % 3600) / 60;
            int workingSeconds = totalWorkSeconds % 60;

            System.out.printf("%d %d %d\n",workingHour,workingMinutes,workingSeconds);
        }
    }
}