/*
進到Java資料夾後
編譯指令
javac -encoding utf-8 -d . *.java
*/
package parser.yearTrend;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.Writer;
import java.util.Map;

public class yearTrend {
    public static void main(String[] args) {
        Reader reader = new Reader("../autonomous_vehicle_data_records/1.txt");
        resultWriter writer = new resultWriter("result.txt");
        for (int i = 1; i <= 27; i++) {
            reader.setFileName("../autonomous_vehicle_data_records/" + Integer.toString(i) + ".txt");
            System.out.println("../autonomous_vehicle_data_records/" + Integer.toString(i) + ".txt");
            reader.readPY();
        }
        Map<Integer, Map<String, Integer>> PY = reader.getList();
        for (Map.Entry<Integer, Map<String, Integer>> entry : PY.entrySet()) {
            writer.addYear(entry.getKey(), entry.getValue());
        }
    }
}