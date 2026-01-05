# EEInteractive-Video Repository Snapshot

This document contains a complete snapshot of all files in the EEInteractive-Video repository.

**Generated:** 2026-01-05

**Repository:** just-goingviral/EEInteractive-Video

---

## Table of Contents

1. [.env.example](#envexample)
2. [README.md](#readmemd)
3. [app.py](#apppy)
4. [batch_example.py](#batch_examplepy)
5. [requirements.txt](#requirementstxt)
6. [simple_example.py](#simple_examplepy)
7. [veo3_demo.py](#veo3_demopy)

---

## .env.example

**File Path:** `.env.example`

```
# Replicate API Token
# Get your token from: https://replicate.com
REPLICATE_API_TOKEN=your-replicate-api-token-here
```

---

## README.md

**File Path:** `README.md`

```markdown
# EEInteractive Video - Google Veo 3 Showcase

![Veo 3 Banner](https://img.shields.io/badge/Google-Veo%203-4285F4?style=for-the-badge&logo=google&logoColor=white)
![Replicate](https://img.shields.io/badge/Replicate-API-00D4AA?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)

## 🎬 Google Veo 3 - Next-Gen Text-to-Video with Native Audio

This repository showcases **Google's Veo 3**, DeepMind's latest advancement in text-to-video generation, available through the Replicate API. Veo 3 pushes the boundaries of AI-generated multimedia content with native audio generation, enhanced prompt adherence, and stunning cinematic quality.

### 🚀 Key Features

- **🎥 Text to Video Generation**: Create high-fidelity videos directly from natural language prompts
- **🔊 Native Audio Generation**: Automatic ambient noise, sound effects, and dialogue that sync naturally with visuals
- **🗣️ Dialogue & Lip-Sync**: Generate characters speaking your script with accurate lip-synchronization
- **🎮 Game World Creation**: Build immersive video game environments from just a sentence
- **🎯 High Prompt Accuracy**: Grounded in real-world physics with deep prompt comprehension
- **🎬 Cinematic Quality**: Stunning output quality with smooth motion and realistic effects

## 📋 Model Information

- **Model Name**: `google/veo-3`
- **Model Type**: Text-to-Video with Audio
- **Provider**: Google DeepMind via Replicate
- **Output Format**: MP4 video with audio

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- Replicate API token ([Get one here](https://replicate.com))

### Setup

1. Clone this repository:
```bash
git clone https://github.com/just-goingviral/EEInteractive-Video.git
cd EEInteractive-Video
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your Replicate API token:
```bash
export REPLICATE_API_TOKEN="your-api-token-here"
```

Or create a `.env` file:
```
REPLICATE_API_TOKEN=your-api-token-here
```

## 🎯 Usage

### Command Line Demo

```bash
python veo3_demo.py
```

### Web Interface

Start the web server:
```bash
python app.py
```

Then open your browser to `http://localhost:5000`

### Python API

```python
import replicate

# Generate a video
output = replicate.run(
    "google/veo-3",
    input={
        "prompt": "gorilla riding a moped through busy italian city",
        "enhance_prompt": True,
        "seed": 42  # Optional - omit for random generation
    }
)

print(f"Video URL: {output}")
```

## 🎨 Prompting Tips

To get the best results from Veo 3, structure your prompts with these elements:

### Shot Composition
- "Close-up", "Two shot", "Over-the-shoulder", "Wide shot"

### Lens & Focus
- "Macro lens", "Shallow focus", "Wide-angle lens", "Telephoto lens"

### Genre & Style
- "Sci-fi", "Romantic comedy", "Action movie", "Documentary style"

### Camera Motion
- "Zoom shot", "Dolly shot", "Tracking shot", "Pan shot", "Crane shot"

### Example Prompt Structure
```
Close up shot (composition) of melting icicles (subject) on a frozen rock wall (context) 
with cool blue tones (ambiance), zoomed in (camera motion) maintaining close-up detail 
of water drips (action).
```

## 📝 API Reference

### Input Parameters

| Parameter | Type | Description | Required |
|-----------|------|-------------|----------|
| `prompt` | string | Text prompt for video generation | Yes |
| `enhance_prompt` | boolean | Use Gemini to enhance your prompts | No (default: false) |
| `seed` | integer | Random seed for reproducible results | No |

### Output

The model returns a URI string pointing to the generated MP4 video file.

## 🎬 Example Outputs

### Example 1: Urban Scene
**Prompt**: "gorilla riding a moped through busy italian city"

**Output**: [View Example](https://replicate.delivery/xezq/xfz0U06bqSw1AyiJsw7LjOjVXOBpmjJfe7K9XtRLifW26q7SB/tmpi29yh_f0.mp4)

### Example 2: Nature Scene
**Prompt**: "Timelapse of aurora borealis dancing over snowy mountains with ethereal ambient sounds"

### Example 3: Action Sequence
**Prompt**: "Tracking shot following a parkour athlete jumping between rooftops at sunset, dynamic camera movement"

## 🔧 Advanced Usage

### Batch Processing

```python
prompts = [
    "Underwater scene with colorful coral reef and tropical fish",
    "Space battle with starships and laser effects",
    "Medieval castle siege with dramatic lighting"
]

for i, prompt in enumerate(prompts):
    output = replicate.run(
        "google/veo-3",
        input={"prompt": prompt, "enhance_prompt": True}
    )
    print(f"Video {i+1}: {output}")
```

## 🌟 Creative Examples

### Film-style Prompts
```
"Wide establishing shot of a futuristic city skyline at night, neon lights reflecting on wet streets, cyberpunk aesthetic with flying cars, cinematic color grading"
```

### Nature Documentary Style
```
"Close-up macro shot of a butterfly landing on a flower, shallow depth of field, natural lighting, wildlife documentary style with ambient forest sounds"
```

### Action Sequence
```
"High-speed tracking shot following a motorcycle chase through narrow alleyways, dynamic camera movement, intense action sequence with engine sounds and tire screeches"
```

## 🤝 Contributing

We welcome contributions! Please feel free to submit pull requests.

## 📄 License

This project is licensed under the MIT License.

## 🔗 Links

- [Replicate Veo 3 Model](https://replicate.com/google/veo-3)
- [Google DeepMind](https://deepmind.google/)
- [Replicate Documentation](https://replicate.com/docs)

## ⚠️ Important Notes

- Video generation can take several minutes depending on complexity
- Generated videos are hosted on Replicate's servers
- API usage is subject to Replicate's pricing
- Content policies apply to generated videos

---

**Built with ❤️ for the AI video generation community**
```

---

## app.py

**File Path:** `app.py`

```python
#!/usr/bin/env python3
"""
Veo 3 Web Interface
Simple Flask web application for generating videos with Veo 3
"""

import os
import sys
import json
from flask import Flask, render_template_string, request, jsonify
from dotenv import load_dotenv

try:
    import replicate
except ImportError:
    print("Error: replicate package not installed.")
    print("Please run: pip install replicate")
    sys.exit(1)

# Load environment variables
load_dotenv()

app = Flask(__name__)

# HTML template for the web interface
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EEInteractive Video - Veo 3 Generator</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh; display: flex; align-items: center; justify-content: center;
        }
        .container {
            background: white; border-radius: 15px; box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            padding: 2rem; max-width: 600px; width: 90%;
        }
        .header { text-align: center; margin-bottom: 2rem; }
        .header h1 { color: #333; margin-bottom: 0.5rem; }
        .header p { color: #666; font-size: 1.1rem; }
        .form-group { margin-bottom: 1.5rem; }
        label { display: block; margin-bottom: 0.5rem; font-weight: 600; color: #333; }
        textarea, input[type="number"] {
            width: 100%; padding: 12px; border: 2px solid #e1e5e9; border-radius: 8px;
            font-size: 16px; transition: border-color 0.3s;
        }
        textarea:focus, input[type="number"]:focus { outline: none; border-color: #667eea; }
        textarea { resize: vertical; min-height: 100px; }
        .checkbox-group { display: flex; align-items: center; gap: 0.5rem; }
        input[type="checkbox"] { width: 18px; height: 18px; }
        .generate-btn {
            width: 100%; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white; border: none; padding: 15px; border-radius: 8px;
            font-size: 18px; font-weight: 600; cursor: pointer; transition: transform 0.2s;
        }
        .generate-btn:hover { transform: translateY(-2px); }
        .generate-btn:disabled { opacity: 0.6; cursor: not-allowed; transform: none; }
        .result { margin-top: 2rem; padding: 1rem; border-radius: 8px; display: none; }
        .result.success { background: #d4edda; border: 1px solid #c3e6cb; color: #155724; }
        .result.error { background: #f8d7da; border: 1px solid #f5c6cb; color: #721c24; }
        .loading { text-align: center; padding: 2rem; display: none; }
        .spinner {
            border: 4px solid #f3f3f3; border-top: 4px solid #667eea; border-radius: 50%;
            width: 40px; height: 40px; animation: spin 1s linear infinite; margin: 0 auto 1rem;
        }
        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
        .examples { margin-top: 1rem; padding: 1rem; background: #f8f9fa; border-radius: 8px; }
        .examples h3 { color: #333; margin-bottom: 0.5rem; }
        .example-btn {
            background: #e9ecef; border: 1px solid #ced4da; padding: 0.5rem 1rem;
            margin: 0.25rem; border-radius: 4px; cursor: pointer; font-size: 14px;
            transition: background-color 0.2s;
        }
        .example-btn:hover { background: #dee2e6; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🎬 EEInteractive Video</h1>
            <p>Generate videos with Google's Veo 3</p>
        </div>
        
        <form id="videoForm">
            <div class="form-group">
                <label for="prompt">Video Prompt:</label>
                <textarea id="prompt" name="prompt" placeholder="Describe the video you want to generate..." required></textarea>
            </div>
            
            <div class="form-group">
                <div class="checkbox-group">
                    <input type="checkbox" id="enhance_prompt" name="enhance_prompt" checked>
                    <label for="enhance_prompt">Enhance prompt with Gemini</label>
                </div>
            </div>
            
            <div class="form-group">
                <label for="seed">Seed (optional):</label>
                <input type="number" id="seed" name="seed" placeholder="Leave empty for random generation">
            </div>
            
            <button type="submit" class="generate-btn" id="generateBtn">
                🎥 Generate Video
            </button>
        </form>
        
        <div class="loading" id="loading">
            <div class="spinner"></div>
            <p>Generating your video... This may take a few minutes.</p>
        </div>
        
        <div class="result" id="result">
            <div id="resultContent"></div>
        </div>
        
        <div class="examples">
            <h3>💡 Example Prompts:</h3>
            <div>
                <button type="button" class="example-btn" onclick="setPrompt('gorilla riding a moped through busy italian city')">Urban Comedy</button>
                <button type="button" class="example-btn" onclick="setPrompt('Close-up shot of melting icicles on frozen rock wall with cool blue tones')">Nature Macro</button>
                <button type="button" class="example-btn" onclick="setPrompt('Cinematic drone shot of mountain landscape at golden hour')">Cinematic</button>
                <button type="button" class="example-btn" onclick="setPrompt('Underwater coral reef with tropical fish swimming')">Ocean Life</button>
            </div>
        </div>
    </div>
    
    <script>
        function setPrompt(text) {
            document.getElementById('prompt').value = text;
        }
        
        document.getElementById('videoForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const formData = new FormData(e.target);
            const data = {
                prompt: formData.get('prompt'),
                enhance_prompt: formData.get('enhance_prompt') === 'on',
                seed: formData.get('seed') ? parseInt(formData.get('seed')) : null
            };
            
            // Show loading, hide result
            document.getElementById('loading').style.display = 'block';
            document.getElementById('result').style.display = 'none';
            document.getElementById('generateBtn').disabled = true;
            
            try {
                const response = await fetch('/generate', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(data)
                });
                
                const result = await response.json();
                
                // Hide loading
                document.getElementById('loading').style.display = 'none';
                document.getElementById('generateBtn').disabled = false;
                
                const resultDiv = document.getElementById('result');
                const resultContent = document.getElementById('resultContent');
                
                if (response.ok && result.video_url) {
                    resultDiv.className = 'result success';
                    resultContent.innerHTML = `
                        <h3>✅ Video Generated Successfully!</h3>
                        <video controls style="width: 100%; margin-top: 1rem; border-radius: 8px;">
                            <source src="${result.video_url}" type="video/mp4">
                            Your browser does not support the video tag.
                        </video>
                        <p style="margin-top: 1rem;"><strong>Video URL:</strong> <a href="${result.video_url}" target="_blank">${result.video_url}</a></p>
                        <p><strong>Generation Time:</strong> ${result.generation_time || 'N/A'} seconds</p>
                    `;
                } else {
                    resultDiv.className = 'result error';
                    resultContent.innerHTML = `
                        <h3>❌ Generation Failed</h3>
                        <p>${result.error || 'Unknown error occurred'}</p>
                    `;
                }
                
                resultDiv.style.display = 'block';
                
            } catch (error) {
                document.getElementById('loading').style.display = 'none';
                document.getElementById('generateBtn').disabled = false;
                
                const resultDiv = document.getElementById('result');
                const resultContent = document.getElementById('resultContent');
                
                resultDiv.className = 'result error';
                resultContent.innerHTML = `
                    <h3>❌ Network Error</h3>
                    <p>Failed to connect to server: ${error.message}</p>
                `;
                resultDiv.style.display = 'block';
            }
        });
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    """Main page with video generation form"""
    return render_template_string(HTML_TEMPLATE)

@app.route('/generate', methods=['POST'])
def generate_video():
    """API endpoint to generate video"""
    # Check if API token is set
    if not os.getenv('REPLICATE_API_TOKEN'):
        return jsonify({
            'error': 'REPLICATE_API_TOKEN not configured',
            'message': 'Please set your Replicate API token in environment variables'
        }), 500
    
    try:
        data = request.get_json()
        prompt = data.get('prompt', '').strip()
        enhance_prompt = data.get('enhance_prompt', True)
        seed = data.get('seed')
        
        if not prompt:
            return jsonify({'error': 'Prompt is required'}), 400
        
        # Prepare input parameters
        input_params = {
            "prompt": prompt,
            "enhance_prompt": enhance_prompt
        }
        
        if seed is not None:
            input_params["seed"] = seed
        
        print(f"Generating video with prompt: {prompt}")
        
        # Generate video using Replicate
        import time
        start_time = time.time()
        
        output = replicate.run(
            "google/veo-3",
            input=input_params
        )
        
        end_time = time.time()
        generation_time = round(end_time - start_time, 1)
        
        return jsonify({
            'success': True,
            'video_url': output,
            'generation_time': generation_time,
            'prompt': prompt,
            'enhanced': enhance_prompt
        })
        
    except Exception as e:
        print(f"Error generating video: {str(e)}")
        return jsonify({
            'error': str(e),
            'message': 'Failed to generate video'
        }), 500

if __name__ == '__main__':
    print("🎬 Starting EEInteractive Video - Veo 3 Web Interface")
    print("📋 Make sure to set REPLICATE_API_TOKEN environment variable")
    print("🌐 Server will start at http://localhost:5000")
    
    # Check if API token is set
    if not os.getenv('REPLICATE_API_TOKEN'):
        print("⚠️  WARNING: REPLICATE_API_TOKEN not set!")
        print("   Set it with: export REPLICATE_API_TOKEN='your-token-here'")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
```

---

## batch_example.py

**File Path:** `batch_example.py`

```python
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
```

---

## requirements.txt

**File Path:** `requirements.txt`

```
replicate>=0.15.0
flask>=2.3.0
python-dotenv>=1.0.0
requests>=2.31.0
```

---

## simple_example.py

**File Path:** `simple_example.py`

```python
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
```

---

## veo3_demo.py

**File Path:** `veo3_demo.py`

```python
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
```

---

## Repository Structure

```
EEInteractive-Video/
├── .env.example          # Environment configuration template
├── README.md             # Project documentation
├── app.py                # Flask web interface for video generation
├── batch_example.py      # Batch processing script for multiple videos
├── requirements.txt      # Python dependencies
├── simple_example.py     # Simple single video generation example
└── veo3_demo.py          # Interactive demo with example prompts
```

---

## Summary

This repository contains a complete implementation for generating videos using Google's Veo 3 model via the Replicate API. It includes:

- **Web Interface** (app.py): A Flask-based web application with a user-friendly interface
- **Command Line Tools**: Multiple Python scripts for different use cases
- **Batch Processing**: Support for generating multiple videos sequentially
- **Comprehensive Documentation**: Detailed README with setup instructions and examples

All files are Python-based with dependencies managed through requirements.txt. The project uses the Replicate API to access Google's Veo 3 text-to-video generation model.

---

**End of Repository Snapshot**
