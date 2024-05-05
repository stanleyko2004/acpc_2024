import java.io.BufferedReader;
import java.util.HashMap;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Stickogon {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
        // int[] answers = new int[t];
        for (int i=0; i<t; i++){
			StringTokenizer st = new StringTokenizer(br.readLine());
			int n = Integer.parseInt(st.nextToken());
            st = new StringTokenizer(br.readLine());
            HashMap<String, Integer> freq = new HashMap<>();
            for (int j=0; j<n; j++) {
                String size = st.nextToken();
                // System.out.println("size" + size);
                if (freq.containsKey(size)) {
                    freq.put(size, freq.get(size) + 1);
                } else {
                    freq.put(size, 1);
                }
            }
            // System.out.println(freq.toString());
            int total = 0;
            for (int v: freq.values()) {
                total += v / 3;
            }
            // answers[i] = total;
			System.out.println(total);
		}
	}
}