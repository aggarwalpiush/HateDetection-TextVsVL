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




#image_filenames = ["RoseanneBarr-1.jpg","DaveChappelle-1.jpg","BillClinton-1.jpg","DiegoMaradona-3.jpg","HulkHogan-1.jpg","StevieWonder-2.jpg","BenCarson-6.jpg","BustaRhymes-1.jpg","VinceMcMahon-1.jpg","BenjaminNetanjahu-1.jpg","JosephGoebbels-2.jpg","ChrisBrown-1.jpg","Al-Baghdadi-6.jpg","RoseanneBarr-2.jpg","DiegoMaradona-1.jpg","BenjaminCrump-6.png","HulkHogan-2.jpg","StevieWonder-1.jpg","VinceMcMahon-2.jpg","LorettaLynch-1.jpg","EltonJohn-2.jpg","BustaRhymes-6.jpg","BenCarson-1.jpg","IlhanOmar-1.jpg","BillClinton-7.jpg","Ocasio-Cortez-1.jpg","AdolfHitler3-1.jpg","PopeFrancis-1.jpg","DonaldTrumpJr-1.jpg","PopeBenedikt-2.jpg","DaveChappelle-6.jpg","MittRomney-1.jpg","WoodyAllen-1.jpg","KanyeWest-1.jpg","LorettaLynch-2.jpg","EltonJohn-1.jpg","IlhanOmar-2.jpg","Ocasio-Cortez-2.jpg","AdolfHitler3-2.jpg","BenjaminCrump-1.png","PopeFrancis-2.jpg","DonaldTrumpJr-2.jpg","PopeBenedikt-1.jpg","MittRomney-2.jpg","BenjaminNetanjahu-6.jpg","ChrisBrown-6.jpg","WoodyAllen-2.jpg","KanyeWest-2.jpg","Al-Baghdadi-1.jpg","StephenHawking-1.jpg","J.B.Pritzker-2.jpg","JackNicholson-1.jpg","HughHefner-2.jpg","BillGates-6.jpg","JoeJackson-2.jpg","JoeExotic-1.jpg","AdolfHitler-1.jpg","JustinTrudeau-2.jpg","BaiLing-1.jpg","StephenHawking-2.jpg","J.B.Pritzker-1.jpg","JackNicholson-2.jpg","HughHefner-1.jpg","JoeJackson-1.jpg","ColinPowell-6.jpg","JoeExotic-2.jpg","AdolfHitler-2.jpg","BarackObama-1.jpg","CarrollOConnor-1.jpg","JustinTrudeau-1.jpg","HassanRouhani-1.jpg","RussellTravers-1.jpg","GretaThunberg-1.jpg","HillaryClinton-2.jpg","MartinLutherKingJr-2.jpg","CaitlynJenner-9.jpg","PrinceHarry-2.jpg","MichelleObama-2.jpg","BillGates-1.jpg","TomiLahren-2.jpg","HassanRouhani-2.jpg","RussellTravers-2.jpg","GretaThunberg-2.jpg","HillaryClinton-1.jpg","CarrollOConnor-6.jpg","MartinLutherKingJr-1.jpg","PrinceHarry-1.jpg","AnneFrank-24.jpg","ColinPowell-1.jpg","BarackObama-7.jpg","MichelleObama-1.jpg","AdolfHitler2-1.jpg","BaiLing-6.jpg","TomiLahren-1.jpg","BridgetPowers-1.jpg","MarkZuckerberg-1.jpg","JoeBiden-2.jpg","BernieSanders-1.jpg","WillSmith-2.jpg","JosephGoebbels-1.jpeg","KingCharles-1.jpg","GeorgeWBush-2.jpg","LadyGaga-2.jpg","LindaSarsour-1.jpg","CaitlynJenner-7.jpg","BillCosby-1.jpg","ColinKoepernick-1.jpg","KimJongUn-2.jpg","AlexJones-6.jpg","XiJinping-1.jpg","MikePence-2.jpg","MahatmaGandhi-1.jpg","ConchitaWurst-6.jpg","ArnoldSchwarzenegger-1.jpg","MarkZuckerberg-2.jpg","JoeBiden-1.jpg","DavidCameron-6.jpg","WillSmith-1.jpg","KingCharles-2.jpg","ChrisEvans-1.jpg","GeorgeWBush-1.jpg","LadyGaga-1.jpg","AnneFrank-1.jpg","LindaSarsour-2.jpg","CaitlynJenner-4.jpg","ChrisRock-6.jpg","KimJongUn-1.jpg","XiJinping-2.jpg","MikePence-1.jpg","MahatmaGandhi-2.jpg","RondaRousey-1.jpg","JamesFranco-2.jpg","KamalaHarris-2.jpg","AlexJones-1.jpg","BernieSanders-7.jpg","RobertMugabe-1.jpg","ColinKoepernick-6.jpg","WladimirPutin-1.jpg","DonaldTrump-2.jpg","AnneFrank-12.jpg","NanaAddoDankwaAkufo-Addo-2.jpg","CaitlynJenner-1.jpg","BillCosby-7.jpg","JeremyCorbyn-1.jpg","SeanHannity-2.jpg","KevinHart-2.jpg","NadeschdaAndrejewnaTolokonnikowa-1.jpg","OprahWinfrey-2.jpg","BridgetPowers-6.jpg","KamalaHarris-1.jpg","JamesFranco-1.jpg","RobertMugabe-2.jpg","ChrisRock-1.jpg","DonaldTrump-1.jpg","WladimirPutin-2.jpg","AnneFrank-6.jpg","NanaAddoDankwaAkufo-Addo-1.jpg","ChrisEvans-6.jpg","JeremyCorbyn-2.jpg","SeanHannity-1.jpg","DavidCameron-1.jpg","KevinHart-1.jpg","NadeschdaAndrejewnaTolokonnikowa-2.jpg","OprahWinfrey-1.jpg","RondaRousey-3.jpg","ConchitaWurst-1.jpg","ArnoldSchwarzenegger-6.jpg","LalehBijani-2.jpg","BristolPalin-1.jpg","TigerWoods-1.jpg","PaulineHanson-2.jpg","RashidaTlaib-2.jpg","AngelaMerkel-1.jpg","LeoVaradkar-1.jpg","MelaniaTrump-1.jpg","GordonRamsay-2.jpg","AlbertEinstein-1.jpg","BritneySpears-7.jpg","BearGrylls-6.jpg","JussieSmollett-1.jpg","DarrylWorley-1.jpg","LalehBijani-1.jpg","TigerWoods-2.jpg","PaulineHanson-1.jpg","RashidaTlaib-1.jpg","LeoVaradkar-2.jpg","GordonRamsay-1.jpg","ChuckSchumer-1.jpg","MelaniaTrump-3.jpg","JussieSmollett-2.jpg","QueenElizabeth-2.jpg","NarendraModi-1.jpg","DarrylWorley-6.jpg","BearGrylls-1.jpg","RevAlSharpton-1.jpg","BritneySpears-1.jpg","AlbertEinstein-7.jpg","AngelaMerkel-6.jpg","GiorgioATsoukalos-1.jpg","OsamaBinLaden-1.jpg","BristolPalin-6.jpg","QueenElizabeth-1.jpg","NarendraModi-2.jpg","RevAlSharpton-2.jpg","ChuckSchumer-6.jpg","GiorgioATsoukalos-2.jpg","OsamaBinLaden-2.jpg"]






