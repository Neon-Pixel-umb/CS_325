from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch
import time  

# Set a random seed for more randomness
torch.manual_seed(int(time.time()))  # Use the current time as a seed

# Load the gpt2 model from Hugging Face
model_name = "gpt2"

# Load the model
print("Loading model...")
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="cpu", 
    torch_dtype="auto"
)


tokenizer = AutoTokenizer.from_pretrained(model_name)


pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
)

# Function to read prompts from a text file
def read_prompts(file_path):
    print(f"Reading prompts from {file_path}...")
    with open(file_path, 'r') as file:
        prompts = file.readlines()
    return [prompt.strip() for prompt in prompts if prompt.strip()]  # Remove empty prompts

# Function to generate responses for each prompt
def generate_response(prompt, pipe, generation_args):
    print(f"Generating response for: {prompt}")  #print the prompt
    try:
        output = pipe(prompt, **generation_args)
        response = output[0]['generated_text'].strip()  # Trim whitespace
        print(f"Generated response: {response}")  #print the generated response
        return response
    except Exception as e:
        print(f"Error generating response: {e}")
        return "Error in generation"

# Function to write the prompts and responses to a file
def write_responses(prompts, responses, file_path):
    print(f"Writing prompts and responses to {file_path}...")
    with open(file_path, 'w') as file:
        for prompt, response in zip(prompts, responses):
            file.write(f"Q: {prompt}\nA: {response}\n\n")  # Include both question and response

# Main function
def main():
    print("Starting the program...")

    # Read the prompts from a file
    prompts = read_prompts("prompts.txt")
    print(f"Prompts read: {prompts}")

    # Define the generation parameters
    generation_args = {
        "max_new_tokens": 50,  # Limit token length to 50 tokens
        "return_full_text": False,
        "temperature": 0.7,  # Keep randomness moderate for more coherent responses
        "do_sample": True,  # Enable sampling for diverse responses
        "top_k": 30,  # Consider top 30 tokens to avoid extreme randomness
        "top_p": 0.85,  # Apply nucleus sampling to limit repetition
        "repetition_penalty": 1.2,  # Penalize repetition to avoid looping responses
    }

    # Generate responses for each prompt
    print("Generating responses...")
    responses = []
    for prompt in prompts:
        response = generate_response(prompt, pipe, generation_args)
        responses.append(response)

    # Write the prompts and responses to a file
    write_responses(prompts, responses, "responses.txt")
    print("Responses saved to responses.txt")

if __name__ == "__main__":
    main()
