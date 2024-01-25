import os
import json

def generate_annotation(image_list):
    annotation = {}
    for image in image_list:
        filename, _ = os.path.splitext(image)
        celeb_name_parts = filename.split("-")[0]
        celeb_name = " ".join([name.capitalize() for name in split_name(celeb_name_parts)])
        annotation[image] = {
            "celeb_boxes": [],
            "names": [celeb_name]
        }
    return annotation

def split_name(name):
    #split the name
    parts = []
    current_part = ""
    for char in name:
        if char.isupper() and current_part:
            parts.append(current_part)
            current_part = char
        else:
            current_part += char
    if current_part:
        parts.append(current_part)
    return parts

# paste output of extract_name.py
image_list = ['ChrisEvans-Counterf1.jpeg', 'KingCharles-Counterf1.jpeg', 'OsamaBinLaden-Counterf1.jpeg', 'KamalaHarris-Counterf1.jpeg', 'VinceMcMahon-Counterf1.jpeg', 'JosephGoebbels-Counterf1.jpeg', 'AdolfHitler-Counterf2.jpeg', 'JackNicholson-Counterf1.jpeg', 'JustinTrudeau-Counterf1.jpeg', 'MikePence-Counterf1.jpeg', 'HulkHogan-Counterf1.jpeg', 'DonaldTrump-Counterf1.jpeg', 'MartinLutherKingJr-Counterf1.jpeg', 'MichelleObama-Counterf1.jpeg', 'BillClinton-Counterf1.jpeg', 'BarackObama-Counterf1.jpeg', 'AnneFrank-Counterf1.jpeg', 'HillaryClinton-Counterf1.jpeg', 'StevieWonder-Counterf1.jpeg', 'CaitlynJenner-Counterf1.jpeg', 'AnneFrank-Counterf2.jpeg', 'PaulineHanson-Counterf1.jpeg', 'MartinLutherKingJr-Counterf2.jpeg', 'BillClinton-Counterf2.jpeg', 'BarackObama-Counterf2.jpeg', 'MarkZuckerberg-Counterf1.jpeg', 'TigerWoods-Counterf1.jpeg', 'DonaldTrump-Counterf2.jpeg', 'AnneFrank-Counterf3.jpeg', 'JoeBiden-Counterf1.jpeg', 'NadeschdaAndrejewnaTolokonnikowa-Counterf1.jpeg', 'Al-Baghdadi-Counterf1.jpeg', 'MikePence-Counterf2.jpeg', 'KamalaHarris-Counterf2.jpeg', 'AdolfHitler-Counterf1.jpeg', 'KevinHart-Counterf1.jpeg', 'OsamaBinLaden-Counterf2.jpeg', 'ChrisEvans-Counterf2.jpeg', 'BridgetPowers-Counterf1.jpeg', 'WillSmith-Counterf1.jpeg']
annotation = generate_annotation(image_list)


output_file = "output_counterf.json"
with open(output_file, "w") as f:
    json.dump(annotation, f, indent=4)

print(f"Annotation saved to {output_file}")










