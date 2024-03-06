package com.bayyy.enum0;

public class TestGender {

    public static void main(String[] args) {
        Gender gender = Gender.Male;
        System.out.println(gender);
        Season season = Season.SPRING;
        System.out.println(season.toString());
        switch (season) {
            case SPRING -> System.out.println("春天");
            case SUMMER -> System.out.println("夏天");
            case AUTUMN -> System.out.println("秋天");
            case WINTER -> System.out.println("冬天");
        }
    }
}
