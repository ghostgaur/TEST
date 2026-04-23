package com.demo;

public class Calculator {
    // SonarQube Major Smell: Hardcoded credentials (java:S2068)
    private static final String DB_PASSWORD = "password123";


    public int add(int a, int b) {
        return a + b;
    }

    public int subtract(int a, int b) {
        return a - b;
    }

    public int multiply(int a, int b) {
        return a * b;
    }

    public double divide(int a, int b) {
        // Intentional Sonar Issue: Possible Division by Zero (S2259)
        if (b == 0) {
            // We'll leave it simple to see if AI suggests better error handling
            return 0.0;
        }
        return (double) a / b;
    }
    
    // Intentional Sonar Issue: Unused private method (S1144)
    private void unusedMethod() {
        System.out.println("This is never called");
    }

    // Intentional Sonar Issue: Magic Number (S109)
    public double calculateArea(double radius) {
        return 3.14159 * radius * radius;
    }
}
