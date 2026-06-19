-- Create table for tracking data
CREATE TABLE tracking_data (
    id BIGSERIAL PRIMARY KEY,
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    ip_address VARCHAR(50),
    token VARCHAR(255),
    latitude DECIMAL(10, 8),
    longitude DECIMAL(11, 8),
    city VARCHAR(100),
    country VARCHAR(100),
    foto_filename VARCHAR(255),
    accuracy DECIMAL(10, 2),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Create index on token for faster queries
CREATE INDEX idx_tracking_data_token ON tracking_data(token);

-- Create index on timestamp for sorting
CREATE INDEX idx_tracking_data_timestamp ON tracking_data(timestamp DESC);

-- Enable Row Level Security (optional, for production)
ALTER TABLE tracking_data ENABLE ROW LEVEL SECURITY;

-- Create policy to allow all operations (for development)
-- In production, you should restrict this based on your authentication needs
CREATE POLICY "Allow all operations on tracking_data" 
ON tracking_data FOR ALL 
USING (true) 
WITH CHECK (true);
