from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from poll.serializers import SurveyCategoryCreateSerializer
from utilities.models import Lga, State
from utilities.serializers import *

# Create your views here.
@api_view(['GET', 'POST'])
def seed_states(request):

    if request.method == 'POST':
        data =  [(1,'Abia'),(2,'Adamawa'),(3,'Akwa Ibom'),(4,'Anambra'),(5,'Bauchi'),(6,'Bayelsa'),(7,'Benue'),(8,'Borno'),(9,'Cross river'),(10,'Delta'),(11,'Ebonyi'),(12,'Edo'),(13,'Ekiti'),(14,'Enugu'),(15,'Fct'),(16,'Gombe'),(17,'Imo'),(18,'Jigawa'),(19,'Kaduna'),(20,'Kano'),(21,'Katsina'),(22,'Kebbi'),(23,'Kogi'),(24,'Kwara'),(25,'Lagos'),(26,'Nasarawa'),(27,'Niger'),(28,'Ogun'),(29,'Ondo'),(30,'Osun'),(31,'Oyo'),(32,'Plateau'),(33,'Rivers'),(34,'Sokoto'),(35,'Taraba'),(36,'Yobe'),(37,'Zamfara')]
        for i in data:
            json_data = {"name" : i[1]}
            serialized_data = StateSerializer(data=json_data)
            if serialized_data.is_valid():
                serialized_data.save()
        return Response(serialized_data.data)


@api_view(['POST'])
def seed_lga(request):
        if request.method == 'POST': 
            data = [(43,'Abaji',15,359),(43,'Bwari',15,360),(43,'Gwagwalada',15,359),(43,'Kuje',15,359),(43,'Kwali',15,359),(43,'Municipal',15,360)]
            for i in data:
                json_data = {"name" : i[1], "state_id" : i[2], "senatorial_id" : i[0], "constituency_id" : i[3]}
                serialized_data = LgaSerializer(data=json_data)
                if serialized_data.is_valid():
                    serialized_data.save()
            return Response(serialized_data.data)



@api_view(['POST'])
def seed_senatorial(request):

    if request.method == 'POST':
        data = [('Abia Central',1),('Abia North',1),('Abia South',1),('Adamawa Central',2),('Adamawa North',2),('Adamawa South',2),('Akwa Ibom North East',3),('Akwa Ibom North West',3),('Akwa Ibom South',3),('Anambra Central',4),('Anambra North',4),('Anambra South',4),('Bauchi Central',5),('Bauchi North',5),('Bauchi South',5),('Bayelsa Central',6),('Bayelsa East',6),('Bayelsa West',6),('Benue North East',7),('Benue North West',7),('Benue South',7),('Borno Central',8),('Borno North',8),('Borno South',8),('Cross River Central',9),('Cross River North',9),('Cross River South',9),('Delta Central',10),('Delta North',10),('Delta South',10),('Ebonyi South',11),('Ebonyi Central',11),('Ebonyi North',11),('Edo South',12),('Edo Central',12),('Edo North',12),('Ekiti South',13),('Ekiti Central',13),('Ekiti North',13),('Enugu North',14),('Enugu East',14),('Enugu West',14),('Federal Capital Territory',15),('Gombe Central',16),('Gombe North',16),('Gombe South',16),('Imo East',17),('Imo North',17),('Imo West',17),('Jigawa North - West',18),('Jigawa North - East',18),('Jigawa South - West',18),('Kaduna Central',19),('Kaduna North',19),('Kaduna South',19),('Kano South',20),('Kano Central',20),('Kano North',20),("Katsina Central",21),('Katsina North',21),('Katsina South',21),('Kebbi Central',22),('Kebbi North',22),('Kebbi South',22),('Kogi Central',23),('Kogi East',23),('Kogi West',23),('Kwara Central',24),('Kwara North',24),('Kwara South',24),('Lagos West',25),('Lagos Central',25),('Lagos East',25),('Nasarawa South',26),('Nasarawa North',26),('Nasarawa West',26),('Niger East',27),('Niger North',27),('Niger South',27),('Ogun Central',28),('Ogun East',28),('Ogun West',28),('Ondo Central',29),('Ondo North',29),('Ondo South',29),('Osun Central',30),('Osun East',30),('Osun West',30),("Oyo Central",31),('Oyo North',31),('Oyo South',31),('Plateau Central',32),('Plateau North',32),('Plateau South',32),('Rivers East',33),('Rivers South East',33),('Rivers West',33),('Sokoto East',34),('Sokoto North',34),('Sokoto South',34),('Taraba Central',35),('Taraba North',35),('Taraba South',35),('Yobe East',36),('Yobe North',36),('Yobe South',36),('Zamfara Central',37),('Zamfara North',37),('Zamfara West',37)]
        for i in data:
            json_data = {"name" : i[0], "state_id" : i[1]}
            serialized_data = SenatorialSerializer(data=json_data)
            if serialized_data.is_valid():
                serialized_data.save()
        return Response(serialized_data.data)

