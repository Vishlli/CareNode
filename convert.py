with open("model.tflite", "rb") as f:
    data = f.read()

with open("model_data.h", "w") as out:
    out.write("const unsigned char model_data[] = {")
    for i, byte in enumerate(data):
        if i % 12 == 0:
            out.write("\n")
        out.write(f"0x{byte:02x}, ")
    out.write("\n};")
    out.write(f"\nconst unsigned int model_data_len = {len(data)};")
