from PIL import Image, ImageDraw, ImageFont
from pydash import group_by
import re

def stripVolume(name):
    return re.sub('(\s+\d?\.\d+\s?L)', '', name)

def renderImage(data, out):
    
    data_grouped = group_by(data, lambda row:  round(row['Org_Disc_Price'] / 10) * 10 )
    
    groups_count = len(data_grouped.keys())
    font_size = 25
    line_height = font_size + 5
    padding_left = 50
    font = ImageFont.truetype("/Users/nur/Documents/code/vine-shopper/OpenSans-Regular.ttf", font_size)

    img = Image.new("RGB", (1024, line_height * (len(data) + groups_count)))
    draw = ImageDraw.Draw(img)
    group_idx = 0
    lines_written = 0
    current_y = 0
    for group_name, group in data_grouped.items():
        draw.text((padding_left, current_y), '                     >>>>>>>>>>>>>>>> {0} - {1} SGD<<<<<<<<<<<<<<<'.format(group_name, group_name + 10), (255,255,0), font=font)
        current_y += line_height

        for row in group:    
            draw.text((padding_left, current_y), '{0}'.format(stripVolume(row['ProductGroupTitle'])), (255,255,0), font=font)
            current_y += line_height
        lines_written += len(group)
        
        
    
    draw = ImageDraw.Draw(img)
    img.save(out)

if __name__ == '__main__':
    data = [{'ProductGroupTitle': 'FRESCOBALDI NIPOZZANO RISERVA 0.75L', 'Org_Disc_Price': 31.0, 'Org_Price': 36.0}, {'ProductGroupTitle': 'CHATEAU HAUT-BONNEAU 0.75 L', 'Org_Disc_Price': 30.0, 'Org_Price': 30.0}, {'ProductGroupTitle': 'TERRAZAS RESERVA MALBEC 0.75 L', 'Org_Disc_Price': 24.0, 'Org_Price': 29.0}]
    renderImage(data, '/tmp/img1.jpg')