@api_view(['POST'])
def seed_constituencies(request):

    if request.method == 'POST':
        data = [('Aba N/S',1),('Arochukwu/Ohafia',1),('Bende',1),('Nsiala Ngwa N/S',1),('Isuikwuato/Umu-Nneochi',1),('Obingwa/Ugwunagbo/Osisioma',1),('Umuahia(N/S)/Ikwuano',1),('Ukwa E/W',1),('Demsa/Numan/Lamurde',2),('Furore/Song',2),('Mayo Belwa/Ganye/Jada/Toungo',2),('Gombi/Hong',2),('Guyuk/Shelleng',2),('Madagali/Michika',2),('Maiha/Mubi(N/S)',2),('Yola(N/S)/Girei',2),('Abak/Etim Ekpo/Ika',3),('Eket/Onna/Esit Eket/Ibeno',3),('Etinan/Nsit Ibom/Nsit Ubium',3),('Ikono/Ini',3),('Ikot Absai/Mkpat Enin/Eastern Obolo',3),('Ikot Ekpene/Essien Udim/Obot Akara',3),('Itu/Ibiono Ibom',3),('Oron/Mbo/Okobo/Udung Uko/Urue Offong/Uruko',3),('Ukanafun/Oruk Anam',3),('Uyo/Uruan/Nsit Atai/Ibesikpo Asutan',3),('Anambra(E/W)',4),('Onitcha(N/S)',4),('Ogbaru',4),('Aguata',4),('Oyi/Ayamelum',4),('Awka(N/S)',4),('Nijikoka/Dunukofia/Anaocha',4),('Idemili(N/S)',4),('Ihiala',4),('Nnewi(N/S)/Ekwusigo',4),('Orumba(N/S)',4),('Alkaleri/Kirfi',5),('Bauchi',5),('Bogoro/Dass/Tafawa Balewa',5),('Toro',5),('Ningi/Warji',5),('Darazo/Gunjuwa',5),('Misau/Dambam',5),('Zaki',5),('Gamawa',5),('Jamaare/Itas-Gadau',5),('Shira/Giade',5),('Katagum',5),('Brass/Nembe',6),('Ogbia',6),('Sagbama/Ekeremor)',6),('Southern Ijaw',6),('Yenagoa/Kolokuna/Opokuma',6),('Ado/Obadigbo/Okpokwu',7),('Apa/Agatu',7),('Buruku',7),('Gboko/Tarka',7),('Guma/Makurdi',7),('Gwer East/West',7),('Konshisha/Vandeikya',7),('Kwande/Ushongo',7),('Oju/Obi',7),('Otukpo/Ohimini',7),('Askira-Uba/Hawul',8),('Bama/Ngala/Kala-Balge',8),('Biu/Kwaya-Kusar, Shani/Bayo',8),('Dikwa/Mafa/Konduga',8),('Damboa/Gwoza/Chibok',8),('Kaga/Gubio/Magumeri',8),('Monguno/Nganzai/Marte',8),('Kukawa/Mobbar/Abadam/ Guzamali',8),('Maiduguri (Metropolitan)',8),('Jere',8),
        ('Yakurr/Abi',9),('Akamkpa/Biase',9),('Boki/Ikom',9),('Calabar South/Akpabuyo/Bakassi',9),('Calabar Municipal/Odukpani',9),('Obanliku/Obudu/Bekwarra',9),('Obubra/Etung',9),('Ogoja/Yala',9),('Aniocha(N/S)/Oshimili(N/S)',10),('Bomadi/Patani',10),('Ethiope East/Ethiope West',10),('Ika North East/Ika South',10),('Isoko(N/S)',10),('Nkokwa(E&S)/Ukwuani',10),('Okpe/Sapele/Uvwie)',10),('Burutu',10),('Ughelli(N/S)/Udu',10),('Warri(N/S/SE)',10),('Ebonyi/Ohaukwu',11),('Abakaliki/Izzi',11),('Ezza North/Ishielu',11),('Ezza South/Ikwo',11),('Ivo-Ohaozara/Onicha',11),('Afikpo(N/S)',11),('Akoko-Edo',12),('Esan Central/Esan South/Igueben',12),('Esan North East/Esan South East',12),('Etsako (E/W/C) ',12),('Egor/Ikpoba-Okha',12),('Oredo',12),('Orhionmwon/Uhunmwonde',12),('Ovia(NE/SW)',12),('Owan(E/W)',12),('Ado Ekiti/Irepodun/Ifelodun',13),('Ekiti South West/Ikere/Orun/Ise',13),('Emure/Gbonyin/Ekiti East',13),('Ido/Osi, Moba/Ilejeme',13),('Ijero/Ekiti West/Efon',13),('Ikole/Oye',13),('Aninri/Awgu/Oji River',14),('IEnugu East/Isi Uzo',14),
        ('Enugu(N/S)',14),('Ezeagu/Udi',14),('Igbo-Etiti/Uzo-Uwani',14),('Igbo-Eze North/Udenu',14),
        ('Nkanu East/Nkanu West',14),('Nsukka/Igbo-Eze South',14),('Akko',16),('Yamaltu/Deba',16),('Balanga/Billiri',16),('Kaltungo/Shongom',16),('Gombe/Kwami/Funakaye',16),('Dukku/Nafada',16),('Ehime Mbano/Ihite-Uboma/Obowo',17),('Isiala Mbano/Okigwe/Onuimo',17),('Ideato(N/S)',17),('Isu/Njaba/Nkwerre/Nwangele',17),('Oguta/Ohaji-Egbema/Oru West',17),('Oru East/Orsu/Orlu',17),('Aboh Mbaise/Ngor Okpala',17),('Ahiazu Mbaise/Ezinihitte',17),('Ikeduru/Mbaitoli',17),('Owerri Municipal/Owerri(N/W)',17),('Babura/Garki',18),('Birnin Kudu/Buji',18),('Birniwa Guri/Kirikasamma',18),('Dutse/Kiyawa',18),('Gwaram',18),('Gumel/Maigatari/Sule Tankarkar/Gagarawa',18),('Hadejia/Kafin Hausa',18),('Jahun/Miga',18),('Mallam Madori/Kaugama',18),('Kazaure/Roni/Gwiwa/Yankwashi',18),('Ringim/Taura',18),('Kaduna North',19),('Zaria',19),('Soba',19),('Igabi',19),('Ikara/Kubau',19),('Makarfi/Kudan',19),('Lere',19),('Kachia/Kagarko',19),('Chikun/Kajuru',19),('Jemaa/Sanga',19),('Birnin Gwari/Giwa',19),('Sabon Gari',19),('Kaduna South',19),('Kaura',19),('Kauru',19),('Zangon Kataf/Jaba',19),('Alabasu/Gaya/Ajingi',20),('Shanono/Bagwai',20),('Bebeji/Kiru',20),('Bichi',20),('Rano/Bunkure/Kibiya',20),('Dala',20),('Gwale',20),('Dambatta/Makoda',20),('Dawakin Kudu/Warawa',20),('Dawakin Tofa/Tofa/Rimin Gado',20),('Doguwa/Tudun Wada',20),('Gezawa/Gabasawa',20),('Gwarzo/Ikabo',20),('Municipal',20),('Tarauni',20),('Karaye/Rogo',20),('Kumbotso',20),('Kura/Madobi/Garun Mallam',20),('Nassarawa',20),('Fagge',20),('Sumaila/Takai',20),('Minjibir/Ungogo',20),('Tsanyawa/Kunchi',20),('Wudil/Garko',20),('Bakori/Danja',21),('Batagarawa/Charanchi/Rimi',21),('Batsari/Safana/Danmusa',21),('Bindawa/Mani',21),('Daura/Sandamu/Maiadua',21),('Dutsin-ma/Kurfi',21),('Faskari/Kankara/Sabuwa',21),('Funtua/Dandume',21),('Ingawa/Kankia/Kusada',21),('Jibia/Kaita',21),('Malumfashi/Kafur',21),('Katsina',21),('Mashi/Dutsi',21),('Matazu/Musawa',21),('Zango/Baure',21),('Arewa/Dandi',22),('Argungu/Augie',22),('Bagudo/Suru',22),('Bunza/Birnin Kebbi/Kalgo',22),('Aleiro/Gwandu/Jega',22),('Koko-Besse/Maiyama',22),('Fakai/Sakaba/Wasagu/Danko/Zuru',22),('Ngaski/Shanga/Yauri',22),('Adavi/Okehi',23),('Ankpa/Omala/Olamaboro',23),('Bassa/Dekina',23),('Idah/Igalamela Odolu/Ibaji/ Ofu',23),('Ijumu/Kabba-Bunu',23),('Ajaokuta',23),('Kogi (Lokoja)/Kogi (K.K.)',23),('Okene/Ogori-Magogo',23),('Yagba East/Yagba West/ Mopamuro',23),('Baruten/Kaiama',24),('Edu/Moro/Pategi',24),('Ekiti/Isin/Irepodun/Oke-Ero',24),('Ilorin East/Ilorin South',24),('Ilorin West/Asa',24),('Ifelodun/Offa/Oyun',24),('Agege',25),('Ifako/Ijaiye',25),('Alimosho',25),('Badagry',25),('Epe',25),('Ibeju Lekki',25),('Eti-Osa',25),('Apapa',25),('Ikeja',25),('Ikorodu',25),('Lagos Island I',25),('Lagos Island II',25),('Lagos Mainland',25),('Mushin I',25),('Mushin II',25),('Ojo',25),('Amuwo-Odofin',25),('Ajeromi/Ifelodun',25),('Oshodi/Isolo I',25),('Oshodi/Isolo II',25),('Shomolu',25),('Kosofe',25),('Surulere I',25),('Surulere II',25),('Akwanga/Nassarawa Eggon/ Wamba',26),('Awe/Doma/Keana',26),('Keffi/Karu/Kokona',26),('Lafia/Obi',26),('Nassarawa/Toto',26),('Agaie/Lapai',27),('Agwara/Borgu',27),('Bida/Gbako/Katcha',27),('Booso/Paikoro',27),('Chanchaga',27),('Gurara/Suleja/Tapa',27),('Lavun/Mokwa/Edati',27),('Magama/Rijau',27),('Kontagora/Wushishi/Mariga/ Mashegu',27),('Shiroro/Rafi/Munya',27),('Abeokuta North/ Obafemi-Owode/Odeda',28),('Abeokuta South',28),('Ado-Odo/Ota',28),('Egbado North/Imeko-Afon',28),('Egbado South/Ipokia',28),('Ifo/Ewekoro',28),('Ijebu North/Ijebu East/Ogun Waterside',28),('Ijebu Ode /Odogbolu /Ijebu North East',28),('Ikenne/Shagamu/Remo North',28),('Akoko North East/Akoko North West',29),('Akoko South East/Akoko South West',29),('Akure North/Akure South',29),('Idanre/Ifedore',29),('Ileoluji/Okeigbo/Odigbo',29),('Okitipupa/Irele',29),('Eseodo/Ilaje',29),('Ondo East/Ondo West',29),('Owo/Ose',29),('Irepodun/Olorunda/Osogbo/Orolu',30),('Odo-Otin/Ifelodun/Boripe',30),('Boluwaduro/Ifedayo/Ila',30),('Atakunmosa(E&W)/Ilesha(E&W)',30),('Obokun/Oriade',30),('Ife(C/N/S/E)',30),('Ayedire/Iwo/Ola-Oluwa',30),('Ayedaade/Irewole/Isokan',30),('Ede(N/S)/Egbedore/Ejigbo',30),('Afijio/Oyo(E/W)/Atiba',31),('Akinyele/Lagelu',31),('Egbeda/Ona-Ara',31),('Ibarapa Central/Ibarapa North',31),('Ibarapa East/Ido',31),('Saki(E/W)/Atisbo',31),('Irepo/Orelope/Olorunsogo',31),('Iseyin/Itesiwaju/Kajola/Iwajowa',31),('Ogbomoso(N/S)/Orire',31),('Ogo-Oluwa/Surulere',31),('Oluyole',31),('Ibadan NorthEast/Ibadan SouthEast',31),('Ibadan South West/Ibadan North West',31),('Ibadan North',31),('Jos North/Bassa',32),('Jos South/Jos East',32),('Barkin Ladi/Riyom',32),('Bokkos/Mangu',32),('Kanke/Pankshin/Kanam',32),('Wase',32),('Langtang North/Langtang South',32),('Mikang/Quaan/Pan/Shedam',32),('Abua-Odual/Ahaoda East',33),('Ahoada West/Ogba Egbema',33),('Degema/Bonny',33),('Akuku-Toru/Asari-Toru',33),('Okrika/Ogu-Bolo',33),('Opobo/Nkoro/Andoni',33),('Eleme/Tai/Oyigbo',33),('Khana/Gokana',33),('Ikwerre/Umohua',33),('Etche/Omuma',33),('Obio Akpor',33),('Port Harcourt I',33),('Port Harcourt II',33),('Isa/Sabon Birni',34),('Goronyo/Gada',34),('Wurno/Rabah',34),('Illela/Gwadabawa',34),('Tangaza/Gudu',34),('Binji/Silame',34),('Kware/Wamakko',34),('Sokoto North/Sokoto South',34),('Dange-Shuni/Bodinga/Tureta',34),('Yabo/Shagari',34),('Kebbe/Tambuwal',34),('Bali/Gassol',35),('Takum/Donga/Ussa',35),('Sardauna/Kurmi/Gashaka',35),('Ibi/Wukari',35),('Jalingo/Yorro/Zing',35),('Karim Lamido/Lau/Ardo-Kola',35),('Bade/Jakusko',36),('Bursari/Geidam/Yunusari',36),('Damaturu/Gujba/Gulani/ Tarmuwa',36),('Fika/Fune',36),('Machina/Nguru/Yusufari/ Karasuwa',36),('Nangere/Potiskm',36),('Kaura-Namoda/Birnin Magaji',37),('Shinkafi/Zurmi',37),('Gusau/Tsafe',37),('Bungudu/Maru',37),('Anka/Talata Mafara',37),('Bakura/Maradun',37),('Gummi/Bukkuyum',37),('Abaji/Gwagwalada/Kwali/Kuje',15),('Municipal/Bwari',15)
        ]
        for i in data:
            json_data = {"name" : i[0], "state_id" : i[1]}
            serialized_data = ConstituencySerializer(data=json_data)
            if serialized_data.is_valid():
                serialized_data.save()
        return Response(serialized_data.data)
 
