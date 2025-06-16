#!/usr/bin/env python3
"""
Simple Veo 3 API Example
Basic example showing how to generate a single video
"""

import os
import replicate
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def main():
    # Check if API token is set
    if not os.getenv('REPLICATE_API_TOKEN'):
        print("❌ Error: REPLICATE_API_TOKEN environment variable not set.")
        print("Please set your Replicate API token:")
        print("export REPLICATE_API_TOKEN='your-token-here'")
        return
    
    # Simple video generation
    prompt = "A majestic eagle soaring over snow-capped mountains at sunrise"
    
    print(f"🎬 Generating video: '{prompt}'")
    print("⏳ Please wait...")
    
    try:
        # Generate the video
        output = replicate.run(
            "google/veo-3",
            input={
                "prompt": prompt,
                "enhance_prompt": True
            }
        )
        
        print("\n✅ Video generated successfully!")
        print(f"🔗 Video URL: {output}")
        print("\n💡 You can now download or share this video!")
        
    except Exception as e:
        print(f"\n❌ Error generating video: {str(e)}")

if __name__ == "__main__":
    main()