from qiskit import QuantumCircuit
import numpy as np

def create_bell_pair_singlet_state():
    """Returns a QuantumCircuit creating the |Ψ-⟩ Bell state."""
    qc = QuantumCircuit(2, 2)
    # Start with |11>
    qc.x(0)
    qc.x(1)
    # Apply Hadamard on qubit 0 to get (|01> - |11>)/sqrt(2)
    qc.h(0)
    # Apply CNOT to get (|01> - |10>)/sqrt(2) which is |Ψ-⟩
    qc.cx(0, 1)
    return qc

def apply_basis_transformation(qc: QuantumCircuit, qubit_index: int, measurement_angle: str):
    """
    Applies the appropriate unitary transformation for a given measurement angle.
    """
    if measurement_angle == '0':
        pass  # Z-basis, no transformation needed
    elif measurement_angle == '45':
        # Transformation for 45 degrees (pi/4)
        qc.ry(-np.pi/4, qubit_index)
    elif measurement_angle == '90':
        # Transformation for 90 degrees (X-basis)
        qc.ry(-np.pi/2, qubit_index)
        # Or equivalently: qc.h(qubit_index)
    elif measurement_angle == '-45':
        # Transformation for -45 degrees (-pi/4)
        qc.ry(np.pi/4, qubit_index)
    else:
        raise ValueError(f"Unknown angle: {measurement_angle}")
    return qc

def measure_bell_pair(bell_state: QuantumCircuit, alice_angle: str, bob_angle: str):
    """
    Simulates the measurement of a Bell pair by Alice and Bob at given angles.
    Returns: '00', '01', '10', or '11'
    """
    from qiskit_aer import Aer
    from qiskit import transpile
    
    # Create a copy so we don't modify the original circuit repeatedly in loops
    qc = bell_state.copy()
    
    # Apply Alice's transformation to qubit 0
    apply_basis_transformation(qc, 0, alice_angle)
    
    # Apply Bob's transformation to qubit 1
    apply_basis_transformation(qc, 1, bob_angle)
    
    # Measure
    qc.measure(0, 0)
    qc.measure(1, 1)
    
    # Run the simulation (1 shot)
    simulator = Aer.get_backend('qasm_simulator')
    compiled_circuit = transpile(qc, simulator)
    job = simulator.run(compiled_circuit, shots=1)
    result = job.result()
    
    # Get the count dict, e.g., {'01': 1}
    counts = result.get_counts(compiled_circuit)
    
    # Return the single outcome string
    return list(counts.keys())[0]

def calculate_chsh_value(results_a1_b1, results_a1_b2, results_a2_b1, results_a2_b2):
    """
    Calculates the CHSH parameter S given sets of measurement results.
    """
    def correlation(results):
        same = sum(1 for r in results if r in ['00', '11'])
        diff = sum(1 for r in results if r in ['01', '10'])
        total = len(results)
        if total == 0: return 0
        return (same - diff) / total
        
    E_a1_b1 = correlation(results_a1_b1)
    E_a1_b2 = correlation(results_a1_b2)
    E_a2_b1 = correlation(results_a2_b1)
    E_a2_b2 = correlation(results_a2_b2)
    
    # For the specific angles we chose and the |Ψ-⟩ state:
    S = E_a1_b1 - E_a1_b2 + E_a2_b1 + E_a2_b2
    return S
