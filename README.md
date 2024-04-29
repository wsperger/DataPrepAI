# DataPrepAI

## Overview
DataPrepAI is an open-source Docker-based solution designed to simplify the data preparation process for generative AI models. It supports various data types, including text, images, and videos, facilitating tasks such as cleaning, labeling, and structuring data. With the capability for both local and cloud-based operations, DataPrepAI is ideal for developers looking to prepare data for AI models like LLMs, StyleGAN3, and video-based training algorithms.

## Features
- **Local and Cloud Compatibility**: Run on your local machine for development or integrate with Azure Blob Storage for a real-time, cloud-based pipeline.
- **Multi-Data Support**: Handles text, image, and video data, providing tools for effective preprocessing and labeling.
- **Real-Time Data Handling**: Monitors cloud storage for new files and processes them automatically, flagging them as ready for model training.
- **Scalable Architecture**: Designed to scale with your project needs, from simple data cleaning tasks to comprehensive data structuring for advanced AI models.

## Getting Started

### Prerequisites
- Docker
- Docker Compose
- Access to Azure Blob Storage (for cloud functionality)

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/DataPrepAI.git
   cd DataPrepAI
   ```

2. Build the Docker images:
   ```bash
   docker-compose build
   ```

3. Launch the containers:
   - For local deployment:
     ```bash
     docker-compose up
     ```
   - For cloud deployment:
     ```bash
     docker-compose -f docker-compose.cloud.yml up
     ```

## Usage
- **Local Development**: Navigate to http://localhost:5000 to access the web interface for managing and processing data.
- **Cloud Deployment**: Files added to the specified Azure Blob Storage container are automatically processed according to the defined workflows.

## Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.
1. Fork the Project
2. Create your Feature Branch (git checkout -b feature/AmazingFeature)
3. Commit your Changes (git commit -m 'Add some AmazingFeature')
4. Push to the Branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

## License
Distributed under the MIT License. See LICENSE for more information.

## Contact
Your Name - your-email@example.com
GitHub: https://github.com/yourusername