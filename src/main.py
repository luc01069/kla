import matplotlib.pyplot as plt

def kla_simulation(volume, kla_initial, scale_factor):
    """
    Simulates the KLA value scaling for a fermenter.

    Parameters:
    - volume: Initial volume of the fermenter (liters).
    - kla_initial: Initial KLA value (1/h).
    - scale_factor: Factor by which the fermenter is scaled.

    Returns:
    - scaled_volume: New volume after scaling.
    - scaled_kla: New KLA value after scaling.
    """
    scaled_volume = volume * scale_factor
    scaled_kla = kla_initial * (volume / scaled_volume)**(2/3)  # Empirical scaling law
    return scaled_volume, scaled_kla

def main():
    # Initial parameters
    initial_volume = 10  # liters
    initial_kla = 0.5  # 1/h
    scaling_factors = [1, 2, 5, 10]  # Example scaling factors

    # Simulate scaling
    results = []
    for factor in scaling_factors:
        scaled_volume, scaled_kla = kla_simulation(initial_volume, initial_kla, factor)
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
