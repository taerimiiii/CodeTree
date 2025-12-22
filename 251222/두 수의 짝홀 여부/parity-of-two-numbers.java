import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 변수 선언
        int a, b;
        
        // 입력
        a = sc.nextInt();
        b = sc.nextInt();

        // 출력
        if(a % 2 == 0)
            System.out.println("even");
        else
            System.out.println("odd");
        
        if(b % 2 == 0)
            System.out.println("even");
        else
            System.out.println("odd");
    }
}
