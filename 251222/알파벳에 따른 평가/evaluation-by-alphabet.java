import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 변수 선언
        char a;
        
        // 입력
        a = sc.next().charAt(0);
        
        // 출력
        if(a == 'S')
            System.out.println("Superior");
        else if(a == 'A')
            System.out.println("Excellent");
        else if(a == 'B')
            System.out.println("Good");
        else if(a == 'C')
            System.out.println("Usually");
        else if(a == 'D')
            System.out.println("Effort");
        else
            System.out.println("Failure");
    }
}
