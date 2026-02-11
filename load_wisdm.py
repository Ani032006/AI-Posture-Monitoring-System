import cv2
import numpy as np

# ============================================
# WEBCAM POSTURE MONITORING SYSTEM
# ============================================

def run_webcam_posture_mode():

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Camera not opening.")
        return

    baseline_x = None
    baseline_y = None
    baseline_h = None

    smooth_x = None
    smooth_y = None
    smooth_h = None

    alpha = 0.2   # smoothing factor

    posture_message = "Initializing..."
    good_frames = 0
    bad_frames = 0

    print("Webcam posture mode started. Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(80, 80)
        )

        if len(faces) > 0:

            # Select largest detected face
            faces = sorted(faces, key=lambda f: f[2]*f[3], reverse=True)
            x, y, w, h = faces[0]

            cx = x + w // 2
            cy = y + h // 2

            # ---------- SMOOTHING ----------
            if smooth_x is None:
                smooth_x, smooth_y, smooth_h = cx, cy, h
            else:
                smooth_x = alpha * cx + (1-alpha) * smooth_x
                smooth_y = alpha * cy + (1-alpha) * smooth_y
                smooth_h = alpha * h + (1-alpha) * smooth_h

            # ---------- BASELINE SETUP ----------
            if baseline_y is None:
                baseline_x = smooth_x
                baseline_y = smooth_y
                baseline_h = smooth_h

            vertical_dev = smooth_y - baseline_y
            horizontal_dev = smooth_x - baseline_x
            size_ratio = smooth_h / baseline_h

            posture = "Good"

            # ---------- POSTURE CLASSIFICATION ----------
            if vertical_dev > 15 or size_ratio > 1.15:
                posture = "Severe Slouch"
            elif vertical_dev > 8 or size_ratio > 1.08:
                posture = "Mild Slouch"
            elif abs(horizontal_dev) > 15:
                posture = "Head Tilt"

            # ---------- STABILITY CONTROL ----------
            if posture == "Good":
                good_frames += 1
                bad_frames = 0
            else:
                bad_frames += 1
                good_frames = 0

            # Update baseline only when stable good posture
            if good_frames > 10:
                baseline_x = smooth_x
                baseline_y = smooth_y
                baseline_h = smooth_h

            # ---------- MESSAGE ----------
            if posture == "Good":
                posture_message = "Good posture. Keep it up."
            elif posture == "Mild Slouch":
                posture_message = "Straighten your back slightly."
            elif posture == "Severe Slouch":
                posture_message = "Sit upright and pull head back."
            elif posture == "Head Tilt":
                if horizontal_dev > 0:
                    posture_message = "Tilt head slightly to the left."
                else:
                    posture_message = "Tilt head slightly to the right."

        # ---------- DISPLAY ----------
        cv2.putText(
            frame,
            posture_message,
            (30, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 0, 255),
            2
        )

        cv2.imshow("AI Posture Monitoring System", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


# ============================================
# MAIN EXECUTION BLOCK
# ============================================

if __name__ == "__main__":
    print("Starting AI Posture Monitoring System...")
    run_webcam_posture_mode()
