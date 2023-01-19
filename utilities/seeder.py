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
        data =  [(1,'Abia'),(2,'Adamawa'),(3,'Akwa Ibom'),(4,'Anambra'),(5,'Bauchi'),(6,'Bayelsa'),(7,'Benue'),(8,'Borno'),
        (9,'Cross river'),(10,'Delta'),(11,'Ebonyi'),(12,'Edo'),(13,'Ekiti'),(14,'Enugu'),(15,'Fct'),(16,'Gombe'),(17,'Imo'),
        (18,'Jigawa'),(19,'Kaduna'),(20,'Kano'),(21,'Katsina'),(22,'Kebbi'),(23,'Kogi'),(24,'Kwara'),(25,'Lagos'),(26,'Nasarawa'),
        (27,'Niger'),(28,'Ogun'),(29,'Ondo'),(30,'Osun'),(31,'Oyo'),(32,'Plateau'),(33,'Rivers'),(34,'Sokoto'),(35,'Taraba'),(36,'Yobe'),(37,'Zamfara')]
        for i in data:
            json_data = {"name" : i[1]}
            serialized_data = StateSerializer(data=json_data)
            if serialized_data.is_valid():
                serialized_data.save()
        return Response(serialized_data.data)


@api_view(['POST'])
def seed_lga(request):
        if request.method == 'POST': 
            data = [(3,'Aba north',1,1),(3,'Aba south',1,1),(2,'Arochukwu',1, 2),(2,'Bende',1,3),(1,'Ikwuano',1,7),(1,'Isiala ngwa north',1,4),
            (1,'Isiala ngwa south',1,4),(2,'Isuikwuato',1,5),(3,'Obingwa',1,6),(2,'Ohafia',1,2),(3,'Osisioma',1,6),(3,'Ugwunagbo',1,6),(3,'Ukwa  west',1,8),
            (3,'Ukwa east',1,8),(2,'Umu - nneochi',1,5),(1,'Umuahia  south',1,7),(1,'Umuahia north',1,7),(6,'Demsa',2,9),(4,'Fufore',2,10),(6,'Ganye',2,11),
            (4,'Gire 1',2,16),(22,'Gombi',2,12),(6,'Guyuk',2,13),(4,'Hong',2,12),(6,'Jada',2,11),(6,'Lamurde',2,9),(5,'Madagali',2,14),(5,'Maiha',2,15),
            (6,'Mayo - belwa',2,11),(5,'Michika',2,14),(5,'Mubi north',2,15),(5,'Mubi south',2,15),(6,'Numan',2,9),(6,'Shelleng',2,13),(4,'Song',2,10),
            (6,'Toungo',2,11),(4,'Yola north',2,16),(4,'Yola south',2,16),(8,'Abak',3,17),(9,'Eastern obolo',3,21),(9,'Eket',3,18),(9,'Esit eket (uquo)',3,18),
            (8,'Essien udim',3,22),(8,'Etim ekpo',3,17),(7,'Etinan',3,19),(9,'Ibeno',3,18),(7,'Ibesikpo asutan',3,26),(7,'Ibiono ibom',3,23),(8,'Ika',3,17),
            (8,'Ikono',3,20),(9,'Ikot abasi',3,21),(8,'Ikot ekpene',3,22),(8,'Ini',3,20),(7,'Itu',3,23),(9,'Mbo',3,24),(9,'Mkpat enin',3,21),(7,'Nsit atai',3,26),
            (7,'Nsit ibom',3,19),(59,'Nsit ubium',3,19),(8,'Obot akara',3,22),(9,'Okobo',3,24),(9,'Onna',3,18),(9,'Oron',3,24),(8,'Oruk anam',3,25),(9,'Udung uko',3,24),
            (8,'Ukanafun',3,25),(7,'Uruan',3,26),(9,'Urue offong/Oruko',3,24),(7,'Uyo',3,26),(12,'Aguata',4,30),(11,'Anambra east',4,27),(11,'Anambra west',4,27),
            (10,'Anaocha',4,33),(10,'Awka north',4,32),(10,'Awka south',4,32),(11,'Ayamelum',4,31),(10,'Dunukofia',4,33),(12,'Ekwusigo',4,36),(10,'Idemili north',4,34),
            (10,'Idemili-south',4,34),(12,'Ihala',4,35),(10,'Njikoka',4,33),(12,'Nnewi north',4,36),(12,'Nnewi south',4,36),(11,'Ogbaru',4,29),(11,'Onitsha -south',4,28),
            (11,'Onitsha-north',4,28),(12,'Orumba  south',4,37),(12,'Orumba north',4,37),(11,'Oyi',4,31),(15,'Alkaleri',5,38),(15,'Bauchi',5,39),(15,'Bogoro',5,40),
            (94,'Dambam',13,44),(95,'Darazo',13,43),(15,'Dass',5,40),(14,'Gamawa',5,46),(13,'Ganjuwa',5,43),(14,'Giade',5,48),(14,'Itas/gadau',5,47),(14,'Jama\'are',5,47),
            (14,'Katagum',5,49),(15,'Kirfi',5,38),(13,'Misau',5,44),(13,'Ningi',5,42),(14,'Shira',5,48),(15,'Tafawa balewa',5,40),(15,'Toro',5,41),(13,'Warji',5,42),
            (14,'Zaki',5,45),(17,'Brass',6,50),(18,'Ekeremor',6,52),(16,'Kolokuma/Opokuma',6,54),(17,'Nembe',6,50),(17,'Ogbia',6,51),(18,'Sagbama',6,52),
            (16,'Southern ijaw',6,53),(16,'Yenagoa',6,54),(21,'Ado',7,55),(21,'Agatu',7,56),(21,'Apa',7,56),(20,'Buruku',7,57),(20,'Gboko',7,58),(20,'Guma',7,59),
            (20,'Gwer East',7,60),(20,'Gwer West',7,60),(19,'Katsina-ala',7,61),(19,'Konshisha',7,62),(19,'Kwande',7,63),(19,'Logo',7,61),(20,'Makurdi',7,59),
            (21,'Obi',7,64),(21,'Ogbadibo',7,55),(21,'Ohimini',7,65),(21,'Oju',7,64),(21,'Okpokwu',7,55),(21,'Otukpo',7,65),(20,'Tarka',7,58),(19,'Ukum',7,61),
            (19,'Ushongo',7,63),(19,'Vandeikya',7,62),(23,'Abadam',8,73),(24,'Askira-Uba',8,66),(22,'Bama',8,67),(24,'Bayo',8,68),(24,'Biu',8,68),(24,'Chibok',8,70),
            (24,'Damboa',8,70),(22,'Dikwa',8,69),(23,'Gubio',8,71),(23,'Guzamali',8,73),(24,'Gwoza',8,70),(24,'Hawul',8,66),(22,'Jere',8,75),(22,'Kaga',8,71),
            (22,'Kala balge',8,67),(22,'Konduga',8,69),(23,'Kukawa',8,73),(24,'Kwaya/kusar',8,68),(22,'Mafa',8,69),(23,'Magumeri',8,71),(22,'Maiduguri m.c.',8,74),
            (163,'Marte',8,72),(23,'Mobbar',8,73),(23,'Monguno',8,72),(22,'Ngala',8,67),(23,'Nganzai',8,72),(24,'Shani',8,68),(25,'Abi',9,76),(27,'Akamkpa',9,77),
            (27,'Akpabuyo',9,79),(27,'Bakassi',9,79),(26,'Bekwarra',9,81),(26,'Biase',9,77),(25,'Boki',9,78),(27,'Calabar municipality',9,80),(27,'Calabar south',9,79),
            (25,'Etung',9,82),(25,'Ikom',9,78),(26,'Obanliku',9,81),(25,'Obubra',9,82),(26,'Obudu',9,81),(27,'Odukpani',9,80),(26,'Ogoja',9,83),(25,'Yakurr',9,76),
            (26,'Yala',9,83),(29,'Aniocha - south',10,84),(29,'Aniocha north',10,84),(30,'Bomadi',10,85),(30,'Burutu',10,91),(28,'Ethiope  east',10,86),
            (28,'Ethiope  west',10,86),(29,'Ika - south',10,87),(29,'Ika north- east',10,87),(30,'Isoko north',10,88),(30,'Isoko south',10,88),(29,'Nkokwa east',10,89),
            (29,'Ndokwa west',10,89),(28,'Okpe',10,90),(29,'Oshimili - north',10,84),(29,'Oshimili - south',10,84),(30,'Patani',10,85),(28,'Sapele',10,90),
            (28,'Udu',10,92),(28,'Ughelli north',10,92),(28,'Ughelli south',10,92),(29,'Ukwuani',10,89),(28,'Uvwie',10,90),(30,'Warri  north',10,93),
            (30,'Warri south',10,93),(30,'Warri south  west',10,93),(33,'Abakaliki',11,95),(31,'Afikpo  south',11,99),(31,'Afikpo north',11,99),(33,'Ebonyi',11,94),
            (32,'Ezza north',11,96),(32,'Ezza south',11,97),(32,'Ikwo',11,97),(32,'Ishielu',11,96),(31,'Ivo',11,98),(33,'Izzi',11,95),(31,'Ohaozara',11,98),
            (33,'Ohaukwu',11,94),(31,'Onicha',11,98),(36,'Akoko edo',12,100),(34,'Egor',12,104),(35,'Esan central',12,101),(35,'Esan north east',12,102),
            (35,'Esan south east',12,102),(35,'Esan South',12,101),(36,'Etsako  west',12,103),(36,'Etsako central',12,103),(36,'Etsako east',12,103),
            (35,'Igueben',12,101),(34,'Ikpoba/okha',12,104),(34,'Oredo',12,105),(34,'Orhionmwon',12,106),(34,'Ovia north east',12,107),(34,'Ovia south west',12,107),
            (36,'Owan east',12,108),(36,'Owan west',12,108),(34,'Uhunmwode',12,106),(38,'Ado ekiti',13,109),(38,'Efon',13,113),(37,'Ekiti east',13,111),
            (37,'Ekiti south west',13,110),(38,'Ekiti west',13,113),(37,'Emure',13,111),(37,'Gbonyin',13,111),(39,'Ido-Osi',13,112),(38,'Ijero',13,113),
            (37,'Ikere',13,110),(39,'Ikole',13,114),(39,'Ilejemeje',13,112),(38,'Irepodun/ifelodun',13,110),(37,'Ise/Orun',13,110),(39,'Moba',13,112),
            (39,'Oye',13,114),(42,'Aninri',14,115),(42,'Awgu',14,115),(41,'Enugu east',14,116),(41,'Enugu north',14,117),(41,'Enugu south',14,117),
            (42,'Ezeagu',14,118),(40,'Igbo etiti',14,119),(40,'Igbo eze north',14,120),(40,'Igbo eze south',14,122),(41,'Isi uzo',14,116),(41,'Nkanu east',14,121),
            (41,'Nkanu west',14,121),(40,'Nsukka',14,122),(42,'Oji-river',14,115),(40,'Udenu',14,120),(42,'Udi',14,118),(40,'Uzo-uwani',14,119),
            (44,'Akko',16,123),(46,'Balanga',16,125),(46,'Billiri',16,125),(45,'Dukku',16,128),(45,'Funakaye',16,127),(45,'Gombe',16,127),(46,'Kaltungo',16,126),
            (45,'Kwami',16,127),(45,'Nafada',16,128),(46,'Shongom',16,126),(44,'Yalmaltu-Deba',16,124),(47,'Aboh mbaise',17,135),(47,'Ahiazu mbaise',17,136),
            (48,'Ehime mbano',17,129),(47,'Ezinihitte mbaise',17,136),(49,'Ideato north',17,131),(49,'Ideato south',17,131),(48,'Ihitte/uboma (isinweke)',17,129),
            (47,'Ikeduru (iho)',17,137),(48,'Isiala mbano (umuelemai)',17,130),(49,'Isu (umundugba)',17,132),(47,'Mbaitoli (nwaorieubi)',17,137),
            (47,'Ngor okpala (umuneke)',17,135),(49,'Njaba (nnenasa)',17,132),(49,'Nkwerre',17,132),(49,'Nwangele (onu-nwangele amaigbo)',17,132),
            (48,'Obowo (otoko)',17,129),(49,'Oguta (oguta)',17,133),(49,'Ohaji/egbema (mmahu-egbema)',17,133),(48,'Okigwe(okigwe)',17,130),(48,'Onuimo (okwe)',17,130),
            (49,'Orlu',17,134),(49,'Orsu (awo idemili)',17,134),(49,'Oru west (mgbidi)',17,133),(49,'Oru East',17,134),(47,'Owerri north (orie uratta)',17,138),
            (47,'Owerri urban',17,138),(47,'Owerri west (umuguma)',17,138),(51,'Auyo',18,139),(50,'Babura',18,139),(52,'Birnin kudu',18,140),(51,'Birniwa',18,141),
            (52,'Buji',18,140),(52,'Dutse',18,142),(50,'Gagarawa',18,144),(50,'Garki',18,139),(50,'Gumel',18,144),(51,'Guri',18,141),(52,'Gwaram',18,143),
            (50,'Gwiwa',18,148),(51,'Hadejia',18,145),(52,'Jahun',18,146),(51,'Kafin hausa',18,145),(51,'Kaugama',18,147),(50,'Kazaure',18,148),(51,'Kirika samma',18,141),
            (52,'Kiyawa',18,142),(50,'Maigatari',1,144),(51,'Malam madori',18,147),(52,'Miga',18,146),(50,'Ringim',18,149),(50,'Roni',18,148),(50,'Sule-tankarkar',18,144),
            (50,'Taura',18,149),(50,'Yankwashi',18,148),(53,'Birnin gwari',19,160),(53,'Chikun',19,158),(53,'Giwa',19,160),(53,'Igabi',19,153),(54,'Ikara',19,154),
            (55,'Jaba',19,165),(55,'Jema\'a',19,159),(55,'Kachia',19,157),(53,'Kaduna north',19,150),(53,'Kaduna south',19,162),(55,'Kagarko',19,157),(53,'Kajuru',19,158),
            (55,'Kaura',19,163),(55,'Kauru',19,164),(54,'Kubau',19,154),(54,'Kudan',19,155),(54,'Lere',19,156),(54,'Makarfi',19,155),(54,'Sabon gari',19,161),
            (55,'Sanga',19,159),(54,'Soba',19,152),(55,'Zangon kataf',19,165),(54,'Zaria',19,151),(56,'Ajingi',20,166),(56,'Albasu',20,166),(58,'Bagwai',20,167),
            (56,'Bebeji',20,168),(58,'Bichi',20,169),(56,'Bunkure',20,170),(57,'Dala',20,171),(58,'Danbata',20,173),(57,'Dawaki kudu',20,174),(58,'Dawaki tofa',20,175),
            (56,'Doguwa',20,176),(57,'Fagge',20,185),(58,'Gabasawa',20,177),(56,'Garko',20,189),(57,'Garun malam',20,183),(56,'Gaya',20,166),(57,'Gezawa',20,177),
            (57,'Gwale',20,172),(58,'Gwarzo',20,178),(58,'IKabo',20,178),(57,'Kano municipal',20,179),(58,'Karaye',20,181),(56,'Kibiya',20,170),(56,'Kiru',20,168),
            (57,'Kumbotso',20,182),(58,'Kunchi',20,188),(57,'Kura',20,183),(57,'Madobi',20,183),(58,'Makoda',20,173),(57,'Minjibir',20,187),(57,'Nasarawa',20,184),
            (56,'Rano',20,170),(58,'Rimin gado',20,175),(56,'Rogo',20,181),(58,'Shanono',20,167),(56,'Sumaila',20,186),(56,'Takai',20,186),(57,'Tarauni',20,180),
            (58,'Tofa',20,175),(58,'Tsanyawa',20,188),(56,'Tudun wada',20,176),(57,'Ungogo',20,187),(57,'Warawa',20,174),(56,'Wudil',20,189),(61,'Bakori',21,190),
            (59,'Batagarawa',21,191),(59,'Batsari',21,192),(60,'Baure',21,204),(60,'Bindawa',21,193),(59,'Charanchi',21,191),(59,'Dan musa',21,192),
            (61,'Dandume',21,197),(61,'Danja',21,190),(60,'Daura',21,194),(60,'Dutsi',21,202),(59,'Dutsin-ma',21,195),(61,'Faskari',21,196),(61,'Funtua',21,197),
            (60,'Ingawa',21,198),(59,'Jibia',21,198),(61,'Kafur',21,200),(59,'Kaita',21,198),(61,'Kankara',21,196),(60,'Kankia',21,198),(59,'Katsina',21,201),
            (59,'Kurfi',21,195),(60,'Kusada',21,198),(60,'Mai\'adua',21,194),(61,'Malufashi',21,200),(60,'Mani',21,193),(60,'Mashi',21,202),(61,'Matazu',21,203),
            (61,'Musawa',21,203),(59,'Rimi',21,191),(61,'Sabuwa',21,196),(59,'Safana',21,192),(60,'Sandamu',21,194),(60,'Zango',21,204),(62,'Aliero',22,209),
            (63,'Arewa',22,205),(63,'Argungu',22,206),(63,'Augie',22,206),(63,'Bagudo',22,207),(62,'Birnin kebbi',22,208),(62,'Bunza',22,208),(63,'Dandi',22,205),
            (64,'Fakai',22,211),(62,'Gwandu',22,209),(63,'Jega',22,209),(62,'Kalgo',22,208),(62,'Koko/besse',22,210),(62,'Maiyama',22,210),(64,'Ngaski',22,212),
            (64,'Sakaba',22,211),(64,'Shanga',22,212),(63,'Suru',22,207),(64,'Wasagu/danko',22,211),(64,'Yauri',22,212),(64,'Zuru',22,211),(65,'Adavi',23,213),
            (65,'Ajaokuta',23,218),(66,'Ankpa',23,214),(66,'Bassa',23,215),(66,'Dekina',23,215),(66,'Ibaji',23,216),(66,'Idah',23,216),(66,'Igalamela/odolu',23,216),
            (67,'Ijumu',23,217),(67,'Kabba/bunu',23,217),(479,'Kogi k.k',23,219),(67,'Lokoja',23,219),(67,'Mopa moro',23,221),(66,'Ofu',23,216),(65,'Ogori mangogo',23,220),
            (65,'Okehi',23,213),(65,'Okene',23,220),(66,'Olamaboro',23,214),(66,'Omala',23,214),(67,'Yagba east',23,221),(67,'Yagba west',23,221),(68,'Asa',24,226),
            (69,'Baruten',24,222),(69,'Edu',24,223),(70,'Ekiti',24,224),(70,'Ifelodun',24,227),(68,'Ilorin east',24,225),(68,'Ilorin-south',24,225),
            (68,'Ilorin-west',24,226),(70,'Irepodun',24,224),(70,'Isin',24,224),(69,'Kaiama',24,222),(69,'Moro',24,223),(68,'Offa',24,227),(70,'Oke-ero',24,224),
            (70,'Oyun',24,227),(69,'Patigi',24,223),(71,'Agege',25,228),(71,'Ajeromi/ifelodun',25,245),(71,'Alimosho',25,230),(71,'Amuwo-odofin',25,244),
            (72,'Apapa',25,235),(71,'Badagry',25,231),(73,'Epe',25,232),(72,'Eti-osa',25,234),(73,'Ibeju/lekki',25,233),(71,'Ifako-ijaye',25,229),(71,'Ikeja',25,236),
            (73,'Ikorodu',25,237),(73,'Kosofe',25,249),(72,'Lagos island',25,238),(72,'Lagos mainland',25,240),(71,'Mushin',25,241),(71,'Ojo',25,243),
            (71,'Oshodi/isolo',25,246),(73,'Shomolu',25,248),(72,'Surulere',25,250),(75,'Akwanga',26,252),(74,'Awe',26,253),(74,'Doma',26,253),(76,'Karu',26,254),
            (74,'Keana',26,253),(76,'Keffi',26,254),(76,'Kokona',26,254),(74,'Lafia',26,255),(76,'Nasarawa',26,256),(75,'Nasarawa eggon',26,252),(74,'Obi',26,255),
            (76,'Toto',26,256),(75,'Wamba',26,252),(79,'Agaie',27,257),(78,'Agwara',27,258),(79,'Bida',27,259),(78,'Borgu',27,258),(77,'Bosso',27,260),
            (77,'Chanchaga',27,261),(79,'Edatti',27,263),(79,'Gbako',27,259),(77,'Gurara',27,262),(79,'Katcha',27,259),(78,'Kontagora',27,265),(79,'Lapai',27,257),
            (79,'Lavun',27,263),(78,'Magama',27,264),(78,'Mariga',27,265),(78,'Mashegu',27,265),(79,'Mokwa',27,263),(77,'Munya',27,266),(77,'Paikoro',27,260),
            (77,'Rafi',27,266),(78,'Rijau',27,264),(77,'Shiroro',27,266),(77,'Suleja',27,262),(77,'Tapa',27,262),(78,'Wushishi',27,265),(80,'Abeokuta north',28,267),
            (80,'Abeokuta south',28,268),(82,'Ado odo-ota',28,269),(82,'Egbado north',28,270),(82,'Egbado south',28,271),(80,'Ewekoro',28,272),(80,'Ifo',28,272),
            (81,'Ijebu east',28,273),(81,'Ijebu north',28,273),(81,'Ijebu north east',28,274),(81,'Ijebu ode',28,274),(81,'Ikenne',28,275),(82,'Imeko/afon',28,270),
            (82,'Ipokia',28,271),(80,'Obafemi/owode',28,267),(80,'Odeda',28,267),(81,'Odogbolu',28,274),(81,'Ogun water side',28,273),(81,'Remo north',28,275),
            (81,'Shagamu',28,275),(84,'Akoko north east',29,276),(84,'Akoko north west',29,276),(84,'Akoko south east',29,277),(84,'Akoko south west',29,277),
            (83,'Akure north',29,278),(83,'Akure south',29,278),(85,'Ese-odo',29,282),(83,'Idanre',29,279),(83,'Ifedore',29,279),(85,'Ilaje',29,282),
            (85,'Ileoluji/okeigbo',29,280),(85,'Irele',29,281),(85,'Odigbo',29,280),(85,'Okitipupa',29,281),(83,'Ondo east',29,283),(83,'Ondo west',29,283),
            (84,'Ose',29,284),(84,'Owo',29,284),(87,'Atakumosa east',30,288),(87,'Atakumosa west',30,288),(88,'Ayedaade',30,292),(88,'Ayedire',30,291),
            (86,'Boluwaduro',30,287),(86,'Boripe',30,286),(88,'Ede north',30,293),(88,'Ede south',30,293),(88,'Egbedore',30,293),(88,'Ejigbo',30,293),
            (87,'Ife central',30,290),(87,'Ife east',30,290),(87,'Ife north',30,290),(87,'Ife south',30,290),(86,'Ifedayo',30,287),(86,'Ifelodun',30,286),
            (86,'Ila',30,287),(87,'Ilesa east',30,288),(87,'Ilesa west',30,288),(86,'Irepodun',30,285),(88,'Irewole',30,292),(88,'Isokan',30,292),(88,'Iwo',30,291),
            (87,'Obokun',30,289),(86,'Odo-otin',30,286),(88,'Ola-oluwa',30,291),(86,'Olorunda',30,285),(87,'Oriade',30,289),(86,'Orolu',30,285),(86,'Osogbo',30,285),
            (89,'Afijio',31,294),(89,'Akinyele',31,295),(89,'Atiba',31,294),(90,'Atisbo',31,299),(89,'Egbeda',31,296),(91,'Ibadan north',31,307),
            (91,'Ibadan north east',31,305),(91,'Ibadan north west',31,306),(91,'Ibadan south west',31,306),(91,'Ibadan south-east',31,305),(91,'Ibarapa central',31,297),
            (91,'Ibarapa east',31,297),(91,'Ibarapa north',31,297),(91,'Ido',31,297),(90,'Irepo',31,300),(90,'Iseyin',31,301),(90,'Itesiwaju',31,301),(90,'Iwajowa',31,301),
            (90,'Kajola',31,301),(89,'Lagelu',31,295),(90,'Ogbomoso north',31,302),(90,'Ogbomoso south',31,302),(89,'Ogo-oluwa',31,303),(90,'Olorunsogo',31,300),
            (89,'Oluyole',31,304),(89,'Ona-ara',31,296),(90,'Oorelope',31,300),(90,'Ori ire',31,302),(89,'Oyo east',31,294),(89,'Oyo west',31,294),
            (90,'Saki east',31,299),(90,'Saki west',31,299),(89,'Surulere',31,303),(93,'Barikin ladi',32,310),(93,'Bassa',32,308),(92,'Bokkos',32,311),
            (93,'Jos east',32,309),(93,'Jos north',32,308),(93,'Jos south',32,309),(92,'Kanam',32,312),(92,'Kanke',32,312),(94,'Langtang north',32,314),
            (94,'Langtang south',32,314),(92,'Mangu',32,311),(94,'Mikang',32,315),(92,'Pankshin',32,312),(94,'Qua\'an pan',32,315),(93,'Riyom',32,310),
            (94,'Shendam',32,315),(94,'Wase',32,313),(97,'Abua-odual',33,316),(97,'Ahoada east',33,316),(97,'Ahoada west',33,317),(97,'Akuku toru',33,319),
            (96,'Andoni',33,321),(97,'Asari-toru',33,319),(97,'Bonny',33,318),(97,'Degema',33,318),(96,'Eleme',33,322),(95,'Emohua',33,324),(95,'Etche',33,325),
            (96,'Gokana',33,323),(95,'Ikwerre',33,324),(96,'Khana',33,323),(95,'Obio/akpor',33,326),(97,'Ogba/egbema/ndoni',33,317),(95,'Ogu/bolo',33,320),
            (95,'Okrika',33,320),(95,'Omuma',33,325),(96,'Opobo/nekoro',33,321),(96,'Oyigbo',33,322),(95,'Port harcourt',33,327),(96,'Tai',33,322),
            (99,'Binji',34,334),(100,'Bodinga',34,337),(100,'Dange/shuni',34,337),(98,'Gada',34,330),(98,'Goronyo',34,330),(99,'Gudu',34,333),
            (98,'Gwadabawa',34,332),(98,'Illela',34,332),(98,'Isa',34,329),(100,'Kebbe',34,339),(99,'Kware',34,335),(98,'Rabah',34,331),
            (98,'S/birni',34,329),(100,'Shagari',34,338),(99,'Silame',34,334),(99,'Sokoto north',34,336),(99,'Sokoto south',34,336),(100,'Tambuwal',34,339),
            (99,'Tangaza',34,333),(100,'Tureta',34,337),(99,'Wamakko',34,335),(98,'Wurno',34,331),(100,'Yabo',34,338),(102,'Ardo - kola',35,345),
            (101,'Bali',35,340),(103,'Donga',35,341),(101,'Gashaka',35,342),(101,'Gassol',35,340),(103,'Ibi',35,343),(102,'Jalingo',35,344),
            (102,'Karim-lamido',35,345),(101,'Kurmi',35,342),(102,'Lau',35,345),(101,'Sardauna',35,342),(103,'Takum',35,341),(103,'Ussa',35,341),
            (103,'Wukari',35,343),(102,'Yorro',35,344),(102,'Zing',35,344),(105,'Bade',36,346),(104,'Bursari',36,347),(106,'Damaturu',36,348)
            ,(106,'Fika',36,349),(106,'Fune',36,349),(104,'Geidam',36,347),(104,'Gujba',36,348),(104,'Gulani',36,348),(105,'Jakusko',36,346),
            (105,'Karasawa',36,350),(105,'Machina',36,350),(106,'Nangere',36,351),(105,'Nguru',36,350),(106,'Potiskum',36,351),(104,'Tarmuwa',36,348),
            (104,'Yunusari',36,347),(105,'Yusufari',36,350),(109,'Anka',37,356),(109,'Bakura',37,357),(108,'Birnin magaji',37,352),(109,'Bukkuyum',37,358),
            (107,'Bungudu',37,355),(109,'Gummi',37,358),(107,'Gusau',37,354),(108,'Kaura namoda',3,352),(109,'Maradun',37,357),(107,'Maru',37,355),
            (108,'Shinkafi',37,353),(108,'Talata mafara',37,356),(107,'Tsafe',37,354),(108,'Zurmi',37,353),(43,'Abaji',15,357),(43,'Bwari',15,358),
            (43,'Gwagwalada',15,357),(43,'Kuje',15,357),(43,'Kwali',15,357),(43,'Municipal',15,358)]
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
        data = [('Aba N/S',1),('Arochukwu/Ohafia',1),('Bende',1),('Nsiala Ngwa N/S',1),('Isuikwuato/Umu-Nneochi',1),('Obingwa/Ugwunagbo/Osisioma',1),
        ('Umuahia(N/S)/Ikwuano',1),('Ukwa E/W',1),('Demsa/Numan/Lamurde',2),('Furore/Song',2),('Mayo Belwa/Ganye/Jada/Toungo',2),('Gombi/Hong',2),
        ('Guyuk/Shelleng',2),('Madagali/Michika',2),('Maiha/Mubi(N/S)',2),('Yola(N/S)/Girei',2),('Abak/Etim Ekpo/Ika',3),('Eket/Onna/Esit Eket/Ibeno',3),
        ('Etinan/Nsit Ibom/Nsit Ubium',3),('Ikono/Ini',3),('Ikot Absai/Mkpat Enin/Eastern Obolo',3),('Ikot Ekpene/Essien Udim/Obot Akara',3),('Itu/Ibiono Ibom',3),
        ('Oron/Mbo/Okobo/Udung Uko/Urue Offong/Uruko',3),('Ukanafun/Oruk Anam',3),('Uyo/Uruan/Nsit Atai/Ibesikpo Asutan',3),('Anambra(E/W)',4),('Onitcha(N/S)',4),
        ('Ogbaru',4),('Aguata',4),('Oyi/Ayamelum',4),('Awka(N/S)',4),('Nijikoka/Dunukofia/Anaocha',4),('Idemili(N/S)',4),('Ihiala',4),('Nnewi(N/S)/Ekwusigo',4),
        ('Orumba(N/S)',4),('Alkaleri/Kirfi',5),('Bauchi',5),('Bogoro/Dass/Tafawa Balewa',5),('Toro',5),('Ningi/Warji',5),('Darazo/Gunjuwa',5),('Misau/Dambam',5),
        ('Zaki',5),('Gamawa',5),('Jamaare/Itas-Gadau',5),('Shira/Giade',5),('Katagum',5),('Brass/Nembe',6),('Ogbia',6),('Sagbama/Ekeremor)',6),('Southern Ijaw',6),
        ('Yenagoa/Kolokuna/Opokuma',6),('Ado/Obadigbo/Okpokwu',7),('Apa/Agatu',7),('Buruku',7),('Gboko/Tarka',7),('Guma/Makurdi',7),('Gwer East/West',7),
        ('Konshisha/Vandeikya',7),('Kwande/Ushongo',7),('Oju/Obi',7),('Otukpo/Ohimini',7),('Askira-Uba/Hawul',8),('Bama/Ngala/Kala-Balge',8),
        ('Biu/Kwaya-Kusar, Shani/Bayo',8),('Dikwa/Mafa/Konduga',8),('Damboa/Gwoza/Chibok',8),('Kaga/Gubio/Magumeri',8),('Monguno/Nganzai/Marte',8),
        ('Kukawa/Mobbar/Abadam/ Guzamali',8),('Maiduguri (Metropolitan)',8),('Jere',8),('Yakurr/Abi',9),('Akamkpa/Biase',9),('Boki/Ikom',9),
        ('Calabar South/Akpabuyo/Bakassi',9),('Calabar Municipal/Odukpani',9),('Obanliku/Obudu/Bekwarra',9),('Obubra/Etung',9),('Ogoja/Yala',9),
        ('Aniocha(N/S)/Oshimili(N/S)',10),('Bomadi/Patani',10),('Ethiope East/Ethiope West',10),('Ika North East/Ika South',10),('Isoko(N/S)',10),
        ('Nkokwa(E&S)/Ukwuani',10),('Okpe/Sapele/Uvwie)',10),('Burutu',10),('Ughelli(N/S)/Udu',10),('Warri(N/S/SE)',10),('Ebonyi/Ohaukwu',11),('Abakaliki/Izzi',11),
        ('Ezza North/Ishielu',11),('Ezza South/Ikwo',11),('Ivo-Ohaozara/Onicha',11),('Afikpo(N/S)',11),('Akoko-Edo',12),('Esan Central/Esan South/Igueben',12),
        ('Esan North East/Esan South East',12),('Etsako (E/W/C) ',12),('Egor/Ikpoba-Okha',12),('Oredo',12),('Orhionmwon/Uhunmwonde',12),('Ovia(NE/SW)',12),
        ('Owan(E/W)',12),('Ado Ekiti/Irepodun/Ifelodun',13),('Ekiti South West/Ikere/Orun/Ise',13),('Emure/Gbonyin/Ekiti East',13),('Ido/Osi, Moba/Ilejeme',13),
        ('Ijero/Ekiti West/Efon',13),('Ikole/Oye',13),('Aninri/Awgu/Oji River',14),('IEnugu East/Isi Uzo',14),('Enugu(N/S)',14),('Ezeagu/Udi',14),
        ('Igbo-Etiti/Uzo-Uwani',14),('Igbo-Eze North/Udenu',14),('Nkanu East/Nkanu West',14),('Nsukka/Igbo-Eze South',14),('Akko',16),('Yamaltu/Deba',16),
        ('Balanga/Billiri',16),('Kaltungo/Shongom',16),('Gombe/Kwami/Funakaye',16),('Dukku/Nafada',16),('Ehime Mbano/Ihite-Uboma/Obowo',17),
        ('Isiala Mbano/Okigwe/Onuimo',17),('Ideato(N/S)',17),('Isu/Njaba/Nkwerre/Nwangele',17),('Oguta/Ohaji-Egbema/Oru West',17),('Oru East/Orsu/Orlu',17),
        ('Aboh Mbaise/Ngor Okpala',17),('Ahiazu Mbaise/Ezinihitte',17),('Ikeduru/Mbaitoli',17),('Owerri Municipal/Owerri(N/W)',17),('Babura/Garki',18),
        ('Birnin Kudu/Buji',18),('Birniwa Guri/Kirikasamma',18),('Dutse/Kiyawa',18),('Gwaram',18),('Gumel/Maigatari/Sule Tankarkar/Gagarawa',18),('Hadejia/Kafin Hausa',18),
        ('Jahun/Miga',18),('Mallam Madori/Kaugama',18),('Kazaure/Roni/Gwiwa/Yankwashi',18),('Ringim/Taura',18),('Kaduna North',19),('Zaria',19),('Soba',19),
        ('Igabi',19),('Ikara/Kubau',19),('Makarfi/Kudan',19),('Lere',19),('Kachia/Kagarko',19),('Chikun/Kajuru',19),('Jemaa/Sanga',19),('Birnin Gwari/Giwa',19),
        ('Sabon Gari',19),('Kaduna South',19),('Kaura',19),('Kauru',19),('Zangon Kataf/Jaba',19),('Alabasu/Gaya/Ajingi',20),('Shanono/Bagwai',20),('Bebeji/Kiru',20),
        ('Bichi',20),('Rano/Bunkure/Kibiya',20),('Dala',20),('Gwale',20),('Dambatta/Makoda',20),('Dawakin Kudu/Warawa',20),('Dawakin Tofa/Tofa/Rimin Gado',20),
        ('Doguwa/Tudun Wada',20),('Gezawa/Gabasawa',20),('Gwarzo/Ikabo',20),('Municipal',20),('Tarauni',20),('Karaye/Rogo',20),('Kumbotso',20),
        ('Kura/Madobi/Garun Mallam',20),('Nassarawa',20),('Fagge',20),('Sumaila/Takai',20),('Minjibir/Ungogo',20),('Tsanyawa/Kunchi',20),('Wudil/Garko',20),
        ('Bakori/Danja',21),('Batagarawa/Charanchi/Rimi',21),('Batsari/Safana/Danmusa',21),('Bindawa/Mani',21),('Daura/Sandamu/Maiadua',21),('Dutsin-ma/Kurfi',21),
        ('Faskari/Kankara/Sabuwa',21),('Funtua/Dandume',21),('Ingawa/Kankia/Kusada',21),('Jibia/Kaita',21),('Malumfashi/Kafur',21),('Katsina',21),('Mashi/Dutsi',21),
        ('Matazu/Musawa',21),('Zango/Baure',21),('Arewa/Dandi',22),('Argungu/Augie',22),('Bagudo/Suru',22),('Bunza/Birnin Kebbi/Kalgo',22),('Aleiro/Gwandu/Jega',22),
        ('Koko-Besse/Maiyama',22),('Fakai/Sakaba/Wasagu/Danko/Zuru',22),('Ngaski/Shanga/Yauri',22),('Adavi/Okehi',23),('Ankpa/Omala/Olamaboro',23),('Bassa/Dekina',23),
        ('Idah/Igalamela Odolu/Ibaji/ Ofu',23),('Ijumu/Kabba-Bunu',23),('Ajaokuta',23),('Kogi (Lokoja)/Kogi (K.K.)',23),('Okene/Ogori-Magogo',23),
        ('Yagba East/Yagba West/ Mopamuro',23),('Baruten/Kaiama',24),('Edu/Moro/Pategi',24),('Ekiti/Isin/Irepodun/Oke-Ero',24),('Ilorin East/Ilorin South',24),
        ('Ilorin West/Asa',24),('Ifelodun/Offa/Oyun',24),('Agege',25),('Ifako/Ijaiye',25),('Alimosho',25),('Badagry',25),('Epe',25),('Ibeju Lekki',25),('Eti-Osa',25),
        ('Apapa',25),('Ikeja',25),('Ikorodu',25),('Lagos Island I',25),('Lagos Island II',25),('Lagos Mainland',25),('Mushin I',25),('Mushin II',25),('Ojo',25),
        ('Amuwo-Odofin',25),('Ajeromi/Ifelodun',25),('Oshodi/Isolo I',25),('Oshodi/Isolo II',25),('Shomolu',25),('Kosofe',25),('Surulere I',25),('Surulere II',25),
        ('Akwanga/Nassarawa Eggon/ Wamba',26),('Awe/Doma/Keana',26),('Keffi/Karu/Kokona',26),('Lafia/Obi',26),('Nassarawa/Toto',26),('Agaie/Lapai',27),
        ('Agwara/Borgu',27),('Bida/Gbako/Katcha',27),('Booso/Paikoro',27),('Chanchaga',27),('Gurara/Suleja/Tapa',27),('Lavun/Mokwa/Edati',27),('Magama/Rijau',27),
        ('Kontagora/Wushishi/Mariga/ Mashegu',27),('Shiroro/Rafi/Munya',27),('Abeokuta North/ Obafemi-Owode/Odeda',28),('Abeokuta South',28),('Ado-Odo/Ota',28),
        ('Egbado North/Imeko-Afon',28),('Egbado South/Ipokia',28),('Ifo/Ewekoro',28),('Ijebu North/Ijebu East/Ogun Waterside',28),
        ('Ijebu Ode /Odogbolu /Ijebu North East',28),('Ikenne/Shagamu/Remo North',28),('Akoko North East/Akoko North West',29),('Akoko South East/Akoko South West',29),
        ('Akure North/Akure South',29),('Idanre/Ifedore',29),('Ileoluji/Okeigbo/Odigbo',29),('Okitipupa/Irele',29),('Eseodo/Ilaje',29),('Ondo East/Ondo West',29),
        ('Owo/Ose',29),('Irepodun/Olorunda/Osogbo/Orolu',30),('Odo-Otin/Ifelodun/Boripe',30),('Boluwaduro/Ifedayo/Ila',30),('Atakunmosa(E&W)/Ilesha(E&W)',30),
        ('Obokun/Oriade',30),('Ife(C/N/S/E)',30),('Ayedire/Iwo/Ola-Oluwa',30),('Ayedaade/Irewole/Isokan',30),('Ede(N/S)/Egbedore/Ejigbo',30),('Afijio/Oyo(E/W)/Atiba',31),
        ('Akinyele/Lagelu',31),('Egbeda/Ona-Ara',31),('Ibarapa Central/Ibarapa North',31),('Ibarapa East/Ido',31),('Saki(E/W)/Atisbo',31),('Irepo/Orelope/Olorunsogo',31),
        ('Iseyin/Itesiwaju/Kajola/Iwajowa',31),('Ogbomoso(N/S)/Orire',31),('Ogo-Oluwa/Surulere',31),('Oluyole',31),('Ibadan NorthEast/Ibadan SouthEast',31),
        ('Ibadan South West/Ibadan North West',31),('Ibadan North',31),('Jos North/Bassa',32),('Jos South/Jos East',32),('Barkin Ladi/Riyom',32),('Bokkos/Mangu',32),
        ('Kanke/Pankshin/Kanam',32),('Wase',32),('Langtang North/Langtang South',32),('Mikang/Quaan/Pan/Shedam',32),('Abua-Odual/Ahaoda East',33),
        ('Ahoada West/Ogba Egbema',33),('Degema/Bonny',33),('Akuku-Toru/Asari-Toru',33),('Okrika/Ogu-Bolo',33),('Opobo/Nkoro/Andoni',33),('Eleme/Tai/Oyigbo',33),
        ('Khana/Gokana',33),('Ikwerre/Umohua',33),('Etche/Omuma',33),('Obio Akpor',33),('Port Harcourt I',33),('Port Harcourt II',33),('Isa/Sabon Birni',34),
        ('Goronyo/Gada',34),('Wurno/Rabah',34),('Illela/Gwadabawa',34),('Tangaza/Gudu',34),('Binji/Silame',34),('Kware/Wamakko',34),('Sokoto North/Sokoto South',34),
        ('Dange-Shuni/Bodinga/Tureta',34),('Yabo/Shagari',34),('Kebbe/Tambuwal',34),('Bali/Gassol',35),('Takum/Donga/Ussa',35),('Sardauna/Kurmi/Gashaka',35),
        ('Ibi/Wukari',35),('Jalingo/Yorro/Zing',35),('Karim Lamido/Lau/Ardo-Kola',35),('Bade/Jakusko',36),('Bursari/Geidam/Yunusari',36),
        ('Damaturu/Gujba/Gulani/ Tarmuwa',36),('Fika/Fune',36),('Machina/Nguru/Yusufari/ Karasuwa',36),('Nangere/Potiskm',36),('Kaura-Namoda/Birnin Magaji',37),
        ('Shinkafi/Zurmi',37),('Gusau/Tsafe',37),('Bungudu/Maru',37),('Anka/Talata Mafara',37),('Bakura/Maradun',37),('Gummi/Bukkuyum',37),
        ('Abaji/Gwagwalada/Kwali/Kuje',15),('Municipal/Bwari',15)]
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
        data =  [('Accord', 'A', "media/party_pictures/A.jpg"),('Action Alliance', 'AA', "media/party_pictures/AA.jpg"),
        ('Action Democratic Party', 'ADP', "media/party_pictures/ADP.png"),('Action Peoples Party','APP', 'media/party_pictures/APP.png'),
        ('African Action Congress','AAC', 'media/party_pictures/AAC.jpg'),('African Democratic Congress', 'ADC', 'media/party_pictures/ADC.jpg'),
        ('All Progressives Congress','APC', 'media/party_pictures/apclogo.jpg'),('All Progressives Grand Alliance','APGA', 'media/party_pictures/APGA.jpg'),
        ('Allied Peoples Movement', 'APM', 'media/party_pictures/APM.jpg'),('Boot Party', 'BP', 'media/party_pictures/BootParty.jpg'),
        ('Labour Party', 'LP','media/party_pictures/LP.jpg'),('National Rescue Movement', 'NRM', 'media/party_pictures/NRM.png'),
        ('New Nigeria Peoples Party', 'NNPP', 'media/party_pictures/NNPP.jpg'),('Peoples Democratic Party', 'PDP', 'media/party_pictures/PDP.jpg'),
        ('Peoples Redemption Party', 'PRP', 'media/party_pictures/PRP.png'),('Social Democratic Party', 'SDP', 'media/party_pictures/SDP.png'),
        ('Young Progressive Party', 'YPP', 'media/party_pictures/YPP-Logo.jpeg'),('Zenith Labour Party', 'ZLP', 'media/party_pictures/ZLP.jpg')]
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
