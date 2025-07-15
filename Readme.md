# Flask Performance Monitoring App

A lightweight Flask application with performance monitoring endpoints, designed for testing and benchmarking purposes.

## Features

- **Health Check**: Basic health monitoring endpoint
- **Ping Test**: Network latency measurement
- **CPU Benchmark**: Fibonacci calculation for CPU performance testing
- **Startup Time**: Application startup duration tracking
- **CORS Support**: Cross-origin request handling enabled

## API Endpoints

### `GET /`
Returns welcome message and available endpoints.

**Response:**
```json
{
  "message": "Welcome to the Flask App",
  "endpoints": ["/ping", "/fib", "/health", "/startup"]
}
```

### `GET /ping`
Measures response time for basic connectivity testing.

**Response:**
```json
{
  "delay": 0.0001,
  "status": "ok"
}
```

### `GET /fib`
Performs CPU-intensive Fibonacci calculation (n=30) for performance testing.

**Response:**
```json
{
  "n": 30,
  "result": 832040,
  "duration": 0.0002,
  "status": "completed"
}
```

### `GET /health`
Basic health check endpoint.

**Response:**
```json
{
  "status": "healthy"
}
```

### `GET /startup`
Returns application startup time in seconds.

**Response:**
```json
{
  "startup_time": 0.1234567890
}
```

## Installation & Setup

### Local Development

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd flask-performance-app
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```

The application will be available at `http://localhost:5000`

### Docker Deployment

1. **Build the Docker image:**
   ```bash
   docker build -t flask-performance-app .
   ```

2. **Run the container:**
   ```bash
   docker run -p 5000:5000 flask-performance-app
   ```

3. **Run with custom port:**
   ```bash
   docker run -p 8080:8080 -e PORT=8080 flask-performance-app
   ```

## Dependencies

- **Flask 2.3.3**: Web framework
- **flask-cors 4.0.0**: Cross-origin resource sharing support

## Configuration

The application uses the following environment variables:

- `PORT`: Server port (default: 5000)

## File Structure

```
.
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── Dockerfile         # Docker configuration
└── README.md          # This file
```

## Usage Examples

### Testing with curl

```bash
# Health check
curl http://localhost:5000/health

# Performance test
curl http://localhost:5000/fib

# Ping test
curl http://localhost:5000/ping

# Startup time
curl http://localhost:5000/startup
```

### Using in Load Testing

This application is ideal for:
- Load testing with tools like Apache Bench, wrk, or Locust
- Container performance benchmarking
- Network latency measurements
- CPU performance testing

## Performance Notes

- The `/fib` endpoint calculates the 30th Fibonacci number, which provides a consistent CPU workload
- Response times are measured in seconds with 4 decimal places precision
- Startup time is tracked from application initialization

## Docker Image Details

- **Base Image**: python:3.10-slim
- **Working Directory**: /app
- **Exposed Port**: 5000
- **Build Dependencies**: build-essential (removed after installation)

## License

This project is open source and available under the MIT License.