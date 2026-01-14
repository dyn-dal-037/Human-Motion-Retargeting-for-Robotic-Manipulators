def clamp(value, vmin, vmax):
    return max(vmin, min(value, vmax))


def map_human_to_servo(
    angle,
    human_min=0.0,
    human_max=180.0,
    servo_min=10,
    servo_max=170
):
    """
    Maps a human joint angle (degrees) to a servo-safe angle.

    Args:
        angle (float): Human joint angle in degrees
        human_min (float): Min expected human angle
        human_max (float): Max expected human angle
        servo_min (int): Servo lower limit
        servo_max (int): Servo upper limit

    Returns:
        int: Safe servo angle
    """
    # Linear mapping
    mapped = servo_min + (
        (angle - human_min)
        * (servo_max - servo_min)
        / (human_max - human_min)
    )

    return int(clamp(mapped, servo_min, servo_max))
