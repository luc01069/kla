
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
