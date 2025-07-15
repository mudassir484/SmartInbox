import threading
from llama_cpp import Llama

# Thread lock to avoid simultaneous llama() calls
llm_lock = threading.Lock()

# Load LLaMA model
llm = Llama(
    model_path="models/llama-3.2-3b-instruct-q3_k_l.gguf",
    n_ctx=512,
    n_threads=6,
    n_gpu_layers=0,
    verbose=False
)

# ------------------------- #
# LLaMA Wrapper
# ------------------------- #

def generate_llama_response(prompt: str, max_tokens=64):
    try:
        with llm_lock:
            output = llm(
                prompt=prompt,
                max_tokens=max_tokens,
                temperature=0.1,
                top_p=0.9,
                stop=["\n", "User:", "Answer:"]
            )
        return output["choices"][0]["text"].strip()
    except Exception as e:
        print("[LLaMA ERROR]:", str(e))
        return None  # Trigger fallback
        

# ------------------------- #
# Tone Classifier
# ------------------------- #

def classify_email_tone(email_text: str) -> str:
    prompt = (
        "You are a tone classifier. Respond with one word: polite, urgent, neutral, or formal.\n\n"
        "Email: Please let me know your feedback at your convenience.\nAnswer: polite\n"
        "Email: I need this done immediately!\nAnswer: urgent\n"
        "Now I need you to answer about the email below:\n"
        f"Email: {email_text.strip()}\nAnswer:"
    )

    result = generate_llama_response(prompt, max_tokens=8)
    if result:
        result = result.lower()
        print("[Tone Raw]:", repr(result))
        for tone in ["polite", "urgent", "neutral", "formal"]:
            if tone in result:
                return tone
        return f"unknown ({result})"

    # 🔁 Fallback: Keyword-based tone detection
    text = email_text.lower()
    if any(word in text for word in ["please", "kindly", "thank you"]):
        return "polite"
    elif any(word in text for word in ["immediately", "asap", "urgent"]):
        return "urgent"
    elif any(word in text for word in ["sincerely", "regards", "respectfully"]):
        return "formal"
    else:
        return "failed"

# ------------------------- #
# Spam Detector
# ------------------------- #

def detect_spam(email_text: str) -> bool:
    prompt = (
        "You are a spam detector. Respond only with 'yes' or 'no'.\n\n"
        "Email: You've won a free prize! Click this link to claim.\nAnswer: yes\n"
        "Email: Let's schedule a meeting for next week.\nAnswer: no\n"
        f"Email: {email_text.strip()}\nAnswer:"
    )

    result = generate_llama_response(prompt, max_tokens=5)
    if result:
        result = result.lower()
        print("[Spam Raw]:", repr(result))
        return "yes" in result

    # 🔁 Fallback: Keyword-based spam detection
    spam_keywords = ["click here", "free", "prize", "congratulations", "winner", "claim", "urgent offer"]
    return any(word in email_text.lower() for word in spam_keywords)
