package parser.yearTrend;

import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.lang.SecurityException;
import java.util.Formatter;
import java.util.FormatterClosedException;
import java.util.Map;

public class resultWriter {
    private static Formatter output; // outputs text to a file
    private String fileName; // target file name

    private final Integer LIMIT_CNT = 5;

    public resultWriter(String fileName) {
        this.fileName = fileName;
        clearFile();
    }

    public void clearFile() {
        try {
            FileWriter fw = new FileWriter(fileName);
            fw.write("");
            fw.flush();
            fw.close();
        } catch (IOException e) {

        }
    }

    public void addYear(int year, Map<String, Integer> keywords) {
        openFile();
        output.format("Year: %d%n", year);
        for (Map.Entry<String, Integer> keyword : keywords.entrySet()) {
            if (keyword.getValue() >= LIMIT_CNT) {
                addRecord(keyword.getKey(), keyword.getValue());
            }
        }
        output.format("%n");
        closeFile();
    }

    public void openFile() {
        try {
            FileWriter fw = new FileWriter(fileName, true);
            output = new Formatter(fw);
        } catch (SecurityException securityException) {
            System.err.println("Write permission denied. Terminating.");
            System.exit(1); // terminate the program
        } catch (FileNotFoundException fileNotFoundException) {
            System.err.println("Error opening file. Terminating.");
            System.exit(1); // terminate the program
        } catch (IOException e) {
            System.err.println("I/O error. Terminating.");
            System.exit(1); // terminate the program
        }
    }

    // add records to file
    public void addRecord(String keyword, int count) {
        try {
            // output new record to file; assumes valid input
            output.format("%s(%d)%n", keyword, count);
        } catch (FormatterClosedException formatterClosedException) {
            System.err.println("Error writing to file. Terminating.");
        }
    }

    // close file
    public static void closeFile() {
        if (output != null)
            output.close();
    }
}
