import random
import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

# Simulator setup
aer_simulator = AerSimulator()
MANUAL_SIMULATOR_SEED_COUNTER = 42

CHSH_BASIS_PAIRS = [('0', '45'), ('0', '135'), ('90', '45'), ('90', '135')]

def set_simulator_seed(seed: int):
    global MANUAL_SIMULATOR_SEED_COUNTER
    MANUAL_SIMULATOR_SEED_COUNTER = seed

def run_circuit(circ: QuantumCircuit, shots=1) -> dict:
    """Run a quantum circuit on the simulator."""
    global MANUAL_SIMULATOR_SEED_COUNTER
    global aer_simulator
    
    current_run_seed = MANUAL_SIMULATOR_SEED_COUNTER
    MANUAL_SIMULATOR_SEED_COUNTER += 1
    
    circ = transpile(circ, aer_simulator)
    result = aer_simulator.run(circ, shots=shots, seed_simulator=current_run_seed).result()
    return result.get_counts(circ)


def apply_basis_transformation(circuit: QuantumCircuit, qubit_index: int, basis: str) -> QuantumCircuit:
    """Apply rotation to measure in a specific basis."""
    transformed = circuit.copy()
    if basis == '0':
        pass  # No rotation for Z basis
    elif basis == '90':
        transformed.h(qubit_index)
    elif basis == '45':
        transformed.ry(-np.pi/4, qubit_index)
    elif basis == '135':
        transformed.ry(-3*np.pi/4, qubit_index)
    else:
        raise ValueError(f"Unknown basis: {basis}")
    return transformed


def measure_bell_pair(circuit: QuantumCircuit, alice_basis: str, bob_basis: str) -> str:
    """Measure a Bell pair with specified bases."""
    meas_qc = circuit.copy()
    meas_qc = apply_basis_transformation(meas_qc, 0, alice_basis)
    meas_qc = apply_basis_transformation(meas_qc, 1, bob_basis)
    meas_qc.measure_all()
    counts = run_circuit(meas_qc, shots=1)
    return list(counts.keys())[0]


def organize_measurements_by_basis(results, alice_bases, bob_bases):
    """Group measurement results by basis pair for correlation calculation."""
    unique_alice = list(set(alice_bases))
    unique_bob = list(set(bob_bases))
    counts = {}
    for a in unique_alice:
        for b in unique_bob:
            counts[(a, b)] = {'00': 0, '01': 0, '10': 0, '11': 0}
    for i, result in enumerate(results):
        a_base = alice_bases[i]
        b_base = bob_bases[i]
        if result in counts[(a_base, b_base)]:
            counts[(a_base, b_base)][result] += 1
    return counts


def calculate_correlations(measurements):
    """Calculate E(a,b) correlation for each basis pair."""
    correlations = {}
    for basis_pair, results in measurements.items():
        total = sum(results.values())
        if total > 0:
            E = (results['00'] + results['11'] - results['01'] - results['10']) / total
            correlations[basis_pair] = E
        else:
            correlations[basis_pair] = 0
    return correlations


def generate_random_bases(length, options):
    """Generate a list of random measurement bases."""
    return [random.choice(options) for _ in range(length)]


def measure_all_pairs(bell_pairs, alice_bases, bob_bases):
    """Measure all Bell pairs with the specified bases."""
    results = []
    for qc, a_base, b_base in zip(bell_pairs, alice_bases, bob_bases):
        result = measure_bell_pair(qc, a_base, b_base)
        results.append(result)
    return results


def extract_e91_key_and_bell_test_data(results, alice_bases, bob_bases):
    """Sift measurement results into key generation and Bell test data."""
    key_results = []
    chsh_results = []
    chsh_alice_bases = []
    chsh_bob_bases = []
    for result, a_base, b_base in zip(results, alice_bases, bob_bases):
        if a_base == b_base:
            key_results.append(result)
        elif (a_base, b_base) in CHSH_BASIS_PAIRS:
            chsh_results.append(result)
            chsh_alice_bases.append(a_base)
            chsh_bob_bases.append(b_base)
    return {
        'key_results': key_results,
        'chsh_results': chsh_results,
        'chsh_alice_bases': chsh_alice_bases,
        'chsh_bob_bases': chsh_bob_bases,
    }
