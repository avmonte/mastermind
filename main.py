from tools import *

num_qubits = 3
circuit = Circuit()

# Create qubits
A = [LineQubit(i) for i in range(num_qubits)]
B = [LineQubit(num_qubits + i) for i in range(num_qubits)]
e = [LineQubit(2*num_qubits + i) for i in range(num_qubits)]
E = [LineQubit(3*num_qubits)]

# Testing
# circuit.append(X(A[0]))

# Create the equality check circuit
circuit += equality_check(A, B, e, E)
print(circuit)

# Simulate the circuit
circuit.append(measure(E, key='result'))
simulator = Simulator()
result = simulator.run(circuit)
measurement = result.measurements['result']
print("Ancilla measurement result (1 means qubits are equal):", measurement[0][0])
