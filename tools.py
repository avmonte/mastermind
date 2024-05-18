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
