import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    //석가모니가 열반한 해를 기준으로 연도를 센다고? (불기)
    //불기를 서기로 바꿔주는 프로그램
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine(); //String으로 받기 때문에 파싱 해줘야함
        int a = Integer.parseInt(input);
        System.out.printf("%d",(a - 543));
    }
}