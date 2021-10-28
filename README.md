package com.company;

import java.util.Scanner;

public class Calculator {
    public Calculator() {
    }

    public int EvaluateExpression(int firstNumber, int secondNumber, char operation) throws NumberFormatException, ArithmeticException {
        switch (operation) {
            case '+':
                return firstNumber + secondNumber;
            case '-':
                return firstNumber - secondNumber;
            case '*':
                return firstNumber * secondNumber;
            case '/':
                return firstNumber / secondNumber;
            default:
                throw new NumberFormatException();
        }
    }

    public void ShowEvaluation() {
        Scanner scan = new Scanner(System.in);

        int firstNumber =  scan.nextInt();
        System.out.print("Enter first number: ");

        char operation = scan.next().charAt(0);
        System.out.print("Enter operation: ");

        int secondNumber = scan.nextInt();
        System.out.print("Enter second number: ");

        try {
            System.out.println("Result: " + EvaluateExpression(firstNumber, secondNumber, operation));
        }
        catch (NumberFormatException nfe) {
            System.out.println("UNKNOWN OPERATION");
        }
        catch (ArithmeticException ae) {
            System.out.println("DIVISION BY ZERO");
        }

        scan.close();
    }
}
