#!/usr/bin/env python3
"""
Veo 3 Demo Script
Demonstrates how to use Google's Veo 3 model via Replicate API
"""

import os
import sys
import time
from dotenv import load_dotenv

try:
    import replicate
except ImportError:
    print("Error: replicate package not installed.")
    print("Please run: pip install replicate")
    sys.exit(1)

# Load environment variables
load_dotenv()

def generate_video(prompt, enhance_prompt=True, seed=None):
    """
    Generate a video using Veo 3 model
    
    Args:
        prompt (str): Text description for video generation
        enhance_prompt (bool): Whether to enhance prompt with Gemini
        seed (int, optional): Random seed for reproducible results
    
    Returns:
        str: URL of the generated video
    """
    # Check if API token is set
    if not os.getenv('REPLICATE_API_TOKEN'):
        print("Error: REPLICATE_API_TOKEN environment variable not set.")
        print("Please set your Replicate API token:")
        print("export REPLICATE_API_TOKEN='your-token-here'")
        return None
    
    print(f"🎬 Generating video for prompt: '{prompt}'")
    print(f"📈 Enhanced prompting: {'Enabled' if enhance_prompt else 'Disabled'}")
    if seed:
        print(f"🎲 Using seed: {seed}")
    
    # Prepare input parameters
    input_params = {
        "prompt": prompt,
        "enhance_prompt": enhance_prompt
    }
    
    if seed is not None:
        input_params["seed"] = seed
    
    try:
        print("\n⏳ Starting video generation...")
        start_time = time.time()
        
        # Generate video
        output = replicate.run(
            "google/veo-3",
            input=input_params
        )
        
        end_time = time.time()
        duration = end_time - start_time
        
        print(f"\n✅ Video generated successfully!")
        print(f"⏱️  Generation time: {duration:.1f} seconds")
        print(f"🔗 Video URL: {output}")
        
        return output
        
    except Exception as e:
        print(f"\n❌ Error generating video: {str(e)}")
        return None

def main():
    """
    Main demo function with example prompts
    """
    print("🎥 Google Veo 3 Demo - EEInteractive Video")
    print("=" * 50)
    
    # Example prompts
    example_prompts = [
        {
            "prompt": "gorilla riding a moped through busy italian city",
            "description": "Urban Comedy Scene"
        },
        {
            "prompt": "Close-up shot of melting icicles on a frozen rock wall with cool blue tones, zoomed in maintaining close-up detail of water drips",
            "description": "Nature Macro Shot"
        },
        {
            "prompt": "Cinematic drone shot of mountain landscape at golden hour with dramatic lighting and ambient nature sounds",
            "description": "Cinematic Landscape"
        }
    ]
    
    print("\nAvailable example prompts:")
    for i, example in enumerate(example_prompts, 1):
        print(f"{i}. {example['description']}: {example['prompt'][:60]}...")
    
    print("\nOptions:")
    print("- Enter a number (1-3) to use an example prompt")
    print("- Enter 'custom' to input your own prompt")
    print("- Enter 'quit' to exit")
    
    while True:
        choice = input("\nYour choice: ").strip().lower()
        
        if choice == 'quit':
            print("👋 Goodbye!")
            break
        elif choice in ['1', '2', '3']:
            idx = int(choice) - 1
            selected = example_prompts[idx]
            print(f"\n🎯 Selected: {selected['description']}")
            generate_video(selected['prompt'])
        elif choice == 'custom':
            custom_prompt = input("\nEnter your custom prompt: ").strip()
            if custom_prompt:
                # Ask about enhanced prompting
                enhance = input("Enable prompt enhancement? (y/n) [y]: ").strip().lower()
                enhance_prompt = enhance != 'n'
                
                # Ask about seed
                seed_input = input("Enter seed (optional, press Enter to skip): ").strip()
                seed = int(seed_input) if seed_input.isdigit() else None
                
                generate_video(custom_prompt, enhance_prompt, seed)
            else:
                print("❌ Empty prompt, please try again.")
        else:
            print("❌ Invalid choice, please try again.")

if __name__ == "__main__":
    main()