#image_filenames = ["RoseanneBarr-1.jpg, DaveChappelle-1.jpg, BillClinton-1.jpg, DiegoMaradona-3.jpg, HulkHogan-1.jpg, StevieWonder-2.jpg, BenCarson-6.jpg, BustaRhymes-1.jpg, VinceMcMahon-1.jpg, BenjaminNetanjahu-1.jpg, JosephGoebbels-2.jpg, ChrisBrown-1.jpg, Al-Baghdadi-6.jpg, RoseanneBarr-2.jpg, DiegoMaradona-1.jpg, BenjaminCrump-6.png, HulkHogan-2.jpg, StevieWonder-1.jpg, VinceMcMahon-2.jpg, LorettaLynch-1.jpg, EltonJohn-2.jpg, BustaRhymes-6.jpg, BenCarson-1.jpg, IlhanOmar-1.jpg, BillClinton-7.jpg, Ocasio-Cortez-1.jpg, AdolfHitler3-1.jpg, PopeFrancis-1.jpg, DonaldTrumpJr-1.jpg, PopeBenedikt-2.jpg, DaveChappelle-6.jpg, MittRomney-1.jpg, WoodyAllen-1.jpg, KanyeWest-1.jpg, LorettaLynch-2.jpg, EltonJohn-1.jpg, IlhanOmar-2.jpg, Ocasio-Cortez-2.jpg, AdolfHitler3-2.jpg, BenjaminCrump-1.png, PopeFrancis-2.jpg, DonaldTrumpJr-2.jpg, PopeBenedikt-1.jpg, MittRomney-2.jpg, BenjaminNetanjahu-6.jpg, ChrisBrown-6.jpg, WoodyAllen-2.jpg, KanyeWest-2.jpg, Al-Baghdadi-1.jpg, StephenHawking-1.jpg, J.B.Pritzker-2.jpg, JackNicholson-1.jpg, HughHefner-2.jpg, BillGates-6.jpg, JoeJackson-2.jpg, JoeExotic-1.jpg, AdolfHitler-1.jpg, JustinTrudeau-2.jpg, BaiLing-1.jpg, StephenHawking-2.jpg, J.B.Pritzker-1.jpg, JackNicholson-2.jpg, HughHefner-1.jpg, JoeJackson-1.jpg, ColinPowell-6.jpg, JoeExotic-2.jpg, AdolfHitler-2.jpg, BarackObama-1.jpg, CarrollOConnor-1.jpg, JustinTrudeau-1.jpg, HassanRouhani-1.jpg, RussellTravers-1.jpg, GretaThunberg-1.jpg, HillaryClinton-2.jpg, MartinLutherKingJr-2.jpg, CaitlynJenner-9.jpg, PrinceHarry-2.jpg, MichelleObama-2.jpg, BillGates-1.jpg, TomiLahren-2.jpg, HassanRouhani-2.jpg, RussellTravers-2.jpg, GretaThunberg-2.jpg, HillaryClinton-1.jpg, CarrollOConnor-6.jpg, MartinLutherKingJr-1.jpg, PrinceHarry-1.jpg, AnneFrank-24.jpg, ColinPowell-1.jpg, BarackObama-7.jpg, MichelleObama-1.jpg, AdolfHitler2-1.jpg, BaiLing-6.jpg, TomiLahren-1.jpg, BridgetPowers-1.jpg, MarkZuckerberg-1.jpg, JoeBiden-2.jpg, BernieSanders-1.jpg, WillSmith-2.jpg, JosephGoebbels-1.jpeg, KingCharles-1.jpg, GeorgeWBush-2.jpg, LadyGaga-2.jpg, LindaSarsour-1.jpg, CaitlynJenner-7.jpg, BillCosby-1.jpg, ColinKoepernick-1.jpg, KimJongUn-2.jpg, AlexJones-6.jpg, XiJinping-1.jpg, MikePence-2.jpg, MahatmaGandhi-1.jpg, ConchitaWurst-6.jpg, ArnoldSchwarzenegger-1.jpg, MarkZuckerberg-2.jpg, JoeBiden-1.jpg, DavidCameron-6.jpg, WillSmith-1.jpg, KingCharles-2.jpg, ChrisEvans-1.jpg, GeorgeWBush-1.jpg, LadyGaga-1.jpg, AnneFrank-1.jpg, LindaSarsour-2.jpg, CaitlynJenner-4.jpg, ChrisRock-6.jpg, KimJongUn-1.jpg, XiJinping-2.jpg, MikePence-1.jpg, MahatmaGandhi-2.jpg, RondaRousey-1.jpg, JamesFranco-2.jpg, KamalaHarris-2.jpg, AlexJones-1.jpg, BernieSanders-7.jpg, RobertMugabe-1.jpg, ColinKoepernick-6.jpg, WladimirPutin-1.jpg, DonaldTrump-2.jpg, AnneFrank-12.jpg, NanaAddoDankwaAkufo-Addo-2.jpg, CaitlynJenner-1.jpg, BillCosby-7.jpg, JeremyCorbyn-1.jpg, SeanHannity-2.jpg, KevinHart-2.jpg, NadeschdaAndrejewnaTolokonnikowa-1.jpg, OprahWinfrey-2.jpg, BridgetPowers-6.jpg, KamalaHarris-1.jpg, JamesFranco-1.jpg, RobertMugabe-2.jpg, ChrisRock-1.jpg, DonaldTrump-1.jpg, WladimirPutin-2.jpg, AnneFrank-6.jpg, NanaAddoDankwaAkufo-Addo-1.jpg, ChrisEvans-6.jpg, JeremyCorbyn-2.jpg, SeanHannity-1.jpg, DavidCameron-1.jpg, KevinHart-1.jpg, NadeschdaAndrejewnaTolokonnikowa-2.jpg, OprahWinfrey-1.jpg, RondaRousey-3.jpg, ConchitaWurst-1.jpg, ArnoldSchwarzenegger-6.jpg, LalehBijani-2.jpg, BristolPalin-1.jpg, TigerWoods-1.jpg, PaulineHanson-2.jpg, RashidaTlaib-2.jpg, AngelaMerkel-1.jpg, LeoVaradkar-1.jpg, MelaniaTrump-1.jpg, GordonRamsay-2.jpg, AlbertEinstein-1.jpg, BritneySpears-7.jpg, BearGrylls-6.jpg, JussieSmollett-1.jpg, DarrylWorley-1.jpg, LalehBijani-1.jpg, TigerWoods-2.jpg, PaulineHanson-1.jpg, RashidaTlaib-1.jpg, LeoVaradkar-2.jpg, GordonRamsay-1.jpg, ChuckSchumer-1.jpg, MelaniaTrump-3.jpg, JussieSmollett-2.jpg, QueenElizabeth-2.jpg, NarendraModi-1.jpg, DarrylWorley-6.jpg, BearGrylls-1.jpg, RevAlSharpton-1.jpg, BritneySpears-1.jpg, AlbertEinstein-7.jpg, AngelaMerkel-6.jpg, GiorgioATsoukalos-1.jpg, OsamaBinLaden-1.jpg, BristolPalin-6.jpg, QueenElizabeth-1.jpg, NarendraModi-2.jpg, RevAlSharpton-2.jpg, ChuckSchumer-6.jpg, GiorgioATsoukalos-2.jpg, OsamaBinLaden-2.jpg"]
