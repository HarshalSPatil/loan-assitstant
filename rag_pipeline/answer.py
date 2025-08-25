import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from google import genai
from rag_pipeline.query import retrieve
from dotenv import load_dotenv

# Load .env and configure Gemini
load_dotenv()
os.getenv("GEMINI_API_KEY")
client = genai.Client()

def answer(query: str) -> str:
    """
    Retrieve supporting docs via RAG, then ask Gemini to answer using that context.
    """
    # Fetch relevant docs
    docs = retrieve(query)
  
    # Build the prompt (or use messages for multi-turn)
    context = "\n\n".join(docs)
    # print(f"Context for query '{query}':\n{context}\n")
    

    prompt=""""You are Loan Product Assistant, an expert in home loan products, "
            "EMI calculations, interest rates, and related financial concepts. "
            "Your goal is to provide clear, actionable, and accurate answers "
            "based **only** on the information in the provided context. "
            "If the context does not contain enough information to fully answer "
            "the question, you must say you don’t have enough data rather than guess.
            "Instructions:\n"
            "- Base your answer strictly on the this context/document.\n"
            "- Explain complex terms in simple language and specific to question.\n"
            "- Provide a concise answer and, only if applicable, a step-by-step guide.\n"
            "- If you lack sufficient context, reply: “I don’t have enough information to answer that.”\n\n"
            
            """
    try:
        # Call Gemini’s free flash model
        response=client.models.generate_content(model="gemini-2.5-flash",
                         contents=[context,prompt,query],
                            )

        return response.text.strip()

    # except errors.AuthenticationError:
    #     raise RuntimeError("Invalid or missing GEMINI_API_KEY.")
    # except errors.RateLimitError:
    #     raise RuntimeError("Gemini rate limit exceeded, please retry later.")
    except Exception as e:
        raise RuntimeError(f"Gemini API error: {e}")

# Example usage
# if __name__ == "__main__":
#     print(answer("Explain how EMI calculation works for a home loan."))

# Uncomment the following code to use OpenAI's GPT-3.5-Turbo instead of Gemini
# openai.api_key = os.getenv("OPENAI_API_KEY")

# def answer(query: str) -> str:
#     docs = retrieve(query)
#     prompt = (
#         "Use the following context to answer the question:\n\n"
#         + "\n\n".join(docs)
#         + f"\n\nQuestion: {query}\nAnswer:"
#     )

#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[{"role": "user", "content": prompt}],
#         max_tokens=1500,
#         temperature=0.7
#     )
#     return response.choices[0].message.content.strip()