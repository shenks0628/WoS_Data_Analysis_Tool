package parser.yearTrend;

import java.io.IOException;
import java.lang.IllegalStateException;
import java.nio.file.Paths;
import java.util.Map;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.NoSuchElementException;
import java.util.Scanner;

public class Reader {
    private Scanner input;
    private String fileName; // target file name
    private Map<Integer, Map<String, Integer>> list;

    public Reader(String fileName) {
        list = new HashMap<>();
        this.fileName = fileName;
    }

    public void setFileName(String fileName) {
        this.fileName = fileName;
    }

    public Map<Integer, Map<String, Integer>> getList() {
        return list;
    }

    public void readPY() {
        openFile();
        try {
            if (input.hasNextLine()) {
                String inputFirst = input.nextLine();
                Map<String, Integer> keywords = new HashMap<>();
                while (input.hasNextLine()) // while there is more to read
                {
                    String type = inputFirst.substring(0, 2);
                    String text = inputFirst.substring(3);
                    if (type.startsWith("PY")) {
                        try {
                            int year = Integer.parseInt(text);
                            if (list.containsKey(year)) {
                                Map<String, Integer> old = list.get(year);
                                for (Map.Entry<String, Integer> keyword : keywords.entrySet()) {
                                    if (old.containsKey(keyword.getKey())) {
                                        old.replace(keyword.getKey(), old.get(keyword.getKey()) + keyword.getValue());
                                    } else {
                                        old.put(keyword.getKey(), keyword.getValue());
                                    }
                                }
                                list.replace(year, old);
                            } else {
                                list.put(year, keywords);
                            }
                            keywords = new HashMap<>();
                        } catch (NumberFormatException e) {
                            System.out.println(e);
                        }
                    } else if (type.startsWith("DE")) {
                        for (String keyword : text.split(";")) {
                            keyword = keyword.toLowerCase().trim();
                            if (keywords.containsKey(keyword)) {
                                keywords.replace(keyword, keywords.get(keyword) + 1);
                            } else {
                                keywords.put(keyword, 1);
                            }
                        }
                    }

                    while (input.hasNextLine()) {
                        text = input.nextLine();
                        if (text.startsWith("   ")) {
                            // System.out.println(text);
                        } else {
                            inputFirst = text;
                            if (inputFirst.length() >= 2 && !inputFirst.startsWith("ER"))
                                break;
                        }
                    }
                }
            }
        } catch (NoSuchElementException elementException) {
            System.err.println("File improperly formed. Terminating.");
        } catch (IllegalStateException stateException) {
            System.err.println("Error reading from file. Terminating.");
        }
        closeFile();
    }

    public void openFile() {
        try {
            input = new Scanner(Paths.get(fileName));
        } catch (IOException ioException) {
            System.err.println("Error opening file. Terminating.");
            System.exit(1);
        }
    }

    // close file and terminate application
    public void closeFile() {
        if (input != null)
            input.close();
    }
}
