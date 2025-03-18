from transformers import pipeline

# Use a text generation model (e.g., GPT-Neo) instead of just summarization
generator = pipeline("text-generation", model="EleutherAI/gpt-neo-125M")

def generate_content(posts):
    # Combine posts into a prompt
    combined_text = " ".join([post["text"] for post in posts])
    max_input_length = 500  # Adjust based on model limits
    if len(combined_text) > max_input_length:
        combined_text = combined_text[:max_input_length]

    # Generate content with AI
    prompt = f"Based on recent market analysis and economic updates: {combined_text}, provide a concise summary and insight."
    generated = generator(prompt, max_length=150, num_return_sequences=1, do_sample=True)[0]["generated_text"]

    # Add credits
    credited_accounts = ", ".join([f"@{post['user']}" for post in posts])
    content = f"{generated}\n\nCredits: {credited_accounts}"
    
    return content

if __name__ == "__main__":
    from fetch_data import fetch_posts
    accounts = ["elonmusk", "wsj"]
    posts = fetch_posts(accounts)
    content = generate_content(posts)
    print(content)