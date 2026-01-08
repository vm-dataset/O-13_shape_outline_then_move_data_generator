# Shape Outline-Then-Move Task Generator

A specialized data generator for creating **two-step sequential visual reasoning tasks** where shapes undergo fill-to-outline transformation followed by vertical movement.

## 🎯 Task Format

This generator creates visual analogies in the **A→B→C :: D→?→?** format:

- **Example Sequence (A→B→C)**: Shows the complete two-step transformation
  - **A**: Original shape (e.g., filled circle at center position)
  - **B**: After step 1 - fill-to-outline (e.g., outline circle at center position)  
  - **C**: After step 2 - vertical movement (e.g., outline circle moved up)

- **Question Sequence (D→?→?)**: User must solve both steps
  - **D**: Original shape (e.g., filled square at center position)
  - **First ?**: Apply step 1 - fill-to-outline (e.g., outline square at center position)
  - **Second ?**: Apply step 2 - vertical movement (e.g., outline square moved up)

## 🌟 Key Features

### Sequential Two-Step Transformations
- **Step 1**: Fill-to-outline transformation (filled → outline-only)
- **Step 2**: Vertical movement (up/down by specified distances)
- **Consistent Pattern**: Both example and question follow identical transformation sequence

### Enhanced Visual Design
- **Optimized Layout**: 800×400 image format for better horizontal spacing
- **Improved Spacing**: 80% space for shapes, 20% for arrows to prevent overlap
- **Clear Separation**: Proper margins between all visual elements
- **Single Color Focus**: Blue color for all shapes to emphasize style and position changes

### Rich Animation
- **Two-Step Video**: Shows sequential revelation of both question marks
- **Step 1 Animation**: First ? gradually converts from filled to outline (25 frames)
- **Step 2 Animation**: Second ? gradually moves vertically (25 frames)
- **Smooth Transitions**: Clear visual progression through transformation steps

## 🎨 Visual Elements

### Shapes
- **10 Shape Types**: square, triangle, circle, diamond, pentagon, hexagon, rectangle, oval, star, heart
- **Consistent Style**: All shapes use blue color with black outlines

### Fill Styles
- **Filled**: Full color fill with thin border (width=2)
- **Outline**: No fill, thicker border (width=3) for clear distinction

### Movement Options
- **6 Movement Types**: 
  - `up` (60px up), `down` (60px down)
  - `up_small` (40px up), `down_small` (40px down)  
  - `up_large` (80px up), `down_large` (80px down)
- **Clear Displacement**: Easily distinguishable vertical position changes

## 🚀 Quick Start

### Installation
```bash
pip install -e .
```

### Generate Tasks
```bash
python examples/generate.py --num-samples 10 --output data/my_tasks
```

### Configuration
Edit `src/config.py` to customize:
- Image dimensions (default: 800×400)
- Shape sizes and margins
- Video frame rates
- Output settings

## 📁 Output Structure

Each generated task includes:
```
task_id/
├── prompt.txt           # Task instruction
└── ground_truth.mp4     # Animated solution showing both steps
```

## 🎬 Video Animation Sequence

1. **Initial State**: Shows A→B→C :: D→?→? layout
2. **Step 1 Animation**: First ? reveals with fill-to-outline transformation
3. **Step 2 Animation**: Second ? reveals with vertical movement  
4. **Final State**: Complete sequence A→B→C :: D→E→F

## 🔧 Customization

### Adding New Movement Patterns
Modify `movements` in `src/generator.py`:
```python
self.movements = {
    "up": -60,          # Move up by 60 pixels
    "down": 60,         # Move down by 60 pixels
    "up_small": -40,    # Move up by 40 pixels
    # Add your movements...
}
```

### Adjusting Movement Distances
Update movement pixel values:
```python
self.valid_transformations = [
    ("filled", "outline", "center", "up"),      # Fill-to-outline + move up
    ("filled", "outline", "center", "down"),    # Fill-to-outline + move down
    # Add your combinations...
]
```

## 🧠 Cognitive Challenge

This task type tests:
- **Sequential Reasoning**: Understanding multi-step transformation patterns
- **Style Recognition**: Distinguishing filled vs outline-only shapes
- **Spatial Awareness**: Recognizing vertical movement patterns and distances
- **Analogical Thinking**: Applying learned patterns to new shapes

## 📊 Task Complexity

- **Transformation Steps**: 2 (fill-to-outline then vertical movement)
- **Shape Variations**: 10 different shapes
- **Movement Options**: 6 different vertical movements
- **Style Transformation**: Always filled → outline
- **Total Unique Tasks**: 10 × 10 × 6 = 600 possible combinations

## 🎯 Use Cases

- **Visual Reasoning Research**: Multi-step transformation understanding
- **AI Training Data**: Sequential pattern recognition tasks
- **Cognitive Assessment**: Two-step analogical reasoning evaluation
- **Educational Tools**: Teaching sequential logical thinking with spatial elements

## 🔍 Example Task

**Visual Layout:**
```
filled_circle → outline_circle → outline_circle_moved_up
filled_square →       ?        →           ?
```

**Solution:**
- First ?: outline_square (apply fill-to-outline change)
- Second ?: outline_square_moved_up (apply same vertical movement)

**Reasoning:** The pattern shows style change first (filled→outline), then position change (center→up). Apply the same sequence to the square.

## 🎨 Visual Transformation Details

### Step 1: Fill-to-Outline Transformation
- **Phase 1**: Gradual fill opacity reduction (first 12 frames)
- **Phase 2**: Complete fill removal, outline emphasis (remaining 13 frames)
- **Border Enhancement**: Outline width increases from 2px to 3px
- **Visual Clarity**: Clear distinction between filled and outline states

### Step 2: Vertical Movement
- **Small Movement**: ±40 pixels (subtle but noticeable displacement)
- **Medium Movement**: ±60 pixels (clear positional change)
- **Large Movement**: ±80 pixels (dramatic positional shift)
- **Smooth Animation**: Gradual position interpolation over 25 frames
- **Direction Consistency**: Up movements are negative Y, down movements are positive Y

## 🔬 Research Applications

- **Spatial Cognition**: Understanding how humans process position changes
- **Sequential Processing**: Investigating multi-step visual reasoning
- **AI Pattern Recognition**: Training models on style and spatial transformations
- **Educational Assessment**: Measuring analogical reasoning with spatial elements
- **Perceptual Studies**: Investigating style change and movement detection

## 💡 Design Philosophy

This generator focuses on **intuitive transformations** that are:
- **Easy to Understand**: Fill-to-outline is a clear visual change
- **Spatially Clear**: Vertical movement is unambiguous
- **Cognitively Engaging**: Requires attention to both style and position
- **Visually Distinct**: Large enough movements to be easily perceived

## 🎓 Educational Value

Perfect for teaching:
- **Sequential Thinking**: Step-by-step problem solving
- **Pattern Recognition**: Identifying consistent transformation rules
- **Spatial Reasoning**: Understanding position and movement
- **Visual Analysis**: Distinguishing style and spatial changes

---

Built with the Template Data Generator framework for creating high-quality visual reasoning datasets.