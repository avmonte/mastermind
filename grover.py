import cirq


def grover_search(num_qubits, oracle):
    # Create qubits
    qubits = [cirq.LineQubit(i) for i in range(num_qubits)]

    # Create the circuit
    circuit = cirq.Circuit()

    # Apply Hadamard gates to all qubits to create superposition
    circuit.append(cirq.H.on_each(qubits))

    # Apply the oracle
    circuit.append(oracle)

    # Apply the Grover diffusion operator
    circuit.append(apply_diffusion_operator(qubits))

    # Measure the qubits
    circuit.append(cirq.measure(*qubits, key='result'))

    return circuit


def apply_diffusion_operator(qubits):
    """Construct the Grover diffusion operator."""
    num_qubits = len(qubits)
    circuit = cirq.Circuit()

    # Apply Hadamard gates to all qubits
    circuit.append(cirq.H.on_each(qubits))

    # Apply X gates to all qubits
    circuit.append(cirq.X.on_each(qubits))

    # Apply multi-controlled Z gate
    circuit.append(cirq.Z(qubits[-1]).controlled_by(*qubits[:-1]))

    # Apply X gates to all qubits
    circuit.append(cirq.X.on_each(qubits))

    # Apply Hadamard gates to all qubits
    circuit.append(cirq.H.on_each(qubits))

    return circuit


# Example of a custom oracle (marking the state |11...1>)
def custom_oracle(qubits):
    num_qubits = len(qubits)
    circuit = cirq.Circuit()

    # Apply X gates to invert all qubits
    circuit.append(cirq.X.on_each(qubits))

    # Apply multi-controlled Z gate
    circuit.append(cirq.Z(qubits[-1]).controlled_by(*qubits[:-1]))

    # Apply X gates again to revert the inversion
    circuit.append(cirq.X.on_each(qubits))

    return circuit


# Parameters
num_qubits = 3
oracle = custom_oracle([cirq.LineQubit(i) for i in range(num_qubits)])

# Create the Grover circuit
grover_circuit = grover_search(num_qubits, oracle)

# Print the circuit
print("Grover's algorithm circuit:")
print(grover_circuit)

# Simulate the circuit
simulator = cirq.Simulator()
result = simulator.run(grover_circuit, repetitions=100)

# Print the results
print("Results:")
print(result.histogram(key='result'))
