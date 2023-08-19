import java.math.BigInteger;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.HashMap;

public class Decoder {
  private static int[] values = new int[] {
      252, 136, 204, 147, 160, 75, 221, 13, 53, 171,
      113, 140, 103, 120, 95, 192, 145, 181, 155, 75,
      162, 220, 132, 209, 239, 8, 49, 22, 61, 207,
      24, 135, 5, 148, 97, 161, 0, 179, 155, 28,
      12, 142, 194, 169, 230, 138, 138, 176, 194, 104,
      184, 104, 151, 222, 151, 89, 184, 228, 146, 62,
      102, 84, 112, 25, 165, 190, 148, 24, 221, 57,
      149, 235, 128, 153, 25, 223, 76, 180, 167, 188,
      109, 248, 95, 71, 241, 32, 64, 207, 213, 207,
      130, 227, 26, 110, 178, 200, 126, 240, 9, 8,
      78, 193, 227, 18, 121, 108, 135, 112, 234, 64,
      220, 246, 11, 195, 192, 239, 98, 216, 79, 36,
      104, 19, 59, 109, 253, 135, 151, 29, 161, 117,
      61, 9, 249, 119, 191, 185, 121, 245, 152, 186,
      142, 200, 89, 135, 68, 5, 152, 41, 206, 153,
      145, 196, 79, 52, 193, 1, 131, 235, 156, 140,
      124, 251, 155, 68, 225, 206, 214, 1, 43, 92,
      12, 173, 69, 227, 24, 13, 168, 213, 61, 71,
      149, 84, 239, 45, 9, 154, 201, 220, 237, 225,
      223, 176, 66, 68, 252, 210, 23, 66, 181, 188,
      190, 78, 114, 55, 226, 184, 69, 245, 96, 195,
      239, 90, 251, 162, 152, 78, 225, 104, 232, 39,
      18, 148, 106, 24, 23, 12, 59, 54, 41, 123,
      6, 253, 172, 96, 83, 76, 121, 128, 174, 67,
      185, 161, 131, 243, 70, 6, 243, 99, 136, 137,
      193, 231, 14, 98, 176 };

  static HashMap<Integer, Long> map = new HashMap<>();

  static long f(int paramInt) {
    if (map.containsKey(Integer.valueOf(paramInt)))
      return ((Long) map.get(Integer.valueOf(paramInt))).longValue();
    if (paramInt <= 0)
      return 1L;
    long l1 = f(paramInt - 3) * paramInt;
    long l2 = f(paramInt - 1) * f(paramInt - 2);
    long l3 = l1 + l2;
    map.put(Integer.valueOf(paramInt), Long.valueOf(l3));
    return l3;
  }

