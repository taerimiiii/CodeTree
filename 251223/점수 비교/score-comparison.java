import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 변수 선언
        int aMath, aEng;
        int bMath, bEng;
        
        // 입력
        aMath = sc.nextInt();
        aEng = sc.nextInt();
        bMath = sc.nextInt();
        bEng = sc.nextInt();
        
        if(aMath > bMath && aEng > bEng)
            System.out.println("1");
        else
            System.out.println("0");
    }
}
