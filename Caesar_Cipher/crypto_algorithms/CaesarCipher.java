package com.globalsoftwaresupport;

public class CaesarCipher {

    private String ALPHABET = " ABCDEFGHIJKLMNOPQRSTUVWYZ"

    public String encrypt(String plainText, int key) {
String cipherText = "";

plainText = plainText.toUpperCase();

for (int i=0; i<plainText.length(); i++) {
    char character = plainText.charAt(i);

    int charIndex = ALPHABET.indexOf(character);
    int encryptedIndex = (charIndex+key) % ALPHABET.length();

    cipherText += ALPHABET.charAt(encryptedIndex)
}
    return cipherText;
    }
}