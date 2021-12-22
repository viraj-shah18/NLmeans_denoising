import os
from nl_means import nl_means
from utils import load_images, save_all, print_metrics
import yaml


if __name__ == "__main__":
    # assumption for the various parameters
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)

    patch_size=config['patch_size']
    search_size = config['search_size']
    h = config['h']
    sigma = config['sigma']
    a = config['a']
    img_folder, img_name = config['img_folder'], config['img_name']
    PATH = os.path.join(img_folder, img_name)
    save_folder = config['save_folder']
    if not os.path.exists(save_folder):
        os.mkdir(save_folder)
    
    image = load_images(PATH)

    # Gaussian noise Denoising
    nl_out1, gauss_out1, noisy_image1 = nl_means(image, patch_size, search_size, h, sigma, a, "gaussian")

    # Salt and pepper noise Denoising
    nl_out2, gauss_out2,noisy_image2 = nl_means(image, patch_size, search_size, h, sigma, a, "s&p")

    save_name1 = os.path.join(save_folder, f"GaussNoise{img_name}")
    save_name2 = os.path.join(save_folder, f"SPNoise{img_name}")
    save_all(noisy_image1, gauss_out1, nl_out1, save_name1)
    save_all(noisy_image2, gauss_out2, nl_out2, save_name2)

    print_metrics(image, noisy_image1, gauss_out1, nl_out1)
    print_metrics(image, noisy_image2, gauss_out2, nl_out2)