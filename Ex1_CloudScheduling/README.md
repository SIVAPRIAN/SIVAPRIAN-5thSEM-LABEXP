# Simulate A Cloud Scenario Using Cloud Sim And Run A Scheduling Algorithm Not Present In Cloudsim

## Aim
To simulate a cloud environment using CloudSim and design/run a custom virtual machine scheduling policy (Round-Robin VM Allocation Policy) not present in CloudSim by default.

## Theory
CloudSim is a framework for modeling and simulation of cloud computing infrastructures and services. The virtual machine allocation policy determines how virtual machines (VMs) are mapped to physical nodes (Hosts) within a Datacenter.
- **Default Policy (`VmAllocationPolicySimple`)**: Uses a First-Fit strategy, allocating VMs to the first host that can satisfy their resource requirements. This can lead to unbalanced resource utilization and hot-spots.
- **Round-Robin VM Allocation Policy (Custom)**: Sequentially assigns VMs to physical hosts in a circular fashion. This ensures that the VM instances are distributed evenly across the available physical infrastructure, improving resource utilization balance.

## Algorithm
1. **Initialize CloudSim**: Call `CloudSim.init(numUsers, calendar, traceFlag)`.
2. **Create Datacenter Characteristics**: Define architecture, OS, VMM, and hosts with predefined capacity (MIPS, RAM, Storage, Bandwidth).
3. **Instantiate Custom VM Allocation Policy**: Pass the list of hosts to the custom `RoundRobinVmAllocationPolicy`.
4. **Create Datacenter**: Instantiate the `Datacenter` object using the custom allocation policy.
5. **Create Datacenter Broker**: Instantiate a broker to coordinate VM creation and Cloudlet submissions.
6. **Create VMs & Cloudlets**: Configure VM configurations (MIPS, RAM, etc.) and Cloudlets (length, utilization model). Submit them to the broker.
7. **Start Simulation**: Run the simulation using `CloudSim.startSimulation()`.
8. **Retrieve and Print Results**: Retrieve finished Cloudlets and compile simulation execution details.
9. **Stop Simulation**: Clean up resources using `CloudSim.stopSimulation()`.

## Requirements
- Java Development Kit (JDK) 8 or later.
- CloudSim 3.0.3 JAR.
- Apache Commons Math 3.x (dependency of CloudSim).

## How to Run
1. Download `cloudsim-3.0.3.jar` and `commons-math3-3.6.1.jar` into this directory.
2. Compile the Java code:
   ```bash
   javac -cp ".;cloudsim-3.0.3.jar;commons-math3-3.6.1.jar" CustomSchedulingSimulation.java
   ```
3. Run the compiled application:
   ```bash
   java -cp ".;cloudsim-3.0.3.jar;commons-math3-3.6.1.jar" CustomSchedulingSimulation
   ```

## Sample Output
```
Starting Cloud Custom Scheduling Simulation...
[RoundRobinVmAllocationPolicy] VM #0 allocated to Host #0
[RoundRobinVmAllocationPolicy] VM #1 allocated to Host #1
[RoundRobinVmAllocationPolicy] VM #2 allocated to Host #2
[RoundRobinVmAllocationPolicy] VM #3 allocated to Host #3
[RoundRobinVmAllocationPolicy] VM #4 allocated to Host #4

========== OUTPUT ==========
Total simulation time: 1000.0 seconds
Datacenter Information:
-Number of hosts: 5
-Number of virtual machines: 5
-Number of cloudlets: 10

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
Simulation completed successfully.
```

## Result
A cloud scenario was simulated successfully using CloudSim. A custom Round-Robin VM Allocation policy was designed, implemented, and executed to demonstrate resource scheduling across virtual resources.
