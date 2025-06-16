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