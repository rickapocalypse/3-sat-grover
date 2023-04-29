from qiskit import QuantumCircuit
import matplotlib.pyplot as plt




def reflection(n):
    qc = QuantumCircuit(n+n, n)
    qc.h(list(range(0,n)))
    qc.barrier()
    qc.x(list(range(0,n)))
    qc.barrier()
    qc.h(n-1)
    qc.mcx(list(range(0,n-1)), n-1)
    qc.h(n-1)
    qc.barrier()
    qc.x(list(range(0,n)))
    qc.barrier()
    qc.h(list(range(0,n)))
    return qc
n = 2
qc = QuantumCircuit(n+n,n)
qc.h(list(range(0,n)))

qc.draw('mpl')
plt.show()