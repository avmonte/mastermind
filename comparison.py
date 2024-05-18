from tools import *

# Example usage
num_qubits = 3
humanA = [1, 0, 0]
humanB = [1, 0, 1]
A = [NamedQubit(f'A{i}') for i in range(num_qubits)]
B = [NamedQubit(f'B{i}') for i in range(num_qubits)]

# Prepare qubits (for testing, we can manually set some states)
circuit = Circuit()
circuit.append(initialize_qubits(A, B, [humanA, humanB]))


# Create the full circuit
circuit += comparison_check(A, B, [NamedQubit(f'e{i}') for i in range(num_qubits)])


# Simulate the circuit
circuit.append(measure(*[NamedQubit(f'e{i}') for i in range(num_qubits)], key='diffs'))

simulator = Simulator()
result = simulator.run(circuit, repetitions=1)

measurement = result.measurements['diffs'][0]
differences = sum(measurement)

print(circuit)
print("|" + "".join(str(i) for i in humanA) + ">", end=" |C| ")
print("|" + "".join(str(i) for i in humanB) + ">")
print("Number of differing bits:", differences)
