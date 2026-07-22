import java.util.ArrayList;
import java.util.List;

class LogEntry {

    private String timestamp;
    private String sourceIP;
    private String destinationIP;
    private String message;

    public LogEntry(String timestamp, String sourceIP,
                    String destinationIP, String message) {
        this.timestamp = timestamp;
        this.sourceIP = sourceIP;
        this.destinationIP = destinationIP;
        this.message = message;
    }

    public String getMessage() {
        return message;
    }

    @Override
    public String toString() {
        return timestamp +
                " | " +
                sourceIP +
                " -> " +
                destinationIP +
                " | " +
                message;
    }
}

public class LogForensicsSimulation {

    public static void main(String[] args) {

        List<LogEntry> logData = generateLogData();

        List<LogEntry> suspiciousActivities =
                detectSuspiciousActivities(logData);

        List<LogEntry> anomalies =
                detectAnomalies(logData);

        printSuspiciousActivities(suspiciousActivities);

        printAnomalies(anomalies);
    }

    private static List<LogEntry> generateLogData() {

        List<LogEntry> logs = new ArrayList<>();

        logs.add(new LogEntry(
                "2026-06-24 10:00:00",
                "192.168.1.10",
                "10.0.0.1",
                "User Login"));

        logs.add(new LogEntry(
                "2026-06-24 10:05:00",
                "192.168.1.20",
                "10.0.0.2",
                "Failed Login"));

        logs.add(new LogEntry(
                "2026-06-24 10:10:00",
                "192.168.1.30",
                "10.0.0.3",
                "Port Scan Detected"));

        logs.add(new LogEntry(
                "2026-06-24 10:15:00",
                "192.168.1.40",
                "10.0.0.4",
                "Data Exfiltration Attempt"));

        logs.add(new LogEntry(
                "2026-06-24 10:20:00",
                "192.168.1.50",
                "10.0.0.5",
                "Normal Traffic"));

        return logs;
    }

    private static List<LogEntry> detectSuspiciousActivities(
            List<LogEntry> logData) {

        List<LogEntry> suspicious = new ArrayList<>();

        for (LogEntry log : logData) {

            String msg = log.getMessage().toLowerCase();

            if (msg.contains("failed")
                    || msg.contains("scan")
                    || msg.contains("exfiltration")) {

                suspicious.add(log);
            }
        }

        return suspicious;
    }

    private static List<LogEntry> detectAnomalies(
            List<LogEntry> logData) {

        List<LogEntry> anomalies = new ArrayList<>();

        for (LogEntry log : logData) {

            if (log.getMessage()
                    .toLowerCase()
                    .contains("exfiltration")) {

                anomalies.add(log);
            }
        }

        return anomalies;
    }

    private static void printSuspiciousActivities(
            List<LogEntry> suspiciousActivities) {

        System.out.println("==================================");
        System.out.println("SUSPICIOUS ACTIVITIES DETECTED");
        System.out.println("==================================");

        for (LogEntry log : suspiciousActivities) {
            System.out.println(log);
        }
    }

    private static void printAnomalies(
            List<LogEntry> anomalies) {

        System.out.println("\n==================================");
        System.out.println("ANOMALIES DETECTED");
        System.out.println("==================================");

        for (LogEntry log : anomalies) {
            System.out.println(log);
        }
    }
}