from PIL import Image
import color
import cv2
import time

print(color.hide)


def get_color(image):
    couleurs_pixels = []
    largeur, hauteur = image.size

    for y in range(hauteur):
        ligne_couleurs = []
        for x in range(largeur):
            couleur = image.getpixel((x, y))
            ligne_couleurs.append(couleur)
        couleurs_pixels.append(ligne_couleurs)

    return couleurs_pixels


def print_image(image, widht: int = None, height: int = None, margin: str = '', margin2: str = '', char: str = ' ', background: bool = True):
    largeur, hauteur = image.size
    if widht == None:
        widht = int(color.os.get_terminal_size().columns/2)
    if height == None:
        facteur_redimensionnement = widht / float(largeur)
        height = int(float(hauteur) * float(facteur_redimensionnement))

    image = image.resize((widht, height))

    couleurs_pixels = get_color(image)
    for ligne in couleurs_pixels:
        print(end=margin)
        for couleur in ligne:
            color.rgbprint(couleur[0], couleur[1], couleur[2],
                           char, background=background, end=color.RESET_ALL)
        print(end=margin2+'\n')


def video(video_path:str, img:int =4, t:int=0, *args, **kwargs):
    """Display a video in the terminal

    Args:
        video_path (str): the path of the video
        img (int, optional): the ratio of skipped frames. Defaults to 4.
        t (int, optional): the time to wait beetween each frame. Defaults to 0.
    """
    cap = cv2.VideoCapture(video_path)
    i = 0
    ret = True

    while cap.isOpened() and ret:
        ret, frame = cap.read()
        if ret:
            if i % img == 0:
                pil_image = Image.fromarray(
                    cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                color.clear()
                print_image(pil_image, *args, **kwargs)
                time.sleep(t)

            i += 1

    cap.release()
    
    
if __name__ == "__main__":
    
    vid = "STAR WARS A NEW HOPE Opening Scene (1977) George Lucas.mp4"
    video(vid, 10, t=0.01, background=True, char=' ')