# Lab Experiment 3: Buffer Overflow Attack Demonstration

## 1. Aim
To implement and demonstrate a buffer overflow attack by showing how providing oversized input can overwrite memory and alter the normal program execution flow.

## 2. Algorithm
1. **Program Setup**: Write a vulnerable C program that uses unsafe functions (`gets()` or `strcpy()`) to copy user input into a fixed-size buffer.
2. **Normal Execution**: Run the program with valid input to observe normal behavior.
3. **Overflow Input**: Provide input larger than the buffer size so that extra characters overwrite memory locations beyond the buffer.
4. **Memory Corruption**: Observe how the overflow overwrites nearby variables or affects the control flow of the program.
5. **Demonstration**: Compare normal and overflowed runs to illustrate how attackers can misuse this vulnerability.

## 3. Output
> [!IMPORTANT]
> **Execution Output:**
>
> **Case 1: Normal Input**
> ```text
> Enter some text: hello
> You entered: hello
> Secret value: 0
> ❌ Normal Execution. Secret not changed.
> ```
>
> **Case 2: Overflow Input (long string)**
> ```text
> Enter some text: AAAAAAAAAAAAAAAA12345
> You entered: AAAAAAAAAAAAAAAA12345
> Secret value: 12345
> ✅ Buffer Overflow Successful! Secret value changed!
> ```

## 4. Result
The experiment successfully demonstrated that providing oversized input can overwrite memory locations and alter the normal program execution flow, proving that buffer overflow vulnerabilities can be exploited to compromise program security.
