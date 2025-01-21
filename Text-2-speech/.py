import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# import speech_recognition as sr

# Step 1: Prepare the Dataset
data = {
    'Feature1': [1, 0, 1, 0],
    'Feature2': [0, 1, 1, 0],
    'Feature3': [1, 1, 0, 0],
    'Disease': ['Disease A', 'Disease B', 'Disease A', 'Disease C']
    # 'Chest Pain (1=Yes, 0=No)': [1, 0, 1, 0],
    # 'Shortness of Breath (1=Yes, 0=No)': [0, 1, 1, 0],
    # 'High Blood Pressure (1=Yes, 0=No)': [1, 1, 0, 0],
    # 'Disease': ['Angina', 'Heart Failure', 'Angina', 'Healthy']
}
df = pd.DataFrame(data)

# Split features and labels
X = df[['Feature1', 'Feature2', 'Feature3']]
y = df['Disease']

# Step 2: Train the Model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Test accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# Step 3: Speech Recognition Function
# def speech_to_text():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening for symptoms...")
#         try:
#             audio = recognizer.listen(source)
#             text = recognizer.recognize_google(audio)
#             print(f"You said: {text}")
#             return text
#         except sr.UnknownValueError:
#             return "Sorry, I couldn't understand the audio."
#         except sr.RequestError:
#             return "Speech recognition service is unavailable."

# Step 4: Prediction Function
def predict_disease(features):
    try:
        features_list = list(map(int, features.split(',')))
        input_data = pd.DataFrame([features_list], columns=X.columns)
        prediction = model.predict(input_data)[0]
        return f"Predicted Disease: {prediction}"
    except Exception as e:
        return f"Error: {e}"

# Step 5: Speech Recognition Chatbot
def disease_prediction_chatbot(): 
    print("Welcome to the Disease Prediction Chatbot!")
    print("Would you like to communicate through 'Chat' (text) or 'Speech' (voice)? Please type 'Chat' or 'Speech'.")
    
    mode = input("Enter your choice: ").strip().lower()

    if mode == "chat":
        print("You chose Chat mode. Please enter your symptoms as comma-separated values (e.g., 1,0,1).")
        while True:
            user_input = input("Enter symptoms or 'exit' to quit: ")  # Correcting syntax of input
            if user_input.lower() in ["exit", "quit", "stop"]:
                print("Exiting the chatbot. Stay healthy!")
                break
            
            response = predict_disease(user_input)
            print(response)
    
    elif mode == "speech":
        print("You chose Speech mode. Please speak your symptoms clearly.")
        while True:
            user_input = speech_to_text()
            if "Sorry" in user_input or "unavailable" in user_input:
                print(user_input)  # Print the error message from speech recognition
                continue
            
            if user_input.lower() in ["exit", "quit", "stop"]:
                print("Exiting the chatbot. Stay healthy!")
                break

            response = predict_disease(user_input)
            print(response)
    
    else:
        print("Invalid choice. Please restart the program and choose 'Chat' or 'Speech'.")

        
        
        response = predict_disease(user_input)
        print(response)

# Run the Chatbot
if __name__ == "__main__":
    disease_prediction_chatbot()
