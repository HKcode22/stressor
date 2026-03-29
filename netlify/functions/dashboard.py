import json
from pathlib import Path

def handler(event, context):
    """Netlify function handler for dashboard API."""
    
    # CORS headers
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Content-Type': 'application/json'
    }
    
    # Handle CORS preflight
    if event['httpMethod'] == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': headers,
            'body': ''
        }
    
    try:
        path = event.get('path', '').split('/')[-1]
        
        if path == 'health':
            response = {
                "status": "healthy",
                "timestamp": "2024-01-01T00:00:00Z",
                "version": "1.0.0"
            }
        
        elif path == 'stats':
            response = {
                "total_tests": 1247,
                "success_rate": 94.2,
                "vulnerabilities_found": 23,
                "average_latency": 1.2,
                "models_tested": ["gpt-4", "claude-3", "gpt-3.5-turbo"],
                "last_run": "2024-01-01T12:00:00Z"
            }
        
        elif path == 'test-runs':
            response = [
                {
                    "id": "run_001",
                    "name": "Adversarial Input Testing",
                    "status": "completed",
                    "created_at": "2024-01-01T10:00:00Z",
                    "total_cases": 156,
                    "success_rate": 96.8,
                    "average_latency": 1.1,
                    "model": "gpt-4"
                },
                {
                    "id": "run_002", 
                    "name": "Prompt Injection Analysis",
                    "status": "completed",
                    "created_at": "2024-01-01T08:00:00Z",
                    "total_cases": 89,
                    "success_rate": 91.2,
                    "average_latency": 1.3,
                    "model": "claude-3"
                },
                {
                    "id": "run_003",
                    "name": "Edge Case Stress Test",
                    "status": "failed",
                    "created_at": "2024-01-01T06:00:00Z",
                    "total_cases": 234,
                    "success_rate": 78.4,
                    "average_latency": 2.1,
                    "model": "gpt-3.5-turbo"
                },
                {
                    "id": "run_004",
                    "name": "Multi-Model Comparison",
                    "status": "running",
                    "created_at": "2024-01-01T12:00:00Z",
                    "total_cases": 412,
                    "success_rate": 0,
                    "average_latency": 0,
                    "model": "multiple"
                }
            ]
        
        elif path.startswith('test-runs/') and 'results' in event.get('path', ''):
            run_id = path.split('/')[0]
            response = [
                {
                    "test_id": f"test_{i}",
                    "status": "success" if i % 10 != 0 else "error",
                    "input_data": f"Test prompt {i}",
                    "output_data": f"Response {i}" if i % 10 != 0 else None,
                    "error_message": "Injection detected" if i % 10 == 0 else None,
                    "latency": 500 + (i * 50),
                    "created_at": "2024-01-01T12:00:00Z"
                } for i in range(1, 21)
            ]
        
        else:
            return {
                'statusCode': 404,
                'headers': headers,
                'body': json.dumps({"error": "Endpoint not found"})
            }
        
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps(response)
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({"error": str(e)})
        }
