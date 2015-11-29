package me.timtim17.dev.pscsta.spring2015.java;

public class SayHello {
    public static void main (String[] args) {
        String[] names = {"Austin", "Myself", "I"};

        int letters = 0;
        for (String name : names) {
            letters += name.length();
        }

        System.out.print("Hello judges! Our names are ");
        for (int i = 0; i < names.length; i++) {
            if (i == names.length - 1) {
                System.out.print("and " + names[i] + ". ");
            } else {
                System.out.print(names[i] + ", ");
            }
        }

        System.out.println("There are " + letters + " letters in our names. Have a wolf strong day! Wolf Strong Pack Strong!");
    }
}
