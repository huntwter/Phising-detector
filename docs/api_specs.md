# API Specifications

## Endpoints

### Scanning
- `POST /api/v1/scan`: Submit a URL for analysis.
  - **Body**: `{ "url": "https://example.com", "scan_type": "deep" }`
  - **Response**: `{ "job_id": "uuid", "status": "pending" }`

### Feedback
- `POST /api/v1/feedback`: Report false positives/negatives.

### Health
- `GET /health`: System status check.
