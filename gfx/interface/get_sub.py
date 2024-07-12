import struct

def read_dds_header(file_path):
    with open(file_path, 'rb') as f:
        header = f.read(128)
        
        if header[:4] != b'DDS ':
            raise ValueError("Not a valid DDS file")
        
        height, width = struct.unpack('II', header[12:20])
        mipmap_count = struct.unpack('I', header[28:32])[0]
        pixel_format = header[84:88].decode('utf-8')
        
        return {
            'height': height,
            'width': width,
            'mipmap_count': mipmap_count,
            'pixel_format': pixel_format
        }

dds_info = read_dds_header('african_map_cover.dds')
print(dds_info)
