from cirq import *


def equality_check(A, B, e, E):
	circuit = Circuit()

	for i in range(len(A)):
		circuit.append(CNOT(A[i], e[i]))
		circuit.append(CNOT(B[i], e[i]))
		circuit.append(X(e[i]))

	for i in range(len(e)):
		circuit.append(CNOT(e[i], E[0]))

	return circuit


def comparison_check(A, B, e):
	circuit = Circuit()

	for i in range(len(A)):
		circuit.append(CNOT(A[i], e[i]))
		circuit.append(CNOT(B[i], e[i]))

	return circuit


def count_differences(A, B):
	n = len(A)
	e = [NamedQubit(f'e{i}') for i in range(n)]

	# Create the comparison circuit
	circuit = comparison_check(A, B, e)

	# Measurement of ancillary qubits to count differences
	circuit.append(measure(*e, key='diffs'))

	# Simulate the circuit
	simulator = Simulator()
	result = simulator.run(circuit, repetitions=1)

	# Get the measurement results
	measurement = result.measurements['diffs'][0]

	# Count the number of bits that differ
	differences = sum(measurement)

	return differences, circuit


def initialize_qubits(A, B, values):
	circuit = Circuit()

	for j in range(len(A)):
		if values[0][j] == 1:
			circuit.append(X(A[j]))

	for j in range(len(B)):
		if values[1][j] == 1:
			circuit.append(X(B[j]))

	return circuit
