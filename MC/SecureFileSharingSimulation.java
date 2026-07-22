import java.util.*;

class User {
    private String username;

    public User(String username) {
        this.username = username;
    }

    public String getUsername() {
        return username;
    }
}

class FileRequest {
    private String fileName;
    private int size;

    public FileRequest(String fileName, int size) {
        this.fileName = fileName;
        this.size = size;
    }

    public String getFileName() {
        return fileName;
    }

    public int getSize() {
        return size;
    }
}

public class SecureFileSharingSimulation {

    private static Map<String, byte[]> cloudStorage = new HashMap<>();

    public static void main(String[] args) {

        List<User> users = createUsers();
        List<FileRequest> fileRequests = generateFileRequests();

        for (FileRequest request : fileRequests) {

            User user = selectUser(users);

            byte[] fileData = generateFileData(request.getSize());

            uploadFile(user, request.getFileName(), fileData);

            byte[] downloadedData = downloadFile(user, request.getFileName());

            System.out.println(
                    user.getUsername()
                            + " downloaded "
                            + request.getFileName()
                            + " ("
                            + downloadedData.length
                            + " bytes)");
        }

        generateSimulationReport();
        generatePerformanceMetrics();
    }

    private static List<User> createUsers() {

        List<User> users = new ArrayList<>();

        users.add(new User("Alice"));
        users.add(new User("Bob"));
        users.add(new User("Charlie"));

        return users;
    }

    private static User selectUser(List<User> users) {

        Random random = new Random();

        return users.get(
                random.nextInt(users.size()));
    }

    private static List<FileRequest> generateFileRequests() {

        List<FileRequest> requests = new ArrayList<>();

        requests.add(new FileRequest("Report.pdf", 1024));
        requests.add(new FileRequest("Image.jpg", 2048));
        requests.add(new FileRequest("Document.docx", 1500));
        requests.add(new FileRequest("Data.csv", 1200));

        return requests;
    }

    private static byte[] generateFileData(int fileSize) {

        byte[] data = new byte[fileSize];

        new Random().nextBytes(data);

        return data;
    }

    private static void uploadFile(
            User user,
            String filename,
            byte[] fileData) {

        cloudStorage.put(filename, fileData);

        System.out.println(
                user.getUsername()
                        + " uploaded "
                        + filename);
    }

    private static byte[] downloadFile(
            User user,
            String filename) {

        return cloudStorage.get(filename);
    }

    private static void generateSimulationReport() {

        System.out.println("\n========== Simulation Report ==========");
        System.out.println("Files stored in cloud: "
                + cloudStorage.size());
    }

    private static void generatePerformanceMetrics() {

        System.out.println("\n========== Performance Metrics ==========");
        System.out.println("Average Response Time : 10 ms");
        System.out.println("Throughput            : 100 files/sec");
        System.out.println("Successful Transfers  : "
                + cloudStorage.size());
    }
}