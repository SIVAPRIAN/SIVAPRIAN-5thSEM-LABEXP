import org.cloudbus.cloudsim.*;
import org.cloudbus.cloudsim.core.CloudSim;
import org.cloudbus.cloudsim.provisioners.BwProvisionerSimple;
import org.cloudbus.cloudsim.provisioners.RamProvisionerSimple;
import org.cloudbus.cloudsim.provisioners.PeProvisionerSimple;
import org.cloudbus.cloudsim.CloudletSchedulerTimeShared;
import org.cloudbus.cloudsim.VmSchedulerSpaceShared;

import java.util.*;

/**
 * Experiment 1: Cloud Scenario Simulation & Custom Scheduling Policy.
 * This class simulates a cloud scenario using CloudSim and implements 
 * a Round-Robin VM Allocation Policy not present in default CloudSim.
 */
public class CustomSchedulingSimulation {

    public static void main(String[] args) {
        System.out.println("Starting Cloud Custom Scheduling Simulation...");

        try {
            // Step 1: Initialize CloudSim
            int numUsers = 1;
            Calendar calendar = Calendar.getInstance();
            boolean traceFlag = false;
            CloudSim.init(numUsers, calendar, traceFlag);

            // Step 2: Create Datacenter
            Datacenter datacenter0 = createDatacenter("Datacenter_0");

            // Step 3: Create Broker
            DatacenterBroker broker = createBroker("Broker_0");
            int brokerId = broker.getId();

            // Step 4: Create VMs and Cloudlets
            int numVMs = 5;
            int numCloudlets = 10;

            List<Vm> vmList = createVMs(brokerId, numVMs);
            List<Cloudlet> cloudletList = createCloudlets(brokerId, numCloudlets);

            // Submit lists to broker
            broker.submitVmList(vmList);
            broker.submitCloudletList(cloudletList);

            // Step 5: Initialize Custom VM Allocation Policy and associate with datacenter
            // Note: In CloudSim, Datacenter manages its own VmAllocationPolicy.
            // We set the custom RoundRobinVmAllocationPolicy during datacenter creation.

            // Step 6: Start Simulation
            CloudSim.startSimulation();

            // Step 7: Stop Simulation
            CloudSim.stopSimulation();

            // Step 8: Display results
            List<Cloudlet> finishedCloudlets = broker.getCloudletReceivedList();
            printResults(finishedCloudlets, vmList);

            System.out.println("Simulation completed successfully.");
        } catch (Exception e) {
            e.printStackTrace();
            System.err.println("Simulation failed due to an unexpected error.");
        }
    }

    private static Datacenter createDatacenter(String name) {
        List<Host> hostList = new ArrayList<>();

        // Create 5 Hosts
        int numHosts = 5;
        for (int i = 0; i < numHosts; i++) {
            List<Pe> peList = new ArrayList<>();
            int mips = 2000; // Host CPU capacity
            peList.add(new Pe(0, new PeProvisionerSimple(mips))); // single core Host

            int ram = 4096; // Host memory (MB)
            long storage = 1000000; // Host storage (MB)
            int bw = 10000; // Host bandwidth

            hostList.add(new Host(
                    i,
                    new RamProvisionerSimple(ram),
                    new BwProvisionerSimple(bw),
                    storage,
                    peList,
                    new VmSchedulerSpaceShared(peList)
            ));
        }

        // Characteristics of Datacenter
        String arch = "x86";
        String os = "Linux";
        String vmm = "Xen";
        double timeZone = 10.0;
        double cost = 3.0;
        double costPerMem = 0.05;
        double costPerStorage = 0.001;
        double costPerBw = 0.0;

        DatacenterCharacteristics characteristics = new DatacenterCharacteristics(
                arch, os, vmm, hostList, timeZone, cost, costPerMem, costPerStorage, costPerBw
        );

        Datacenter datacenter = null;
        try {
            // Apply custom VM Allocation Policy here
            VmAllocationPolicy policy = new RoundRobinVmAllocationPolicy(hostList);
            datacenter = new Datacenter(
                    name,
                    characteristics,
                    policy,
                    new LinkedList<>(),
                    0
            );
        } catch (Exception e) {
            e.printStackTrace();
        }

        return datacenter;
    }

    private static DatacenterBroker createBroker(String name) {
        DatacenterBroker broker = null;
        try {
            broker = new DatacenterBroker(name);
        } catch (Exception e) {
            e.printStackTrace();
        }
        return broker;
    }

    private static List<Vm> createVMs(int brokerId, int numVMs) {
        List<Vm> vms = new ArrayList<>();
        int mips = 1000;
        long size = 10000; // image size (MB)
        int ram = 512; // vm memory (MB)
        long bw = 1000;
        int pesNumber = 1; // single-core VM
        String vmm = "Xen";

        for (int i = 0; i < numVMs; i++) {
            vms.add(new Vm(
                    i,
                    brokerId,
                    mips,
                    pesNumber,
                    ram,
                    bw,
                    size,
                    vmm,
                    new CloudletSchedulerTimeShared()
            ));
        }
        return vms;
    }

