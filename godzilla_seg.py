from PIL import Image

def generate_7seg_image(N, output_path):
    segment_files = [
        '7s0.png',
        '7s1.png',
        '7s2.png',
        '7s3.png',
        '7s4.png',
        '7s5.png',
        '7s6.png',
    ]

    base = Image.new('RGBA', (512, 512), (0, 0, 0, 0))

    for bit in range(7):
        if (N >> bit) & 1:
            segment_img = Image.open(f'./seg/{segment_files[bit]}')
            base.alpha_composite(segment_img)

    base.save(output_path)
    print(f"Saved image for N = {N} as {output_path}")

for i in range(128):
    generate_7seg_image(i, output_path=f'./output/{i}.png')