# GPT-2 Response Generator

This is a simple application built using the GPT-2 model to generate AI responses to prompts. The model is designed to mimic human speech but may produce offensive or inappropriate responses.

## Features
- Uses the GPT-2 model to generate responses to input prompts.
- Supports controlled generation parameters to avoid repetition and increase response diversity.
- Provides both the prompt and generated response in an output file.

## Installation

Follow the steps below to set up and run the project locally:

### Step 1: Clone the Repository
Clone this GitHub repository to your local machine using the following command:

```bash
git clone <https://github.com/Neon-Pixel-umb/Project-1.git>


Step 2: Set Up the Environment
The required dependencies are listed in the environment.yml file. You can create a virtual environment using Conda and install the dependencies as follows:

conda env create -f environment.yml

This will create a Conda environment with all necessary dependencies installed.

Step 3: Activate the Environment
Once the environment is created, activate it:


conda activate <your-environment-name>


Step 4: Run the Script
Make sure to provide a prompts.txt file containing the prompts you'd like to generate responses for, with each prompt on a new line. Then, run the script:

python main.py


The generated responses will be saved to responses.txt.

Warning:
This model was designed to mimic human speech, so offensive or inappropriate responses may occur. Use it with caution.
