from datetime import datetime

def sample_responses(input_text):

    if input_text in ["hello","hi","namaste"]:
        return "Hello, I am Garen, How are you doing?"

    elif input_text in ["help","functions","help!"]:
        return "I can send cute dog pics! and tell current time"
    
    elif input_text in ["time","what is the time?"]:
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)
    
    else:
        return "Sorry i dont get it!"