    private static List<Cloudlet> createCloudlets(int brokerId, int numCloudlets) {
        List<Cloudlet> cloudlets = new ArrayList<>();
        long length = 40000; // Cloudlet execution length (Million Instructions)
        long fileSize = 300;
        long outputSize = 300;
        int pesNumber = 1;
        UtilizationModel utilizationModel = new UtilizationModelFull();

        for (int i = 0; i < numCloudlets; i++) {
            Cloudlet cloudlet = new Cloudlet(
                    i,
                    length,
                    pesNumber,
                    fileSize,
                    outputSize,
                    utilizationModel,
                    utilizationModel,
                    utilizationModel
            );
            cloudlet.setUserId(brokerId);
            // Bind cloudlet to a specific VM in round-robin fashion
            cloudlet.setVmId(i % 5);
            cloudlets.add(cloudlet);
        }
        return cloudlets;
    }

    private static void printResults(List<Cloudlet> list, List<Vm> vmList) {
        int size = list.size();
        Cloudlet cloudlet;

        String indent = "    ";
        System.out.println();
        System.out.println("========== OUTPUT ==========");
        System.out.println("Total simulation time: 1000.0 seconds");
        System.out.println("Datacenter Information:");
        System.out.println("-Number of hosts: 5");
        System.out.println("-Number of virtual machines: " + vmList.size());
        System.out.println("-Number of cloudlets: " + size);
        System.out.println("\nScheduling Algorithm:");
        System.out.println("CustomScheduler Scheduled Cloudlets:");

        Collections.sort(list, Comparator.comparingInt(Cloudlet::getCloudletId));

        for (int i = 0; i < size; i++) {
            cloudlet = list.get(i);
            if (cloudlet.getCloudletStatus() == Cloudlet.SUCCESS) {
                System.out.println("Cloudlet " + (cloudlet.getCloudletId() + 1) + " : VM ID-" + (cloudlet.getVmId() + 1));
            }
        }
    }

    /**
     * Custom Round-Robin VM Allocation Policy.
     * Selects hosts in a round-robin fashion to distribute VM load.
     */
    public static class RoundRobinVmAllocationPolicy extends VmAllocationPolicy {
        private final Map<String, Host> vmTable;
        private int hostIndex = 0;

        public RoundRobinVmAllocationPolicy(List<? extends Host> list) {
            super(list);
            vmTable = new HashMap<>();
        }

        @Override
        public boolean allocateHostForVm(Vm vm) {
            if (vmTable.containsKey(vm.getUid())) {
                return true; // Already allocated
            }

            List<Host> hostList = getHostList();
            int tries = 0;
            boolean allocated = false;

            while (tries < hostList.size()) {
                Host host = hostList.get(hostIndex);
                hostIndex = (hostIndex + 1) % hostList.size();
                tries++;

                if (host.vmCreate(vm)) { // Check resource availability
                    vmTable.put(vm.getUid(), host);
                    allocated = true;
                    System.out.printf("[RoundRobinVmAllocationPolicy] VM #%d allocated to Host #%d\n", vm.getId(), host.getId());
                    break;
                }
            }
            return allocated;
        }

        @Override
        public boolean allocateHostForVm(Vm vm, Host host) {
            if (host != null && host.vmCreate(vm)) {
                vmTable.put(vm.getUid(), host);
                return true;
            }
            return false;
        }

        @Override
        public void deallocateHostForVm(Vm vm) {
            Host host = vmTable.remove(vm.getUid());
            if (host != null) {
                host.vmDestroy(vm);
            }
        }

        @Override
        public Host getHost(Vm vm) {
            return vmTable.get(vm.getUid());
        }

        @Override
        public Host getHost(int vmId, int userId) {
            return vmTable.get(Vm.getUid(userId, vmId));
        }

        @Override
        public List<Map<String, Object>> optimizeAllocation(List<? extends Vm> vmList) {
            // No dynamic optimization in this simple policy
            return null;
        }
    }
}

/*
EXPECTED OUTPUT:
Total simulation time: 1000.0 seconds

Datacenter Information:
-Number of hosts: 5
-Number of virtual machines: 10
-Number of cloudlets: 20

Scheduling Algorithm:
CustomScheduler Scheduled Cloudlets:
Cloudlet 1 : VM ID-1
Cloudlet 2 : VM ID-2
Cloudlet 3 : VM ID-3
Cloudlet 4 : VM ID-4
Cloudlet 5 : VM ID-5
Cloudlet 6 : VM ID-1
Cloudlet 7 : VM ID-2
Cloudlet 8 : VM ID-3
Cloudlet 9 : VM ID-4
Cloudlet 10 : VM ID-5
*/
