import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Vada_x {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
        HashMap<String, Integer> groups = new HashMap();
        StringTokenizer st;
		for (int i=0; i<n; i++){
			st = new StringTokenizer(br.readLine());
            String group = st.nextToken();
            int songs = Integer.parseInt(st.nextToken());
            groups.put(group, songs);

		}
        int t = Integer.parseInt(br.readLine()); 
        for (int i=0; i<t; i++){
            String group = br.readLine();
            if (groups.containsKey(group)) {
                groups.put(group, groups.get(group) - 1);
            }
        }
        boolean flag = false;
        for (String group: groups.keySet()){
            if (groups.get(group) > 0) {
                flag = true;
                System.out.println(group);
                break;
            }
        }
        if (!flag) {
            System.out.println("NO KPOP FOR VADER");
        }
	}
}