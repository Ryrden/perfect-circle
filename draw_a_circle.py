import pyautogui
import math
import time
import keyboard

START_TIMER = 3  # seconds before drawing starts
CIRCLE_RADIUS = 300  # size of the circle to draw
STEP_INCREMENT = 12  # degrees to increment for each step in the circle drawing

def wait_for_enter_key() -> None:
    print("Move the mouse to the center of the circle and press Enter to start.")
    while keyboard.read_key() != "enter":
        time.sleep(0.1)  # Prevent high CPU usage

def countdown(seconds: int) -> None:
    for remaining in range(max(0, seconds), -1, -1):
        print(f"Starting in {remaining}...")
        time.sleep(1)

def get_circle_points(center: tuple[float, float], radius: float, steps: int = 360) -> list[tuple[float,float]]:
    points = []
    for i in range(0, steps + 1, STEP_INCREMENT):
        angle = math.radians(i)
        x = center[0] + radius * math.cos(angle)
        y = center[1] + radius * math.sin(angle)
        points.append((x, y))
    return points

def draw_circle(center: tuple[float,float], radius: float) -> bool:
    start_position = (center[0] + radius, center[1])
    pyautogui.moveTo(*start_position)
    pyautogui.mouseDown()

    for point in get_circle_points(center, radius):
        if keyboard.is_pressed('esc'):
            pyautogui.mouseUp()
            return False
        pyautogui.moveTo(*point)

    pyautogui.mouseUp()
    return True

def main():
    if 360 % STEP_INCREMENT != 0:
        print("STEP_INCREMENT must be a divisor of 360 for a complete circle.")
        return
    
    if CIRCLE_RADIUS < 1:
        print("CIRCLE_RADIUS must be greater than 0.")
        return

    wait_for_enter_key()
    countdown(START_TIMER)
    
    center = pyautogui.position()
    print(f"Center defined as {center}.")
    print("Drawing the circle. Press Esc to cancel.")
    if draw_circle(center, CIRCLE_RADIUS):
        print("Circle drawing complete.")
    else:
        print("Drawing cancelled.")

if __name__ == "__main__":
    main()
