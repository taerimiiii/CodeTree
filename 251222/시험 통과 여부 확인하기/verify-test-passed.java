import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 변수 선언
        int n;
        
        // 입력
        n = sc.nextInt();
        
        // 출력
        if(n >= 80)
            System.out.println("pass");
        else
            System.out.println((80 - n) + " more score");
    }
}
