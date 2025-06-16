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