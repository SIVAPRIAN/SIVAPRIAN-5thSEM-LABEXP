import java.util.ArrayList;
import java.util.List;

/**
 * Experiment 3: Simulate Log Forensics Using CloudSim & Custom Log Analysis.
 * This class implements log generation, suspicious activity analysis,
 * and system anomaly detection.
 */
public class LogForensicsSimulation {

    // Representation of a Log Entry for cloud resource/forensics audits
    public static class LogEntry {
        private String timestamp;
        private String sourceIp;
        private String destIp;
        private String message;
        private double cpuUtilization; // Percentage (e.g., 95.0)
        private long fileTransferSize; // Bytes (e.g., 5000000000)
        private double memoryUtilization; // Percentage (e.g., 98.0)

        public LogEntry(String timestamp, String sourceIp, String destIp, String message, 
                        double cpuUtilization, long fileTransferSize, double memoryUtilization) {
            this.timestamp = timestamp;
            this.sourceIp = sourceIp;
            this.destIp = destIp;
            this.message = message;
            this.cpuUtilization = cpuUtilization;
            this.fileTransferSize = fileTransferSize;
            this.memoryUtilization = memoryUtilization;
        }

        public String getTimestamp() { return timestamp; }
        public String getSourceIp() { return sourceIp; }
        public String getDestIp() { return destIp; }
        public String getMessage() { return message; }
        public double getCpuUtilization() { return cpuUtilization; }
        public long getFileTransferSize() { return fileTransferSize; }
        public double getMemoryUtilization() { return memoryUtilization; }

        @Override
        public String toString() {
            return "Timestamp: " + timestamp + ", Source IP: " + sourceIp + 
                   ", Destination IP: " + destIp + ", Log Message: " + message;
        }
    }

    public static void main(String[] args) {
        System.out.println("Initializing Cloud Log Forensics Engine...");

        // Generate Simulated Cloud Log Data
        List<LogEntry> logData = generateLogData();

        // Perform Forensic Analysis
        List<LogEntry> suspiciousActivities = detectSuspiciousActivities(logData);
        List<LogEntry> anomalies = detectAnomalies(logData);

        // Print Results
        printSuspiciousActivities(suspiciousActivities);
        printAnomalies(anomalies);
    }

    private static List<LogEntry> generateLogData() {
        List<LogEntry> logs = new ArrayList<>();

        // Normal log entries
        logs.add(new LogEntry("2023-06-01 08:15:22", "192.168.1.50", "203.0.113.5", "User login successful.", 12.5, 1024, 45.0));
        logs.add(new LogEntry("2023-06-01 09:30:00", "192.168.1.60", "203.0.113.8", "VM scheduled task started.", 5.0, 512, 10.0));

        // Suspicious Activities
        logs.add(new LogEntry("2023-06-01 10:23:45", "192.168.1.100", "203.0.113.10", "Unauthorized access attempt.", 10.0, 0, 15.0));
        logs.add(new LogEntry("2023-06-02 14:55:12", "192.168.1.150", "203.0.113.20", "High volume of outbound traffic to suspicious IP address.", 15.0, 50000000000L, 20.0)); // 50GB
        logs.add(new LogEntry("2023-06-03 09:10:27", "192.168.1.200", "203.0.113.30", "Unusual login activity from multiple IP addresses.", 8.0, 2048, 12.0));

        // Anomalies (Metrics exceeding safety thresholds)
        logs.add(new LogEntry("2023-06-01 12:05:30", "192.168.1.75", "203.0.113.10", "Abnormal CPU utilization exceeding threshold.", 98.5, 500, 30.0)); // CPU spike
        logs.add(new LogEntry("2023-06-02 16:30:15", "192.168.1.110", "203.0.113.20", "Unusually large file transfer size.", 45.0, 100000000000L, 65.0)); // 100GB
        logs.add(new LogEntry("2023-06-03 11:40:21", "192.168.1.180", "203.0.113.30", "Unusual memory consumption pattern.", 22.0, 1024, 99.1)); // RAM spike

        return logs;
    }

    private static List<LogEntry> detectSuspiciousActivities(List<LogEntry> logData) {
        List<LogEntry> results = new ArrayList<>();
        for (LogEntry log : logData) {
            String msg = log.getMessage().toLowerCase();
            // Rules for suspicious activities
            if (msg.contains("unauthorized") || 
                msg.contains("high volume of outbound") || 
                msg.contains("login activity from multiple")) {
                results.add(log);
            }
        }
        return results;
    }

    private static List<LogEntry> detectAnomalies(List<LogEntry> logData) {
        List<LogEntry> results = new ArrayList<>();
        // Thresholds
        double cpuThreshold = 90.0; // %
        double memoryThreshold = 95.0; // %
        long sizeThreshold = 10L * 1024 * 1024 * 1024; // 10 GB

        for (LogEntry log : logData) {
            if (log.getCpuUtilization() > cpuThreshold || 
                log.getFileTransferSize() > sizeThreshold || 
                log.getMemoryUtilization() > memoryThreshold) {
                results.add(log);
            }
        }
        return results;
    }

    private static void printSuspiciousActivities(List<LogEntry> suspiciousActivities) {
        System.out.println("\nDetected Suspicious Activities:");
        int counter = 1;
        for (LogEntry log : suspiciousActivities) {
            System.out.println(counter + ". " + log);
            counter++;
        }
    }

    private static void printAnomalies(List<LogEntry> anomalies) {
        System.out.println("\nDetected Anomalies:");
        int counter = 1;
        for (LogEntry log : anomalies) {
            System.out.println(counter + ". " + log);
            counter++;
        }
    }
}

/*
EXPECTED OUTPUT:
Detected Suspicious Activities:
1. Timestamp: 2023-06-01 10:23:45, Source IP: 192.168.1.100, Destination IP: 203.0.113.10, Log Message: Unauthorized access attempt.
2. Timestamp: 2023-06-02 14:55:12, Source IP: 192.168.1.150, Destination IP: 203.0.113.20, Log Message: High volume of outbound traffic to suspicious IP address.
3. Timestamp: 2023-06-03 09:10:27, Source IP: 192.168.1.200, Destination IP: 203.0.113.30, Log Message: Unusual login activity from multiple IP addresses.

Detected Anomalies:
1. Timestamp: 2023-06-01 12:05:30, Source IP: 192.168.1.75, Destination IP: 203.0.113.10, Log Message: Abnormal CPU utilization exceeding threshold.
2. Timestamp: 2023-06-02 16:30:15, Source IP: 192.168.1.110, Destination IP: 203.0.113.20, Log Message: Unusually large file transfer size.
3. Timestamp: 2023-06-03 11:40:21, Source IP: 192.168.1.180, Destination IP: 203.0.113.30, Log Message: Unusual memory consumption pattern.
*/
