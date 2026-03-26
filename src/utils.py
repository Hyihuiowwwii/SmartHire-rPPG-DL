def calculate_status(bpm):
    if bpm == 0:
        return "Collecting data"
    elif bpm < 60:
        return "Low heart rate"
    elif bpm > 100:
        return "High heart rate"
    else:
        return "Normal heart rate"
