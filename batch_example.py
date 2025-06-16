#!/usr/bin/env python3
"""
Veo 3 Batch Processing Example
Demonstrates batch video generation with multiple prompts
"""

import os
import json
import time
from datetime import datetime
import replicate
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def batch_generate_videos(prompts, output_file="batch_results.json"):
    """
    Generate multiple videos from a list of prompts
    
    Args:
        prompts (list): List of prompt dictionaries
        output_file (str): File to save results
    
    Returns:
        list: Results with video URLs and metadata
    """
    # Check if API token is set
    if not os.getenv('REPLICATE_API_TOKEN'):
        print("❌ Error: REPLICATE_API_TOKEN environment variable not set.")
        return []
    
    results = []
    total_prompts = len(prompts)
    
    print(f"🎬 Starting batch generation of {total_prompts} videos")
    print("=" * 60)
    
    for i, prompt_data in enumerate(prompts, 1):
        prompt = prompt_data.get('prompt', '')
        name = prompt_data.get('name', f'Video_{i}')
        enhance = prompt_data.get('enhance_prompt', True)
        seed = prompt_data.get('seed')
        
        print(f"\n[{i}/{total_prompts}] Generating: {name}")
        print(f"Prompt: {prompt[:80]}{'...' if len(prompt) > 80 else ''}")
        
        try:
            start_time = time.time()
            
            # Prepare input parameters
            input_params = {
                "prompt": prompt,
                "enhance_prompt": enhance
            }
            
            if seed is not None:
                input_params["seed"] = seed
            
            # Generate video
            output = replicate.run(
                "google/veo-3",
                input=input_params
            )
            
            end_time = time.time()
            generation_time = round(end_time - start_time, 1)
            
            result = {
                "name": name,
                "prompt": prompt,
                "video_url": output,
                "generation_time": generation_time,
                "enhanced": enhance,
                "seed": seed,
                "status": "success",
                "timestamp": datetime.now().isoformat()
            }
            
            results.append(result)
            
            print(f"✅ Success! Generated in {generation_time}s")
            print(f"🔗 URL: {output}")
            
        except Exception as e:
            error_result = {
                "name": name,
                "prompt": prompt,
                "video_url": None,
                "generation_time": None,
                "enhanced": enhance,
                "seed": seed,
                "status": "error",
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }
            
            results.append(error_result)
            print(f"❌ Error: {str(e)}")
        
        # Small delay between requests
        if i < total_prompts:
            print("⏳ Waiting 2 seconds before next generation...")
            time.sleep(2)
    
    # Save results to file
    try:
        with open(output_file, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"\n💾 Results saved to {output_file}")
    except Exception as e:
        print(f"\n⚠️  Could not save results: {str(e)}")
    
    # Print summary
    successful = sum(1 for r in results if r['status'] == 'success')
    failed = total_prompts - successful
    
    print("\n" + "=" * 60)
    print(f"📊 BATCH GENERATION SUMMARY")
    print(f"Total prompts: {total_prompts}")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Success rate: {(successful/total_prompts)*100:.1f}%")
    
    return results

def main():
    # Example prompts for batch processing
    example_prompts = [
        {
            "name": "Nature_Documentary",
            "prompt": "Close-up macro shot of a butterfly landing on a colorful flower, shallow depth of field, natural lighting, wildlife documentary style",
            "enhance_prompt": True
        },
        {
            "name": "Urban_Scene",
            "prompt": "Time-lapse of busy city intersection at night with light trails from cars, urban photography style",
            "enhance_prompt": True
        },
        {
            "name": "Ocean_Life",
            "prompt": "Underwater scene with sea turtles swimming through coral reef, crystal clear water, marine life documentary",
            "enhance_prompt": True
        },
        {
            "name": "Space_Scene",
            "prompt": "Cinematic shot of Earth from space with aurora borealis visible, cosmic vista with stars",
            "enhance_prompt": True,
            "seed": 42
        }
    ]
    
    print("🎥 Veo 3 Batch Processing Demo")
    print("This will generate multiple videos sequentially")
    
    # Ask user for confirmation
    response = input("\nProceed with batch generation? (y/n): ").strip().lower()
    if response != 'y':
        print("👋 Batch generation cancelled.")
        return
    
    # Start batch processing
    results = batch_generate_videos(example_prompts)
    
    # Display results
    print("\n📹 Generated Videos:")
    for result in results:
        if result['status'] == 'success':
            print(f"✅ {result['name']}: {result['video_url']}")
        else:
            print(f"❌ {result['name']}: {result['error']}")

if __name__ == "__main__":
    main()