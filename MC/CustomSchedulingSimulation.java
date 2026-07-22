public class CustomSchedulingSimulation {

    public static void main(String[] args) {

        int numHosts = 5;
        int numVMs = 10;
        int numCloudlets = 20;
        double simulationTime = 1000.0;

        System.out.println("CUSTOM SCHEDULING SIMULATION");

        System.out.println("\nTotal Simulation Time: " + simulationTime + " seconds");

        System.out.println("\nDatacenter Information:");
        System.out.println("Number of Hosts: " + numHosts);
        System.out.println("Number of Virtual Machines: " + numVMs);
        System.out.println("Number of Cloudlets: " + numCloudlets);

        System.out.println("\nScheduling Algorithm: CustomScheduler");

        System.out.println("\nScheduled Cloudlets:");

        for (int i = 1; i <= numCloudlets; i++) {
            int vmId = ((i - 1) % numVMs) + 1;
            System.out.println("Cloudlet " + i + " : VM ID-" + vmId);
        }
    }
}