  public static void main(String[] args) {
    String key = "========================================";
    System.out.println("key awal: " + key);
    StringBuilder builder = new StringBuilder(key);
    System.out.println("Isi StringBuilder: " + builder.toString());

    // hint 6
    builder.replace(8, 17, first_decoder());
    System.out.println("current key: " + builder.toString());

    // hint 5
    builder.replace(0, 8, reverse_e(new BigInteger("6877964425780933488")));
    System.out.println("current key: " + builder.toString());

    // hint 8
    builder.replace(17, 18, "_");
    System.out.println("current key: " + builder.toString());

    // hint 9
    String segment_4 = reverse_e(new BigInteger("5928254888035102819"));
    builder.replace(18, 18 + segment_4.length(), segment_4);
    System.out.println("current key: " + builder.toString());

    // hint 11
    String segment_concated = x(reverse_e(new BigInteger("2524959283562443818")));

    // hint 10
    String segment_5 = segment_concated.substring(0, 3);
    String segment_6 = segment_concated.substring(3, segment_concated.length());
    // insert segment 5
    builder.replace(26, 26 + segment_5.length() + 1, "_" + segment_5);
    System.out.println("Segmen 5 " + segment_5);
    System.out.println("current key: " + builder.toString());
    // insert segment 6
    builder.replace(30, 30 + segment_6.length() + 2, "_" + segment_6 + "_");
    System.out.println("Segmen 6 " + segment_6);
    System.out.println("current key: " + builder.toString());

    // hint 3
    int sum_even_current = 0;
    String current_key = builder.toString();
    for (int j = 0; j < current_key.length(); j += 2) {
      if (current_key.charAt(j) == '=') {
        continue;
      }
      sum_even_current += current_key.charAt(j);
    }

    char last_even_char = (char) (1887 - sum_even_current);
    System.out.println("last even char: " + last_even_char);
    builder.replace(38, 39, String.valueOf(last_even_char));
    System.out.println("key: " + builder.toString());

    // hint 4
    int sum_odd_current = 0;
    current_key = builder.toString();
    for (byte b1 = 1; b1 < current_key.length(); b1 += 2) {
      if (current_key.charAt(b1) == '=') {
        continue;
      }
      sum_odd_current += current_key.charAt(b1);
    }
    int remaining_odd_sum = 1636 - sum_odd_current;
    System.out.println("remaining odd sum: " + remaining_odd_sum);
    //hint 2
    // bruteforce sampai ketemu yang hash nya sama
    String POSSIBLE_CHAR = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";// _ gak
    for (char a : POSSIBLE_CHAR.toCharArray()) {
      for (char b : POSSIBLE_CHAR.toCharArray()) {
        builder.replace(37, 38, String.valueOf(a));
        builder.replace(39, 40, String.valueOf(b));
        String hash_value = "";
        try {
          hash_value = hash(builder.toString());
        } catch (NoSuchAlgorithmException e) {
          System.err.println(e);
        }
        System.out.println("Trying for payload " + a + "r" + b + " ,get hash: " +
            hash_value);

        if (hash_value.equals("d36b43b497b11bb3650f8f8977bd3ecdade2e8ad022a20750b6c3cd34eae9886")) {
          System.out.println("COMBINATION FOUND!");
          System.out.println("Final key: " + builder.toString());
          return;
        }
      }
    }
    System.out.println("COMBINATION NOT FOUND!");
    return;
  }

  static String hash(String paramString) throws NoSuchAlgorithmException {
    MessageDigest messageDigest = MessageDigest.getInstance("SHA-256");
    byte[] arrayOfByte = messageDigest.digest(paramString.getBytes(StandardCharsets.UTF_8));
    StringBuilder stringBuilder = new StringBuilder(2 * arrayOfByte.length);
    for (byte b = 0; b < arrayOfByte.length; b++) {
      String str = Integer.toHexString(0xFF & arrayOfByte[b]);
      if (str.length() == 1)
        stringBuilder.append('0');
      stringBuilder.append(str);
    }
    return stringBuilder.toString();
  }

  static String first_decoder() {
    StringBuilder result = new StringBuilder("");
    for (byte b2 = 0; b2 < 9; b2++) {
      char character = (char) (0xff ^ values[(int) (f(b2) % 101L)]);
      result.append(character);
    }
    return result.toString();
  }

  static BigInteger e(String paramString) {
    BigInteger bigInteger = BigInteger.valueOf(0L);
    for (byte b = 0; b < paramString.length(); b++) {
      BigInteger bigInteger1 = BigInteger.valueOf(paramString.charAt(b)).shiftLeft(8 * b);
      bigInteger = bigInteger.or(bigInteger1);
    }
    return bigInteger;
  }

  static String reverse_e(BigInteger result) {
    StringBuilder original = new StringBuilder();

    for (byte chara : result.toByteArray()) {
      original.append((char) chara);
    }

    return original.reverse().toString();// java big endian nyimpennya
  }

  static String x(String paramString) {
    StringBuilder stringBuilder = new StringBuilder();
    for (char c : paramString.toCharArray())
      stringBuilder.append((char) (c ^ 0x44));
    return stringBuilder.toString();
  }
}