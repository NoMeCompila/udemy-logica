import java.util.HashMap;
import java.util.Map;

public class ej15{
    public static void main(String[] args) {
        String word = "invisible";
        Map<String, Integer> mp = new HashMap<>();
        String[] letters = word.split("");

        //System.out.println(word.split(""));
        for (String str : letters) {
            if(mp.containsKey(str)){
                int count = mp.get(str);
                mp.put(str, count+1);
            }else{
                mp.put(str, 1);
            }
        }

        System.out.println(mp);

        Map.Entry<String, Integer> maxEntry = mp.entrySet().stream()
            .max(Map.Entry.comparingByValue())
            .orElse(null);

        System.out.println(maxEntry);
    }
}