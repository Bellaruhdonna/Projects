import speech_recognition as sr
import pyttsx3

# Initialize the speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    """Speak the provided text."""
    engine.say(text)
    engine.runAndWait()

def take_voice_input():
    """Capture symptoms from voice input."""
    with sr.Microphone() as source:
        print("Listening for symptoms...")
        talk("Please describe your symptoms.")
        try:
            voice = recognizer.listen(source)
            symptoms = recognizer.recognize_google(voice)
            print(f"Recognized symptoms: {symptoms}")
            return symptoms.lower()
        except sr.UnknownValueError:
            talk("Sorry, I didn't catch that. Could you please repeat?")
        except sr.RequestError:
            talk("I'm having trouble connecting to the speech service. Please try again later.")
        return ""

def detect_disease(symptoms):
    # Dictionary of symptoms mapped to cardiovascular diseases
    symptom_disease_map = {
        "chest pain": ["Angina", "Heart Attack", "Aortic Dissection"],
        "shortness of breath": ["Heart Failure", "Pulmonary Embolism", "Coronary Artery Disease"],
        "palpitations": ["Arrhythmia", "Atrial Fibrillation"],
        "dizziness": ["Arrhythmia", "Low Blood Pressure", "Heart Block"],
        "swelling in legs": ["Heart Failure", "Deep Vein Thrombosis"],
        "fatigue": ["Heart Failure", "Anemia", "Coronary Artery Disease"],
        "fainting": ["Arrhythmia", "Aortic Stenosis", "Heart Block"],
        "bluish skin": ["Congenital Heart Disease", "Heart Failure"],
        "rapid heartbeat": ["Arrhythmia", "Tachycardia"],
        "high blood pressure": ["Hypertension", "Atherosclerosis"],
        "low blood pressure": ["Shock", "Heart Block"]
    }

    # Set to store possible diseases
    possible_diseases = set()

    # Match symptoms with diseases
    for symptom in symptoms:
        if symptom in symptom_disease_map:
            possible_diseases.update(symptom_disease_map[symptom])
        else:
            print(f"Symptom '{symptom}' not found in database.")

    return list(possible_diseases)

def main():
    talk("Welcome to Cardiovascular Symptom-to-Disease Detection!")
    talk("Would you like to describe your symptoms using your voice or type them?")
    
    # Take user input for symptoms
    user_choice = input("Enter 'voice' for voice input or 'text' to type your symptoms: ").strip().lower()
    if user_choice == 'voice':
        user_input = take_voice_input()
    else:
        talk("Please type your symptoms.")
        user_input = input("Your symptoms: ").lower()
    
    symptoms = [symptom.strip() for symptom in user_input.split(",")]

    # Detect diseases
    diseases = detect_disease(symptoms)

    # Display and speak results
    if diseases:
        talk("Based on the symptoms provided, the possible cardiovascular diseases are:")
        print("\nPossible cardiovascular diseases:")
        for disease in diseases:
            print(f"- {disease}")
            talk(disease)
    else:
        talk("No matching diseases found. Please consult a cardiologist for accurate diagnosis.")
        print("\nNo matching diseases found.")

if __name__ == "__main__":
    main()
