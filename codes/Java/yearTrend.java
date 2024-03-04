/*
進到Java資料夾後
編譯指令
javac -encoding utf-8 -d . *.java
*/
package parser.yearTrend;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Map;

public class yearTrend {
    public static void main(String[] args) {
        Reader reader = new Reader("../autonomous_vehicle_data_records/1.txt");
        Map<Integer, Map<String, Integer>> PY = reader.readPY();
        for (Map.Entry<Integer, Map<String, Integer>> entry : PY.entrySet()) {
            System.out.println("Year = " + entry.getKey());
            for (Map.Entry<String, Integer> year : entry.getValue().entrySet()) {
                System.out.println(year.getKey() + "(" + year.getValue() + ")");
            }
            System.out.println();
        }
    }
}