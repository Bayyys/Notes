package com.bayyy.pojo;

public class Hello {
    private String text;

    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    @Override
    public String toString() {
        return "Hello{" +
                "text='" + text + '\'' +
                '}';
    }
}
