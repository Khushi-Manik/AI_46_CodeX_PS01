from transformers import pipeline
from sentence_transformers import SentenceTransformer, util
import os

# Suppress TensorFlow warnings
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

# Load models
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# Updated Knowledge Base
knowledge_base = [
    {"question": "What is GST and why is it important?", "answer": "GST is an indirect tax levied on goods and services in India."},
    {"question": "How does IDMS ERP help in GST compliance?", "answer": "IDMS ERP ensures automatic tax calculations and GST return filing support."},
    {"question": "What modules does IDMS ERP offer?", "answer": "IDMS ERP includes modules for inventory management, finance, HR, sales, and procurement."},
    {"question": "How does IDMS ERP help in inventory management?", "answer": "IDMS ERP optimizes inventory tracking, stock levels, and supply chain efficiency."},
    {"question": "Can IDMS ERP generate automated financial reports?", "answer": "Yes, IDMS ERP provides automated financial reporting with real-time insights."},
    {"question": "Is IDMS ERP cloud-based?", "answer": "Yes, IDMS ERP is cloud-based and can be accessed from anywhere."},
    {"question": "How does IDMS ERP improve employee productivity?", "answer": "It streamlines processes, reduces manual work, and enhances collaboration."},
    {"question": "What security features does IDMS ERP provide?", "answer": "IDMS ERP offers role-based access control, encryption, and audit logs."},
    {"question": "Does IDMS ERP support multi-currency transactions?", "answer": "Yes, it allows businesses to handle transactions in multiple currencies."},
    {"question": "How does IDMS ERP integrate with third-party applications?", "answer": "It supports API integration with various business tools like CRM and payment gateways."},
    {"question": "What industries benefit the most from ERP systems?", "answer": "Industries like manufacturing, retail, healthcare, finance, and logistics benefit the most."},
    {"question": "What are the key benefits of using an ERP system?", "answer": "ERP improves efficiency, enhances data accuracy, reduces costs, and provides better reporting."},
    {"question": "How long does ERP implementation take?", "answer": "It depends on the company size, but typically it takes between 3 to 12 months."},
    {"question": "What is the difference between on-premise and cloud ERP?", "answer": "On-premise ERP is installed locally, while cloud ERP is hosted online and accessible remotely."},
    {"question": "Can ERP systems be customized?", "answer": "Yes, most ERP solutions offer customization to fit business needs."},
    {"question": "What challenges do companies face during ERP implementation?", "answer": "Common challenges include high costs, employee resistance, data migration, and training."},
    {"question": "Does ERP support mobile access?", "answer": "Yes, modern ERP systems provide mobile-friendly interfaces for remote access."},
    {"question": "How does ERP handle compliance and regulations?", "answer": "ERP automates compliance with tax laws, financial reporting standards, and industry regulations."},
    {"question": "How does ERP improve decision-making?", "answer": "ERP provides real-time data analytics, dashboards, and reporting for informed decision-making."}
]

# Compute embeddings for the knowledge base
kb_embeddings = {item["question"]: embedder.encode(item["question"], convert_to_tensor=True) for item in knowledge_base}

def get_erp_response(query):
    query_embedding = embedder.encode(query, convert_to_tensor=True)

    # Find the best-matching question using embeddings
    best_match = max(kb_embeddings, key=lambda k: util.pytorch_cos_sim(query_embedding, kb_embeddings[k]).item())

    # Find the best answer from knowledge base
    best_answer = next(item["answer"] for item in knowledge_base if item["question"] == best_match)

    # If query is a single keyword, check for direct keyword match in questions
    query_words = query.lower().split()
    for item in knowledge_base:
        question_words = item["question"].lower().split()
        if any(word in question_words for word in query_words):  # If any keyword matches
            best_answer = item["answer"]
            break

    return best_answer  # Directly return the answer without GPT-2 generation

# ---------------- Interactive Assistant ----------------
def run_interactive_assistant():
    print("Welcome to the ERP Assistant!")
    print("Ask any question about IDMS ERP system, or type 'exit' to quit.")
    print("-" * 50)

    while True:
        user_query = input("\nYour question: ")

        if user_query.lower() in ['exit', 'quit', 'bye']:
            print("Thank you for using the ERP Assistant. Goodbye!")
            break

        response = get_erp_response(user_query)  # Call function once
        print("\nResponse:\n" + response)  # Print response only once
        print("-" * 50)

if __name__ == "__main__":
    run_interactive_assistant()
