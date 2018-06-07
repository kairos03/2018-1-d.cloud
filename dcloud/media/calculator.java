import java.util.Scanner;

class calculator{
    public static void main(String[] args) {

        Scanner scn = new Scanner(System.in);
        
        System.out.print("Input first args: ");

        float num1 = scn.nextFloat();

        System.out.print("Input second args: ");
        float num2 = scn.nextFloat();

        System.out.print("Input Operator(+,-,/,*): ");
        
        String oper = scn.next();

        float result = 0.0f;

        switch (oper) {
            case "+":
                result = num1 + num2;
                break;

            case "-":
            result = num1 - num2;
            break;

            case "/":
            result = num1 / num2;
            break;

            case "*":
            result = num1 * num2;
            break;
        
            default:
                break;
        }

        System.out.println("Result is " + result);
        scn.close();
    }
}