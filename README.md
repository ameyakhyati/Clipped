# Clipped - Process Documentation

## Overview
This document outlines the step-by-step process of building a **Clipped** - _a text summarizer_ , including challenges faced, troubleshooting steps, and key learnings.

## Initial Approach: Fine-Tuning a Large Language Model

- Chose the **`facebook/bart-large-cnn`** model for its strong summarization capabilities.
- Downloaded the pre-trained model and set up a **fine-tuning pipeline** using **Hugging Face Transformers**.
- Attempted to train on a **CPU-only** machine. Training was extremely slow — one epoch was estimated to take over **50 days**.
- Reduced **batch size** and **sequence length** to improve performance, but training was still impractical.

### Issues Encountered

- **RuntimeError:** `The size of tensor a (512) must match the size of tensor b (1024)`  
- Caused by a shape mismatch between input tensors and model expectations.  
- Fixed by padding/truncating input data to the correct sequence length.
<br/>

- **ValueError:** `too many values to unpack (expected 2)`  
- Occurred when loading the dataset.  
- Fixed by correcting the data loader’s unpacking logic.
<br/>

- **ModuleNotFoundError:** for the `transformers` library  
- Installed using `pip install transformers`.  
- Also installed `torch` separately to resolve version compatibility issues.

## Shift to Extractive Summarization (Sumy)

- Realized fine-tuning was not feasible on CPU due to time and resource limitations.
- Switched to a **lighter extractive summarization approach** using the `sumy` library.

### What is Sumy?
> **Sumy** is a Python library for **extractive text summarization**.  
> It uses statistical and linguistic algorithms (like LSA, LexRank, and Luhn) to identify and extract the most important sentences from text.  
> Unlike deep learning models, it does **not** require training or GPUs.

### Issues Encountered

- **DeprecationWarning:** due to a `numpy` version mismatch.  
- Checked compatibility online and installed a supported version manually to avoid dependency conflicts.
<br/>

- Successfully generated summaries, but recognized that **Sumy is not a deep learning-based model**.

## Exploring Lightweight Neural Models

- Wanted a **deep learning-based summarizer** that could still run efficiently.  
- Found **`sshleifer/distilbart-cnn-12-6`**, a distilled version of BART optimized for speed.

### Controlling Summary Length

- Realized most models do not guarantee summaries within a fixed number of lines.  
- Used Python’s **`re`** (Regular Expressions) module to **manually limit** summary length.

### Issues Encountered 

- After using the **`re`** module, noticed that the generated output often repeated the **first few lines** of the input text. 
- Noticed that my summary was being generated where **`do_sample = False`**.To introduce more randomness and diversity in the output, I changed the parameter to **`do_sample = Treu`**
<br/>

- To address this, tried **returning the raw summary** directly, but encountered **formatting issues**.  
- Asked **ChatGPT** for help to format the output cleanly and improve readability.

## Building a Web Application with Flask

- Decided to implement the summarizer as a **web app** using **Flask**, served as a learning opportunity.  
- Watched YouTube tutorials to understand the Flask setup and routing process.

### Issues Encountered

- **ModuleNotFoundError:** Flask was not installed locally.  
- Installed using `pip install flask`.
<br/>

- **TemplateNotFound:** even though a template folder existed.  
- Realized the folder was mistakenly named **`template`** instead of **`templates`**.  
- Renamed it and created the required **`index.html`** file inside it.
<br/>

- **Port Already in Use:** Flask server failed to start due to port conflict.  
- Looked up the issue and identified another application using the same port.  
- Resolved by running Flask on a different port.
<br/>

- **Slow Loading Issue:** The web app took significant time to generate the summary.  
- As a user, it was unclear whether the summary was loading or the app had frozen.  
- Added a small **JavaScript loader script** in the HTML file to indicate that the summary was being generated until the output rendered.
<br/>

- **Frontend Styling:** Improved the appearance by adjusting the **CSS** formatting and layout for a better user experience.

## Usage Instructions

To set up and run the text summarizer web app locally:

- Clone the repository to your local host
``` bash
  git clone https://github.com/ameyakhyati/Clipped.git
  cd Clipped
```
<br/>

- Install the required dependencies using the following command
``` bash
  pip install -r requirements.txt
```
<br/>

- Run the flask web app 
``` bash
  python app.py
```
<br/>

- Navigate to the provided URL to access the web app 
``` bash
  http://127.0.0.1:5000
```
<br/>

#### Note : Flask runs the web app on port 5000 by default, but you can change it to any available port if needed. To do so, please add the port parameter in app.py 
``` bash
  app.run(debug=True, port={port number})
```

## Documentation & Learnings

- Maintained a detailed **README** with all dependencies, installation steps, and commands.  
- Key takeaways:
  - Be flexible and resourceful.  
  - Search and verify solutions online.  
  - Consult ChatGPT, Stack Overflow, and official documentation.  
  - Adapt approach based on hardware and time constraints.

## Final Status

- Abstractive summarizer - Functional, but length control limited  
- Learned valuable debugging, dependency management, and optimization skills
