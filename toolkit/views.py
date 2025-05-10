from django.shortcuts import render
import nmap 
from django.http import HttpResponse
import requests

def index(request):
    return render(request, "index.html")

def scan_ports(request):
    response = requests.get("https://example.com")
    headers = response.headers
    output = "\n".join(f"{k}: {v}" for k, v in headers.items())
    download_link = '<a href="/download/scan_ports/">Download Report</a>'
    return HttpResponse(f"<pre>{output}</pre>{download_link}")

def analyze_headers(request):
    response = requests.get("https://example.com")
    headers = response.headers
    output = "\n".join([f"{k}: {v}" for k, v in headers.items()])
    download_link = '<a href="/download/headers/">Download Report</a>'
    return HttpResponse(f"<pre>{output}</pre>{download_link}")

def bruteforce_simulation(request): 
    simulated_output = """
    Starting Brute Force Attack on target: demo.example.com
    Using Dictionary: rockyou.txt

    Trying user: admin pass: 123456 - Failed
    Trying user: admin pass: password - Failed
    Trying user: admin pass: admin123 - SUCCESS
    Credentials found: admin / admin123
    """
    download_link = '<a href="/download/bruteforce/">Download Report</a>'
    return HttpResponse(f"<pre>{simulated_output}</pre>{download_link}") 

def download_report(request, report_type):
    reports = {
        "scan_ports": "Nmap Scan Simulation\nHost: 127.0.0.1\nPorts: 22/tcp open ssh, 80/tcp open http, 443/tcp open https\n...",
        "headers": "HTTP Header Analysis Report\nContent-Type: text/html\nETag: ...\nConnection: keep-alive\n...",
        "bruteforce": "Brute Force Attack Simulation\nUser: admin Password: admin123\nSUCCESS...",
    }
    content = reports.get(report_type, "Invalid report type")
    response = HttpResponse(content, content_type="text/plain")
    response["Content-Disposition"] = f"attachment; filename={report_type}_report.txt"
    return response

def security_practices(request):
    content = """
    1. Use strong and unique passwords.
    2. Enable Multi-factor Authentication (MFA).
    3. Regularly update your software.
    4. Be cautious with phishing emails.
    5. Secure your home network (Change default router passwords, use WPA3 encryption).
    6. Regular backups.
    7. Limit user permissions and privileges.
    8. Keep antivirus and anti-malware software updated.
    9. Educate yourself and others on cybersecurity trends and threats.
    """
    return HttpResponse(f"<pre>{content}</pre>")
