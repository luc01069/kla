import matplotlib.pyplot as plt
from kla import kla_simulation  

def main():
    # Initial parameters
    initial_volume = 10  # liters
    initial_kla = 0.5  # 1/h
    scaling_factors = [1, 2, 5, 10]  # Example scaling factors

    # Simulate scaling
    results = []
    for factor in scaling_factors:
        scaled_volume, scaled_kla = kla_simulation(initial_volume, initial_kla, factor)
        print(f"{scaled_volume}, {scaled_kla}")
        results.append((scaled_volume, scaled_kla))

    # Extract results for plotting
    volumes = [r[0] for r in results]
    klas = [r[1] for r in results]

    # Plotting
    plt.figure(figsize=(8, 5))
    plt.plot(volumes, klas, marker='o', label='KLA Scaling')
    plt.xlabel('Scaled Volume (L)')
    plt.ylabel('KLA Value (1/h)')
    plt.title('KLA Scaling Simulation for Fermenter')
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