@api_view(['DELETE'])
def clearStates(request):
    if request.method == 'DELETE':
        count = State.objects.all().delete().count
    return Response({'Message':'States Deleted'})

@api_view(['DELETE'])
def clearLga(request):
    if request.method == 'DELETE':
        count = Lga.objects.all().delete()
    return Response({'Message':'LGAs Deleted'})

@api_view(['DELETE'])
def clearSen(request):
    if request.method == 'DELETE':
        Senatorial.objects.all().delete()
    return Response({'Message':'Sen Deleted'})

@api_view(['DELETE'])
def clearParty(request):
    if request.method == 'DELETE':
        Party.objects.all().delete()
    return Response({'Message':'Party Deleted'})

@api_view(['POST'])
def seed_parties(request):

    if request.method == 'POST':
        data =  [('Accord', 'A', "media/party_pictures/A.jpg"),('Action Alliance', 'AA', "media/party_pictures/AA.jpg"),('Action Democratic Party', 'ADP', "media/party_pictures/ADP.png"),('Action Peoples Party','APP', 'media/party_pictures/APP.png'),('African Action Congress','AAC', 'media/party_pictures/AAC.jpg'),('African Democratic Congress', 'ADC', 'media/party_pictures/ADC.jpg'),('All Progressives Congress','APC', 'media/party_pictures/apclogo.jpg'),('All Progressives Grand Alliance','APGA', 'media/party_pictures/APGA.jpg'),('Allied Peoples Movement', 'APM', 'media/party_pictures/APM.jpg'),('Boot Party', 'BP', 'media/party_pictures/BootParty.jpg'),('Labour Party', 'LP','media/party_pictures/LP.jpg'),('National Rescue Movement', 'NRM', 'media/party_pictures/NRM.png'),('New Nigeria Peoples Party', 'NNPP', 'media/party_pictures/NNPP.jpg'),('Peoples Democratic Party', 'PDP', 'media/party_pictures/PDP.jpg'),('Peoples Redemption Party', 'PRP', 'media/party_pictures/PRP.png'),('Social Democratic Party', 'SDP', 'media/party_pictures/SDP.png'),('Young Progressive Party', 'YPP', 'media/party_pictures/YPP-Logo.jpeg'),('Zenith Labour Party', 'ZLP', 'media/party_pictures/ZLP.jpg')]
        for i in data:
            json_data = {"name" : i[0], "abbr" : i[1], "logo" : i[2]}
            serialized_data = PartySerializer(data=json_data)
            if serialized_data.is_valid():
                serialized_data.save()
                print(i[2])
        return Response(serialized_data.data)

@api_view(['POST'])
def seed_survey(request):

    if request.method == 'POST':
        serialized_data = SurveyCategoryCreateSerializer(data = {"surveyName" : "Others" })
        if serialized_data.is_valid():
            serialized_data.save()
    return Response(serialized_data.data)

@api_view(['POST'])
def seed_poll_category(request):

    if request.method == 'POST':
        data =  ['Presidential Poll', 'Gubernatorial Poll', 'Senatorial Poll', 'House of Assembly Poll']
        for i in data:
            json_data = {"title" : i}
            serialized_data = PollCategorySerializer(data=json_data)
            if serialized_data.is_valid():
                serialized_data.save()
        return Response(serialized_data.data)
