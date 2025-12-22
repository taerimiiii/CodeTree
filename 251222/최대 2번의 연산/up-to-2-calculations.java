import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 변수 선언
        int a;
        
        // 입력
        a = sc.nextInt();

        if(a % 2 == 0)
            a /= 2;
        
        if(a % 2 == 1)
            a = (a + 1) / 2;

        System.out.println(a);
    }
}
