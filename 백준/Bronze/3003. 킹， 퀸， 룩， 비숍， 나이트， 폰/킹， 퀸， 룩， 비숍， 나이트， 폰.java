import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    //정상 체스
    int[] chess = {1, 1, 2, 2, 2, 8};
    int[] answer = new int[6];
    for(int i =0; i<6;i++) {
        int num = sc.nextInt();
        answer[i] = chess[i] - num;
    }
    //찾은 체스값 입력;
   for (int num : answer) {
       System.out.printf("%d ", num);
   }
    }
}