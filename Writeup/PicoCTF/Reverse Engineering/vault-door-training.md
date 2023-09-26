## Challenge Name: vault-door-training
>Category: Reverse Engineering

>Points: 50

>Solves: 44,996

### Challenge Description: 

Your mission is to enter Dr. Evil's laboratory and retrieve the blueprints for his Doomsday Project. The laboratory is protected by a series of locked vault doors. Each door is controlled by a computer and requires a password to open. Unfortunately, our undercover agents have not been able to obtain the secret passwords for the vault doors, but one of our junior agents obtained the source code for each vault's computer! You will need to read the source code for each level to figure out what the password is for that vault door. As a warmup, we have created a replica vault in our training facility. The source code for the training vault is here: [VaultDoorTraining.java](https://jupiter.challenges.picoctf.org/static/03c960ddcc761e6f7d1722d8e6212db3/VaultDoorTraining.java)


Artifact Files:
* [VaultDoorTraining.java](https://jupiter.challenges.picoctf.org/static/03c960ddcc761e6f7d1722d8e6212db3/VaultDoorTraining.java)

### Approach
**1. Analisis File**   
Coba kita unduh _file_-nya dan kita lihat _source code_-nya:
```
import java.util.*;

class VaultDoorTraining {
    public static void main(String args[]) {
        VaultDoorTraining vaultDoor = new VaultDoorTraining();
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter vault password: ");
        String userInput = scanner.next();
        String input = userInput.substring("picoCTF{".length(), userInput.length() - 1);
        if (vaultDoor.checkPassword(input)) {
            System.out.println("Access granted.");
        } else {
            System.out.println("Access denied!");
        }
    }

    // The password is below. Is it safe to put the password in the source code?
    // What if somebody stole our source code? Then they would know what our
    // password is. Hmm... I will think of some ways to improve the security
    // on the other doors.
    //
    // -Minion #9567
    public boolean checkPassword(String password) {
        return password.equals("w4rm1ng_Up_w1tH_jAv4_3808d338b46");
    }
}
```
Jadi program ini nerima masukan, ngevalidasi, kalau bener ada tulisan "Access granted.", kalau salah dapat tulisan "Access denied!"

**2. Mendapatkan Flag**   
Kalau kita perhatikan di fungsi ```checkPassword()``` ada komentar dan _string_ yang intinya:
LAH INIMAH TINGGAL CONCAT ```picoCTF``` SAMA _STRING_ DI FUNGSI ```checkPassword()``` AJA!

Bukti lainnya ada di _line_ ini:
```
String input = userInput.substring("picoCTF{".length(), userInput.length() - 1);
```
Hal ini berarti yang dijadikan masukan ke fungsi ```checkPassword()``` ialah _string_ yang berada diantara karakter ```{``` dan karakter terakhir _string input_ yang mengindikasikan isi dari _flag_-nya sehingga bisa ditarik kesimpulan _string_ yang menjadi pembanding di fungsi ```checkPassword()``` adalah _flag_-nya.

Yaudah dapat _flag_-nya:
```
picoCTF{w4rm1ng_Up_w1tH_jAv4_3808d338b46}
```

**[BONUS] Eksekusi Program**

Karena ada istilah "No Bukti Hoax", yasudah kita compile dengan _command_ berikut:
```
javac VaultDoorTraining.java
```
Lalu kita jalankan dengan _command_ berikut:
```
java VaultDoorTraining
```
Dapat _prompt_ seperti berikut:
```
Enter vault password: 
```
Tinggal masukkan _flag_ dan didapat hasil berikut:
```
Enter vault password: picoCTF{w4rm1ng_Up_w1tH_jAv4_3808d338b46}
Access granted.
```

### Reflections

Jujur rada gampang tinggal buka source code. Neverthenless, _warming-up_ yang menarik bagi pemula.

---
[Back to home](../Readme.md)
