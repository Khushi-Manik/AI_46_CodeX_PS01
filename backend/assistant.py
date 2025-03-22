from erp_assistant import get_erp_response
import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"  # Disable oneDNN warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Suppress TensorFlow warnings


def run_interactive_assistant():
    print("Welcome to the ERP Assistant!")
    print("Ask any question about IDMS ERP system, or type 'exit' to quit.")
    print("-" * 50)
    
    while True:
        user_query = input("\nYour question: ")
        
        if user_query.lower() in ['exit', 'quit', 'bye']:
            print("Thank you for using the ERP Assistant. Goodbye!")
            break
        
        response = get_erp_response(user_query)
        
        print("\nResponse:")
        print(response)
        print("-" * 50)

if __name__ == "__main__":
    run_interactive_assistant()
