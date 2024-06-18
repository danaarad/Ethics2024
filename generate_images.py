import os



def generate_with_seed(sd_pipeline, prompt, seed, output_path="./images/"):
    print(prompt)
    image = sd_pipeline(prompt)['images'][0]

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    image_name = f"{output_path}/{prompt}_seed_{seed}.png"
    image.save(image_name)
