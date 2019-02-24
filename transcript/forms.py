from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import (StringField, SelectField, TextAreaField, SubmitField, BooleanField, 
                    TextField, PasswordField, SelectMultipleField)
from wtforms.widgets import ListWidget, CheckboxInput
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from transcript.models import User, Post

class MultiCheckboxField(SelectMultipleField):
    widget			= ListWidget(prefix_label=False)
    option_widget	= CheckboxInput()


class AlumniForm(FlaskForm):
    surname = StringField('Surname', validators=[DataRequired(), Length(min=2, max=100)])
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=100)])
    middle_name = StringField('Middle Name', validators=[DataRequired(), Length(min=2, max=100)])
    maiden = StringField('Maiden Name', validators=[DataRequired(), Length(min=2, max=100)])
    dob = StringField('Date of Birth', validators=[DataRequired()])
    gender = SelectField(u'Gender', choices=[('f', 'Female'), ('m', 'Male')])
    nationality = SelectField(u'Nationality', choices=[(1, 'Nigerian'), (2, 'Non-Nigerian')])
    country = StringField('Country', validators=[DataRequired(), Length(min=2, max=500)])
    state_of_origin = SelectField(u'State of Origin', choices=[
                                    ('Abia', 'Abia'),
                                    ('Adamawa', 'Adamawa'),
                                    ('Akwa Ibom', 'Akwa Ibom'),
                                    ('Anambra', 'Anambra'),
                                    ('Bauchi', 'Bauchi'),
                                    ('Bayelsa', 'Bayelsa'),
                                    ('Benue', 'Benue'),
                                    ('Borno', 'Borno'),
                                    ('Cross River', 'Cross River'),
                                    ('Delta', 'Delta'),
                                    ('Ebonyi', 'Ebonyi'),
                                    ('Edo', 'Edo'),
                                    ('Ekiti', 'Ekiti'),
                                    ('Enugu', 'Enugu'),
                                    ('Gombe', 'Gombe'),
                                    ('Imo', 'Imo'),
                                    ('Jigawa', 'Jigawa'),
                                    ('Kaduna', 'Kaduna'),
                                    ('Kano', 'Kano'),
                                    ('Katsina', 'Katsina'),
                                    ('Kebbi', 'Kebbi'),
                                    ('Kogi', 'Kogi'),
                                    ('Kwara', 'Kwara'),
                                    ('Lagos', 'Lagos'),
                                    ('Nasarawa', 'Nasarawa'),
                                    ('Niger', 'Niger'),
                                    ('Ogun', 'Ogun'),
                                    ('Ondo', 'Ondo'),
                                    ('Osun', 'Osun'),
                                    ('Oyo', 'Oyo'),
                                    ('Plateau', 'Plateau'),
                                    ('Rivers', 'Rivers'),
                                    ('Sokoto', 'Sokoto'),
                                    ('Taraba', 'Taraba'),
                                    ('Yobe', 'Yobe'),
                                    ('Zamfara', 'Zamfara')
                                    ])
    lga = SelectField(u'LGA', choices=[
                    #local governments in abia state#
                    ('Select item...', 'Select item...'), ('Aba North', 'Aba North'), ('Aba South', 'Aba South'), 
                    ('Arochukwu', 'Arochukwu'), ('Bende', 'Bende'), ('Ikwuano', 'Ikwuano'), ('Isiala Ngwa North', 'Isiala Ngwa North'), 
                    ('Isiala Ngwa South', 'Isiala Ngwa South'), ('Isuikwuato', 'Isuikwuato'), ('Obi Ngwa', 'Obi Ngwa'), 
                    ('Ohafia', 'Ohafia'), ('Osisioma', 'Osisioma'), ('Ugwunagbo', 'Ugwunagbo'), ('Ukwa East', 'Ukwa East'), 
                    ('Ukwa West', 'Ukwa West'), ('Umuahia North', 'Umuahia North'), ('muahia South', 'muahia South'), 
                    ('Umu Nneochi', 'Umu Nneochi'),
                    #local governments in adamawa state#
                    ('Demsa', 'Demsa'), ('Fufure', 'Fufure'), ('Ganye', 'Ganye'), ('Gayuk', 'Gayuk'), ('Gombi', 'Gombi'), 
                    ('Grie', 'Grie'), ('Hong', 'Hong'), ('Jada', 'Jada'), ('Larmurde', 'Larmurde'), ('Madagali', 'Madagali'), 
                    ('Maiha', 'Maiha'), ('Mayo Belwa', 'Mayo Belwa'), ('Michika', 'Michika'), ('Mubi North', 'Mubi North'), 
                    ('Mubi South', 'Mubi South'), ('Numan', 'Numan'), ('Shelleng', 'Shelleng'), ('Song', 'Song'), 
                    ('Toungo', 'Toungo'), ('Yola North', 'Yola North'), ('Yola South', 'Yola South'),
                    #local governments in akwa ibom state#
                    ('Abak', 'Abak'), ('Eastern Obolo', 'Eastern Obolo'), ('Eket', 'Eket'), ('Esit Eket', 'Esit Eket'), 
                    ('Essien Udim', 'Essien Udim'), ('Etim Ekpo', 'Etim Ekpo'), ('Etinan', 'Etinan'), ('Ibeno', 'Ibeno'), 
                    ('Ibesikpo Asutan', 'Ibesikpo Asutan'), ('Ibiono-Ibom', 'Ibiono-Ibom'), ('Ika', 'Ika'), ('Ikono', 'Ikono'), 
                    ('Ikot Abasi', 'Ikot Abasi'), ('Ikot Ekpene', 'Ikot Ekpene'), ('Ini', 'Ini'), ('Itu', 'Itu'), ('Mbo', 'Mbo'), 
                    ('Mkpat-Enin', 'Mkpat-Enin'), ('Nsit-Atai', 'Nsit-Atai'), ('Nsit-Ibom', 'Nsit-Ibom'), ('Nsit-Ubium', 'Nsit-Ubium'), 
                    ('Obot Akara', 'Obot Akara'), ('Okobo', 'Okobo'), ('Onna', 'Onna'), ('Oron', 'Oron'), ('Oruk Anam', 'Oruk Anam'), 
                    ('Udung-Uko', 'Udung-Uko'), ('Ukanafun', 'Ukanafun'), ('Uruan', 'Uruan'), ('Urue-Offong Oruko', 'Urue-Offong Oruko'), ('Uyo', 'Uyo'),
                    #local governments in anambra state#
                    ('Aguata', 'Aguata'), ('Anambra East', 'Anambra East'), ('Anambra West', 'Anambra West'), ('Anaocha', 'Anaocha'), 
                    ('Awka North', 'Awka North'), ('Awka South', 'Awka South'), ('Ayamelum', 'Ayamelum'), ('Dunukofia', 'Dunukofia'), 
                    ('Ekwusigo', 'Ekwusigo'), ('Idemili North', 'Idemili North'), ('Idemili South', 'Idemili South'), ('Ihiala', 'Ihiala'), 
                    ('Njikoka', 'Njikoka'), ('Nnewi North', 'Nnewi North'), ('Nnewi South', 'Nnewi South'), ('Ogbaru', 'Ogbaru'), 
                    ('Onitsha North', 'Onitsha North'), ('Onitsha South', 'Onitsha South'), ('Orumba North', 'Orumba North'), 
                    ('Orumba South', 'Orumba South'), ('Oyi', 'Oyi'),
                    #local governments in bauchi state#
                    ('Alkaleri', 'Alkaleri'), ('Bauchi', 'Bauchi'), ('Bogoro', 'Bogoro'), ('Damban', 'Damban'), ('Darazo', 'Darazo'), 
                    ('Dass', 'Dass'), ('Gamawa', 'Gamawa'), ('Ganjuwa', 'Ganjuwa'), ('Giade', 'Giade'), ('Itas-Gadau', 'Itas-Gadau'), 
                    ('Jama are', 'Jama are'), ('Katagum', 'Katagum'), ('Kirfi', 'Kirfi'), ('Misau', 'Misau'), ('Ningi', 'Ningi'), 
                    ('Shira', 'Shira'), ('Tafawa Balewa', 'Tafawa Balewa'), ('Toro', 'Toro'), ('Warji', 'Warji'), ('Zaki', 'Zaki'),
                    #local governments in bayelsa state#
                    ('Brass', 'Brass'), ('Ekeremor', 'Ekeremor'), ('Kolokuma Opokuma', 'Kolokuma Opokuma'), ('Nembe', 'Nembe'), 
                    ('Ogbia', 'Ogbia'), ('Sagbama', 'Sagbama'), ('Southern Ijaw', 'Southern Ijaw'), ('Yenagoa', 'Yenagoa'),
                    #local governments in benue state#
                    ('Agatu', 'Agatu'), ('Apa', 'Apa'), ('Ado', 'Ado'), ('Buruku', 'Buruku'), ('Gboko', 'Gboko'), ('Guma', 'Guma'), 
                    ('Gwer East', 'Gwer East'), ('Gwer West', 'Gwer West'), ('Katsina-Ala', 'Katsina-Ala'), ('Konshisha', 'Konshisha'), 
                    ('Kwande', 'Kwande'), ('Logo', 'Logo'), ('Makurdi', 'Makurdi'), ('Obi', 'Obi'), ('Ogbadibo', 'Ogbadibo'), ('Ohimini', 'Ohimini'), 
                    ('Oju', 'Oju'), ('Okpokwu', 'Okpokwu'), ('Oturkpo', 'Oturkpo'), ('Tarka', 'Tarka'), ('Ukum', 'Ukum'), ('Ushongo', 'Ushongo'), 
                    ('Vandeikya', 'Vandeikya'),
                    #local governments in borno state#
                    ('Abadam', 'Abadam'), ('Askira-Uba', 'Askira-Uba'), ('Bama', 'Bama'), ('Bayo', 'Bayo'), ('Biu', 'Biu'), ('Chibok', 'Chibok'), 
                    ('Damboa', 'Damboa'), ('Dikwa', 'Dikwa'), ('Gubio', 'Gubio'), ('Guzamala', 'Guzamala'), ('Gwoza', 'Gwoza'), ('Hawul', 'Hawul'), 
                    ('Jere', 'Jere'), ('Kaga', 'Kaga'), ('Kala-Balge', 'Kala-Balge'), ('Konduga', 'Konduga'), ('Kukawa', 'Kukawa'), 
                    ('Kwaya Kusar', 'Kwaya Kusar'), ('Mafa', 'Mafa'), ('Magumeri', 'Magumeri'), ('Maiduguri', 'Maiduguri'), ('Marte', 'Marte'), 
                    ('Mobbar', 'Mobbar'), ('Monguno', 'Monguno'), ('Ngala', 'Ngala'), ('Nganzai', 'Nganzai'), ('Shani', 'Shani'),
                    #local governments in cross river state#
                    ('Abi', 'Abi'), ('Akamkpa', 'Akamkpa'), ('Akpabuyo', 'Akpabuyo'), ('Bakassi', 'Bakassi'), ('Bekwarra', 'Bekwarra'), 
                    ('Biase', 'Biase'), ('Boki', 'Boki'), ('Calabar Municipal', 'Calabar Municipal'), ('Calabar South', 'Calabar South'), 
                    ('Etung', 'Etung'), ('Ikom', 'Ikom'), ('Obanliku', 'Obanliku'), ('Obubra', 'Obubra'), ('Obudu', 'Obudu'), 
                    ('Odukpani', 'Odukpani'), ('Ogoja', 'Ogoja'), ('Yakuur', 'Yakuur'), ('Yala', 'Yala'),
                    #local governments in delta state#
                    ('Aniocha North', 'Aniocha North'), ('Aniocha South', 'Aniocha South'), ('Bomadi', 'Bomadi'), ('Burutu', 'Burutu'), 
                    ('Ethiope East', 'Ethiope East'), ('Ethiope West', 'Ethiope West'), ('Ika North East', 'Ika North East'), 
                    ('Ika South', 'Ika South'), ('Isoko North', 'Isoko North'), ('Isoko South', 'Isoko South'), ('Ndokwa East', 'Ndokwa East'), 
                    ('Ndokwa West', 'Ndokwa West'), ('Okpe', 'Okpe'), ('Oshimili North', 'Oshimili North'), ('Oshimili South', 'Oshimili South'), 
                    ('Patani', 'Patani'), ('Sapele', 'Sapele'), ('Udu', 'Udu'), ('Ughelli North', 'Ughelli North'), ('Ughelli South', 'Ughelli South'), 
                    ('Ukwuani', 'Ukwuani'), ('Uvwie', 'Uvwie'), ('Warri North', 'Warri North'), ('Warri South', 'Warri South'), 
                    ('Warri South West', 'Warri South West'),
                    #local governments in ebonyi state#
                    ('Abakaliki', 'Abakaliki'), ('Afikpo North', 'Afikpo North'), ('Afikpo South', 'Afikpo South'), ('Ebonyi', 'Ebonyi'), 
                    ('Ezza North', 'Ezza North'), ('Ezza South', 'Ezza South'), ('Ikwo', 'Ikwo'), ('Ishielu', 'Ishielu'), ('Ivo', 'Ivo'), 
                    ('Izzi', 'Izzi'), ('Ohaozara', 'Ohaozara'), ('Ohaukwu', 'Ohaukwu'), ('Onicha', 'Onicha'),
                    #local governments in edo state#
                    ('Akoko-Edo', 'Akoko-Edo'), ('Egor', 'Egor'), ('Esan Central', 'Esan Central'), ('Esan North-East', 'Esan North-East'), 
                    ('Esan South-East', 'Esan South-East'), ('Esan West', 'Esan West'), ('Etsako Central', 'Etsako Central'), 
                    ('Etsako East', 'Etsako East'), ('Etsako West', 'Etsako West'), ('Igueben', 'Igueben'), ('Ikpoba Okha', 'Ikpoba Okha'), 
                    ('Orhionmwon', 'Orhionmwon'), ('Oredo', 'Oredo'), ('Ovia North-East', 'Ovia North-East'), ('Ovia South-West', 'Ovia South-West'), 
                    ('Owan East', 'Owan East'), ('Owan West', 'Owan West'), ('Uhunmwonde', 'Uhunmwonde'),
                    #local governments in ekiti state#
                    ('Ado Ekiti', 'Ado Ekiti'), ('Efon', 'Efon'), ('Ekiti East', 'Ekiti East'), ('Ekiti South-West', 'Ekiti South-West'), 
                    ('Ekiti West', 'Ekiti West'), ('Emure', 'Emure'), ('Gbonyin', 'Gbonyin'), ('Ido Osi', 'Ido Osi'), ('Ijero', 'Ijero'), 
                    ('Ikere', 'Ikere'), ('Ikole', 'Ikole'), ('Ilejemeje', 'Ilejemeje'), ('Irepodun-Ifelodun', 'Irepodun-Ifelodun'), 
                    ('Ise-Orun', 'Ise-Orun'), ('Moba', 'Moba'), ('Oye', 'Oye'),
                    #local governments in rivers state#
                    ('Port Harcourt', 'Port Harcourt'), ('Obio-Akpor', 'Obio-Akpor'), ('Okrika', 'Okrika'), ('Ogu–Bolo', 'Ogu–Bolo'), 
                    ('Eleme', 'Eleme'), ('Tai', 'Tai'), ('Gokana', 'Gokana'), ('Khana', 'Khana'), ('Oyigbo', 'Oyigbo'), 
                    ('Opobo–Nkoro', 'Opobo–Nkoro'), ('Andoni', 'Andoni'), ('Bonny', 'Bonny'), ('Degema', 'Degema'), ('Asari-Toru', 'Asari-Toru'), 
                    ('Akuku-Toru', 'Akuku-Toru'), ('Abua–Odual', 'Abua–Odual'), ('Ahoada West', 'Ahoada West'), ('Ahoada East', 'Ahoada East'), 
                    ('Ogba–Egbema–Ndoni', 'Ogba–Egbema–Ndoni'), ('Emohua', 'Emohua'), ('Ikwerre', 'Ikwerre'), ('Etche', 'Etche'), ('Omuma', 'Omuma'),
                    #local governments in enugu state#
                    ('Aninri', 'Aninri'), ('Awgu', 'Awgu'), ('Enugu East', 'Enugu East'), ('Enugu North', 'Enugu North'), 
                    ('Enugu South', 'Enugu South'), ('Ezeagu', 'Ezeagu'), ('Igbo Etiti', 'Igbo Etiti'), ('Igbo Eze North', 'Igbo Eze North'), 
                    ('Igbo Eze South', 'Igbo Eze South'), ('Isi Uzo', 'Isi Uzo'), ('Nkanu East', 'Nkanu East'), ('Nkanu West', 'Nkanu West'), 
                    ('Nsukka', 'Nsukka'), ('Oji River', 'Oji River'), ('Udenu', 'Udenu'), ('Udi', 'Udi'), ('Uzo Uwani', 'Uzo Uwani'), 
                    #local governments in FCT#
                    ('Abaji', 'Abaji'), ('Bwari', 'Bwari'), ('Gwagwalada', 'Gwagwalada'), ('Kuje', 'Kuje'), ('Kwali', 'Kwali'), ('Municipal Area Council', 'Municipal Area Council'),
                    #local governments in gombe state#
                    ('Akko', 'Akko'), ('Balanga', 'Balanga'), ('Billiri', 'Billiri'), ('Dukku', 'Dukku'), ('Funakaye', 'Funakaye'), 
                    ('Gombe', 'Gombe'), ('Kaltungo', 'Kaltungo'), ('Kwami', 'Kwami'), ('Nafada', 'Nafada'), ('Shongom', 'Shongom'), 
                    ('Yamaltu-Deba', 'Yamaltu-Deba'),
                    #local governments in imo state#
                    ('Aboh Mbaise', 'Aboh Mbaise'), ('Ahiazu Mbaise', 'Ahiazu Mbaise'), ('Ehime Mbano', 'Ehime Mbano'), 
                    ('Ezinihitte', 'Ezinihitte'), ('Ideato North', 'Ideato North'), ('Ideato South', 'Ideato South'), ('Ihitte-Uboma', 'Ihitte-Uboma'), 
                    ('Ikeduru', 'Ikeduru'), ('Isiala Mbano', 'Isiala Mbano'), ('Isu', 'Isu'), ('Mbaitoli', 'Mbaitoli'), ('Ngor Okpala', 'Ngor Okpala'), 
                    ('Njaba', 'Njaba'), ('Nkwerre', 'Nkwerre'), ('Nwangele', 'Nwangele'), ('Obowo', 'Obowo'), ('Oguta', 'Oguta'), 
                    ('Ohaji-Egbema', 'Ohaji-Egbema'), ('Okigwe', 'Okigwe'), ('Orlu', 'Orlu'), ('Orsu', 'Orsu'), ('Oru East', 'Oru East'), 
                    ('Oru West', 'Oru West'), ('Owerri Municipal', 'Owerri Municipal'), ('Owerri North', 'Owerri North'), 
                    ('Owerri West', 'Owerri West'), ('Unuimo', 'Unuimo'),
                    #local governments in jigawa state#
                    ('Auyo', 'Auyo'), ('Babura', 'Babura'), ('Biriniwa', 'Biriniwa'), ('Birnin Kudu', 'Birnin Kudu'), ('Buji', 'Buji'), 
                    ('Dutse', 'Dutse'), ('Gagarawa', 'Gagarawa'), ('Garki', 'Garki'), ('Gumel', 'Gumel'), ('Guri', 'Guri'), ('Gwaram', 'Gwaram'), 
                    ('Gwiwa', 'Gwiwa'), ('Hadejia', 'Hadejia'), ('Jahun', 'Jahun'), ('Kafin Hausa', 'Kafin Hausa'), ('Kazaure', 'Kazaure'), 
                    ('Kiri Kasama', 'Kiri Kasama'), ('Kiyawa', 'Kiyawa'), ('Kaugama', 'Kaugama'), ('Maigatari', 'Maigatari'), 
                    ('Malam Madori', 'Malam Madori'), ('Miga', 'Miga'), ('Ringim', 'Ringim'), ('Roni', 'Roni'), ('Sule Tankarkar', 'Sule Tankarkar'), 
                    ('Taura', 'Taura'), ('Yankwashi', 'Yankwashi'),
                    #local governments in kaduna state#
                    ('Birnin Gwari', 'Birnin Gwari'), ('Chikun', 'Chikun'), ('Giwa', 'Giwa'), ('Igabi', 'Igabi'), ('Ikara', 'Ikara'), ('Jaba', 'Jaba'), 
                    ('Jema a', 'Jema a'), ('Kachia', 'Kachia'), ('Kaduna North', 'Kaduna North'), ('Kaduna South', 'Kaduna South'), 
                    ('Kagarko', 'Kagarko'), ('Kajuru', 'Kajuru'), ('Kaura', 'Kaura'), ('Kauru', 'Kauru'), ('Kubau', 'Kubau'), ('Kudan', 'Kudan'), 
                    ('Lere', 'Lere'), ('Makarfi', 'Makarfi'), ('Sabon Gari', 'Sabon Gari'), ('Sanga', 'Sanga'), ('Soba', 'Soba'), 
                    ('Zangon Kataf', 'Zangon Kataf'), ('Zaria', 'Zaria'),
                    #local governments in kano state#
                    ('Ajingi', 'Ajingi'), ('Albasu', 'Albasu'), ('Bagwai', 'Bagwai'), ('Bebeji', 'Bebeji'), ('Bichi', 'Bichi'), ('Bunkure', 'Bunkure'), 
                    ('Dala', 'Dala'), ('Dambatta', 'Dambatta'), ('Dawakin Kudu', 'Dawakin Kudu'), ('Dawakin Tofa', 'Dawakin Tofa'), 
                    ('Doguwa', 'Doguwa'), ('Fagge', 'Fagge'), ('Gabasawa', 'Gabasawa'), ('Garko', 'Garko'), ('Garun Mallam', 'Garun Mallam'), 
                    ('Gaya', 'Gaya'), ('Gezawa', 'Gezawa'), ('Gwale', 'Gwale'), ('Gwarzo', 'Gwarzo'), ('Kabo', 'Kabo'), ('Kano Municipal', 'Kano Municipal'), 
                    ('Karaye', 'Karaye'), ('Kibiya', 'Kibiya'), ('Kiru', 'Kiru'), ('Kumbotso', 'Kumbotso'), ('Kunchi', 'Kunchi'), ('Kura', 'Kura'), 
                    ('Madobi', 'Madobi'), ('Makoda', 'Makoda'), ('Minjibir', 'Minjibir'), ('Nasarawa', 'Nasarawa'), ('Rano', 'Rano'), ('Rimin Gado', 'Rimin Gado'), 
                    ('Rogo', 'Rogo'), ('Shanono', 'Shanono'), ('Sumaila', 'Sumaila'), ('Takai', 'Takai'), ('Tarauni', 'Tarauni'), ('Tofa', 'Tofa'), 
                    ('Tsanyawa', 'Tsanyawa'), ('Tudun Wada', 'Tudun Wada'), ('Ungogo', 'Ungogo'), ('Warawa', 'Warawa'), ('Wudil', 'Wudil'),
                    #local governments in katsina state#
                    ('Bakori', 'Bakori'), ('Batagarawa', 'Batagarawa'), ('Batsari', 'Batsari'), ('Baure', 'Baure'), ('Bindawa', 'Bindawa'), 
                    ('Charanchi', 'Charanchi'), ('Dandume', 'Dandume'), ('Danja', 'Danja'), ('Dan Musa', 'Dan Musa'), ('Daura', 'Daura'), 
                    ('Dutsi', 'Dutsi'), ('Dutsin Ma', 'Dutsin Ma'), ('Faskari', 'Faskari'), ('Funtua', 'Funtua'), ('Ingawa', 'Ingawa'), 
                    ('Jibia', 'Jibia'), ('Kafur', 'Kafur'), ('Kaita', 'Kaita'), ('Kankara', 'Kankara'), ('Kankia', 'Kankia'), ('Katsina', 'Katsina'),
                    ('Kurfi', 'Kurfi'), ('Kusada', 'Kusada'), ('Mai Adua', 'Mai Adua'), ('Malumfashi', 'Malumfashi'), ('Mani', 'Mani'), 
                    ('Mashi', 'Mashi'), ('Matazu', 'Matazu'), ('Musawa', 'Musawa'), ('Rimi', 'Rimi'), ('Sabuwa', 'Sabuwa'), ('Safana', 'Safana'), 
                    ('Sandamu', 'Sandamu'), ('Zango', 'Zango'),
                    #local governments in kebbi state#
                    ('Aleiro', 'Aleiro'), ('Arewa Dandi', 'Arewa Dandi'), ('Argungu', 'Argungu'), ('Augie', 'Augie'), ('Bagudo', 'Bagudo'), 
                    ('Birnin Kebbi', 'Birnin Kebbi'), ('Bunza', 'Bunza'), ('Dandi', 'Dandi'), ('Fakai', 'Fakai'), ('Gwandu', 'Gwandu'), 
                    ('Jega', 'Jega'), ('Kalgo', 'Kalgo'), ('Koko Besse', 'Koko Besse'), ('Maiyama', 'Maiyama'), ('Ngaski', 'Ngaski'), 
                    ('Sakaba', 'Sakaba'), ('Shanga', 'Shanga'), ('Suru', 'Suru'), ('Wasagu Danko', 'Wasagu Danko'), ('Yauri', 'Yauri'), 
                    ('Zuru', 'Zuru'),
                    #local governments in kogi state#
                    ('Adavi', 'Adavi'), ('Ajaokuta', 'Ajaokuta'), ('Ankpa', 'Ankpa'), ('Bassa', 'Bassa'), ('Dekina', 'Dekina'), 
                    ('Ibaji', 'Ibaji'), ('Idah', 'Idah'), ('Igalamela Odolu', 'Igalamela Odolu'), ('Ijumu', 'Ijumu'), 
                    ('Kabba Bunu', 'Kabba Bunu'), ('Kogi', 'Kogi'), ('Lokoja', 'Lokoja'), ('Mopa Muro', 'Mopa Muro'), ('Ofu', 'Ofu'), 
                    ('Ogori Magongo', 'Ogori Magongo'), ('Okehi', 'Okehi'), ('Okene', 'Okene'), ('Olamaboro', 'Olamaboro'), ('Omala', 'Omala'), 
                    ('Yagba East', 'Yagba East'), ('Yagba West', 'Yagba West'),
                    #local governments in kwara state#
                    ('Asa', 'Asa'), ('Baruten', 'Baruten'), ('Edu', 'Edu'), ('Ekiti', 'Ekiti'), ('Ifelodun', 'Ifelodun'), 
                    ('Ilorin East', 'Ilorin East'), ('Ilorin South', 'Ilorin South'), ('Ilorin West', 'Ilorin West'), ('Irepodun', 'Irepodun'), 
                    ('Isin', 'Isin'), ('Kaiama', 'Kaiama'), ('Moro', 'Moro'), ('Offa', 'Offa'), ('Oke Ero', 'Oke Ero'), ('Oyun', 'Oyun'), 
                    ('Pategi', 'Pategi'),
                    #local governments in Lagos state#
                    ('Agege', 'Agege'), ('Ajeromi-Ifelodun', 'Ajeromi-Ifelodun'), ('Alimosho', 'Alimosho'), ('Amuwo-Odofin', 'Amuwo-Odofin'), 
                    ('Apapa', 'Apapa'), ('Badagry', 'Badagry'), ('Epe', 'Epe'), ('Eti Osa', 'Eti Osa'), ('Ibeju-Lekki', 'Ibeju-Lekki'), 
                    ('Ifako-Ijaiye', 'Ifako-Ijaiye'), ('Ikeja', 'Ikeja'), ('Ikorodu', 'Ikorodu'), ('Kosofe', 'Kosofe'), 
                    ('Lagos Island', 'Lagos Island'), ('Lagos Mainland', 'Lagos Mainland'), ('Mushin', 'Mushin'), ('Ojo', 'Ojo'), 
                    ('Oshodi-Isolo', 'Oshodi-Isolo'), ('Shomolu', 'Shomolu'), ('Surulere', 'Surulere'),
                    #local governments in nasarawa state#
                    ('Akwanga', 'Akwanga'), ('Awe', 'Awe'), ('Doma', 'Doma'), ('Karu', 'Karu'), ('Keana', 'Keana'), ('Keffi', 'Keffi'), ('Kokona', 'Kokona'), 
                    ('Lafia', 'Lafia'), ('Nasarawa', 'Nasarawa'), ('Nasarawa Egon', 'Nasarawa Egon'), ('Obi', 'Obi'), ('Toto', 'Toto'), ('Wamba', 'Wamba'),
                    #local governments in niger state#
                    ('Agaie', 'Agaie'), ('Agwara', 'Agwara'), ('Bida', 'Bida'), ('Borgu', 'Borgu'), ('Bosso', 'Bosso'), ('Chanchaga', 'Chanchaga'), 
                    ('Edati', 'Edati'), ('Gbako', 'Gbako'), ('Gurara', 'Gurara'), ('Katcha', 'Katcha'), ('Kontagora', 'Kontagora'), 
                    ('Lapai', 'Lapai'), ('Lavun', 'Lavun'), ('Magama', 'Magama'), ('Mariga', 'Mariga'), ('Mashegu', 'Mashegu'), ('Mokwa', 'Mokwa'), 
                    ('Moya', 'Moya'), ('Paikoro', 'Paikoro'), ('Rafi', 'Rafi'), ('Rijau', 'Rijau'), ('Shiroro', 'Shiroro'), ('Suleja', 'Suleja'), 
                    ('Tafa', 'Tafa'), ('Wushishi', 'Wushishi'),
                    #local governments in ogun state#
                    ('Abeokuta North', 'Abeokuta North'), ('Abeokuta South', 'Abeokuta South'), ('Ado-Odo Ota', 'Ado-Odo Ota'), 
                    ('Egbado North', 'Egbado North'), ('Egbado South', 'Egbado South'), ('Ewekoro', 'Ewekoro'), ('Ifo', 'Ifo'), 
                    ('Ijebu East', 'Ijebu East'), ('Ijebu North', 'Ijebu North'), ('Ijebu North East', 'Ijebu North East'), 
                    ('Ijebu Ode', 'Ijebu Ode'), ('Ikenne', 'Ikenne'), ('Imeko Afon', 'Imeko Afon'), ('Ipokia', 'Ipokia'), 
                    ('Obafemi Owode', 'Obafemi Owode'), ('Odeda', 'Odeda'), ('Odogbolu', 'Odogbolu'), ('Ogun Waterside', 'Ogun Waterside'), 
                    ('Remo North', 'Remo North'), ('Shagamu', 'Shagamu'),
                    #local governments in ondo state#
                    ('Akoko North-East', 'Akoko North-East'), ('Akoko North-West', 'Akoko North-West'), ('Akoko South-West', 'Akoko South-West'), 
                    ('Akoko South-East', 'Akoko South-East'), ('Akure North', 'Akure North'), ('Akure South', 'Akure South'), ('Ese Odo', 'Ese Odo'), 
                    ('Idanre', 'Idanre'), ('Ifedore', 'Ifedore'), ('Ilaje', 'Ilaje'), ('Ile Oluji-Okeigbo', 'Ile Oluji-Okeigbo'), ('Irele', 'Irele'), 
                    ('Odigbo', 'Odigbo'), ('Okitipupa', 'Okitipupa'), ('Ondo East', 'Ondo East'), ('Ondo West', 'Ondo West'), ('Ose', 'Ose'), ('Owo', 'Owo'),
                    #local governments in osun state#
                    ('Atakunmosa East', 'Atakunmosa East'), ('Atakunmosa West', 'Atakunmosa West'), ('Aiyedaade', 'Aiyedaade'), 
                    ('Aiyedire', 'Aiyedire'), ('Boluwaduro', 'Boluwaduro'), ('Boripe', 'Boripe'), ('Ede North', 'Ede North'), 
                    ('Ede South', 'Ede South'), ('Ife Central', 'Ife Central'), ('Ife East', 'Ife East'), ('Ife North', 'Ife North'), 
                    ('Ife South', 'Ife South'), ('Egbedore', 'Egbedore'), ('Ejigbo', 'Ejigbo'), ('Ifedayo', 'Ifedayo'), ('Ifelodun', 'Ifelodun'), 
                    ('Ila', 'Ila'), ('Ilesa East', 'Ilesa East'), ('Ilesa West', 'Ilesa West'), ('Irepodun', 'Irepodun'), ('Irewole', 'Irewole'), 
                    ('Isokan', 'Isokan'), ('Iwo', 'Iwo'), ('Obokun', 'Obokun'), ('Odo Otin', 'Odo Otin'), ('Ola Oluwa', 'Ola Oluwa'), 
                    ('Olorunda', 'Olorunda'), ('Oriade', 'Oriade'), ('Orolu', 'Orolu'), ('Osogbo', 'Osogbo'),
                    #local governments in oyo state#
                    ('Afijio', 'Afijio'), ('Akinyele', 'Akinyele'), ('Atiba', 'Atiba'), ('Atisbo', 'Atisbo'), ('Egbeda', 'Egbeda'), 
                    ('Ibadan North', 'Ibadan North'), ('Ibadan North-East', 'Ibadan North-East'), ('Ibadan North-West', 'Ibadan North-West'), 
                    ('Ibadan South-East', 'Ibadan South-East'), ('Ibadan South-West', 'Ibadan South-West'), ('Ibarapa Central', 'Ibarapa Central'), 
                    ('Ibarapa East', 'Ibarapa East'), ('Ibarapa North', 'Ibarapa North'), ('Ido', 'Ido'), ('Irepo', 'Irepo'), ('Iseyin', 'Iseyin'), 
                    ('Itesiwaju', 'Itesiwaju'), ('Iwajowa', 'Iwajowa'), ('Kajola', 'Kajola'), ('Lagelu', 'Lagelu'), ('Ogbomosho North', 'Ogbomosho North'), 
                    ('Ogbomosho South', 'Ogbomosho South'), ('Ogo Oluwa', 'Ogo Oluwa'), ('Olorunsogo', 'Olorunsogo'), ('Oluyole', 'Oluyole'), 
                    ('Ona Ara', 'Ona Ara'), ('Orelope', 'Orelope'), ('Ori Ire', 'Ori Ire'), ('Oyo', 'Oyo'), ('Oyo East', 'Oyo East'), 
                    ('Saki East', 'Saki East'), ('Saki West', 'Saki West'),
                    #local governments in plateau state#
                    ('Bokkos', 'Bokkos'), ('Barkin Ladi', 'Barkin Ladi'), ('Bassa', 'Bassa'), ('Jos East', 'Jos East'), ('Jos North', 'Jos North'), 
                    ('Jos South', 'Jos South'), ('Kanam', 'Kanam'), ('Kanke', 'Kanke'), ('Langtang South', 'Langtang South'), 
                    ('Langtang North', 'Langtang North'), ('Mangu', 'Mangu'), ('Mikang', 'Mikang'), ('Pankshin', 'Pankshin'), 
                    ('Qua an Pan', 'Qua an Pan'), ('Riyom', 'Riyom'), ('Shendam', 'Shendam'), ('Wase', 'Wase'),
                    #local governments in sokoto state#
                    ('Binji', 'Binji'), ('Bodinga', 'Bodinga'), ('Dange Shuni', 'Dange Shuni'), ('Gada', 'Gada'), ('Goronyo', 'Goronyo'), 
                    ('Gudu', 'Gudu'), ('Gwadabawa', 'Gwadabawa'), ('Illela', 'Illela'), ('Isa', 'Isa'), ('Kebbe', 'Kebbe'), ('Kware', 'Kware'), 
                    ('Rabah', 'Rabah'), ('Sabon Birni', 'Sabon Birni'), ('Shagari', 'Shagari'), ('Silame', 'Silame'), 
                    ('Sokoto North', 'Sokoto North'), ('Sokoto South', 'Sokoto South'), ('Tambuwal', 'Tambuwal'), ('Tangaza', 'Tangaza'), 
                    ('Tureta', 'Tureta'), ('Wamako', 'Wamako'), ('Wurno', 'Wurno'), ('Yabo', 'Yabo'),
                    #local governments in taraba state#
                    ('Ardo Kola', 'Ardo Kola'), ('Bali', 'Bali'), ('Donga', 'Donga'), ('Gashaka', 'Gashaka'), ('Gassol', 'Gassol'), 
                    ('Ibi', 'Ibi'), ('Jalingo', 'Jalingo'), ('Karim Lamido', 'Karim Lamido'), ('Kumi', 'Kumi'), ('Lau', 'Lau'), 
                    ('Sardauna', 'Sardauna'), ('Takum', 'Takum'), ('Ussa', 'Ussa'), ('Wukari', 'Wukari'), ('Yorro', 'Yorro'), 
                    ('Zing', 'Zing'),
                    #local governments in yobe state#
                    ('Bade', 'Bade'), ('Bursari', 'Bursari'), ('Damaturu', 'Damaturu'), ('Fika', 'Fika'), ('Fune', 'Fune'), ('Geidam', 'Geidam'), 
                    ('Gujba', 'Gujba'), ('Gulani', 'Gulani'), ('Jakusko', 'Jakusko'), ('Karasuwa', 'Karasuwa'), ('Machina', 'Machina'), 
                    ('Nangere', 'Nangere'), ('Nguru', 'Nguru'), ('Potiskum', 'Potiskum'), ('Tarmuwa', 'Tarmuwa'), ('Yunusari', 'Yunusari'), 
                    ('Yusufari', 'Yusufari'),
                    #local governments in zamfara state#
                    ('Anka', 'Anka'), ('Bakura', 'Bakura'), ('Birnin Magaji Kiyaw', 'Birnin Magaji Kiyaw'), ('Bukkuyum', 'Bukkuyum'), ('Bungudu', 'Bungudu'), 
                    ('Gummi', 'Gummi'), ('Gusau', 'Gusau'), ('Kaura Namoda', 'Kaura Namoda'), ('Maradun', 'Maradun'), ('Maru', 'Maru'), 
                    ('Shinkafi', 'Shinkafi'), ('Talata Mafara', 'Talata Mafara'), ('Chafe', 'Chafe'), ('Zurmi', 'Zurmi')
                ])
    marital_status = SelectField(u'Marital Status', choices=[('mar', 'Married'), ('sin', 'Single'), ('widow', 'Widow/Widower'), ('div', 'Divorced')])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone Number', validators=[DataRequired(), Length(min=8, max=20)])
    telephone = StringField('Fixed Number', validators=[Length(min=8, max=20)])
    degree_awarded = SelectField(u'Degree Awarded', coerce=int, choices=[
                                        (1, 'First Degree (e.g. B.Sc, BA, etc)'), 
                                        (2, 'Second Degree (e.g. M.Sc, MBA, etc)'), 
                                        (3, 'Doctorate'), 
                                        (4, 'Post Doctorate')
                                        ], validators=[DataRequired()])
    faculty = StringField('Faculty', validators=[DataRequired(), Length(min=1, max=250)])
    department = StringField('Department', validators=[DataRequired(), Length(min=1, max=500)])
    year_of_grad = StringField('Year of Graduation', validators=[DataRequired(), Length(min=2, max=20)])
    permanent_addr = TextAreaField('Present Permanent Address')
    password = PasswordField('Password', validators=[DataRequired(), Length(min=3)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), Length(min=3), EqualTo('password')])

    submit = SubmitField('Register')

    #fields input validation
    def validate_email(self, email):
        alumni = User.query.filter_by(email=email.data).first()
        if alumni:
            raise ValidationError(f'{self.email.data} already exist, try a different email address')

    def validate_phone(self, phone):
        alumni = User.query.filter_by(phone=phone.data).first()
        if alumni:
            raise ValidationError(f'{self.phone.data} already exist, try a different phone number')

class LoginForm(FlaskForm) :
    email = StringField('E-Mail', validators=[DataRequired(), Email(), Length(max=200)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login') 

class UpdateAccountForm(FlaskForm):
    surname = StringField('Surname', validators=[DataRequired(), Length(min=2, max=100)])
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=100)])
    first_name = StringField('Middle Name', validators=[DataRequired(), Length(min=2, max=100)])
    maiden = StringField('Maiden Name', validators=[DataRequired(), Length(min=2, max=100)])
    dob = StringField('Date of Birth', validators=[DataRequired()])
    gender = SelectField(u'Gender', choices=[('f', 'Female'), ('m', 'Male')])
    state_of_origin = SelectField(u'State of Origin', choices=[('ls', 'List')])
    marital_status = SelectField(u'Marital Status', choices=[('mar', 'Married'), ('sin', 'Single'), ('w', 'Widow'), ('wer', 'Widower'), ('div', 'Divorced')])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone Number', validators=[DataRequired(), Length(min=8, max=20)])
    telephone = StringField('Fixed Number', validators=[Length(min=8, max=20)])
    degree_awarded = StringField('Degree Awarded *(Use abbreviation)*', validators=[DataRequired(), Length(min=2, max=20)])
    faculty = StringField('Faculty', validators=[DataRequired(), Length(min=1, max=250)])
    department = StringField('Department', validators=[DataRequired(), Length(min=1, max=500)])
    year_of_grad = StringField('Year of Graduation', validators=[DataRequired(), Length(min=2, max=20)])
    permanent_addr = TextAreaField('Present Permanent Address')
    
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    #Fields input validation
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError(f'{self.email.data} already exist, try a different email address')

    def validate_phone(self, phone):
        if phone.data != current_user.phone:
            user = User.query.filter_by(phone=phone.data).first()
            if user:
                raise ValidationError(f'{self.phone} already exist, try a different phone address')

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')

class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')
    
    #validates email address
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError(f'There is no account with email: {self.email}. You must register first.')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4)]) 
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), Length(min=4), EqualTo('password')])
    
    submit = SubmitField('Reset Password')

class RecipientForm(FlaskForm):
    
    matric_no = StringField('Matriculation Number', validators=[DataRequired(), Length(min=4, max=50)])
    transcript_type = SelectField(u'Transcript Type', choices=[('grad', 'Graduate'), ('post', 'Post-Graduate')])
    recipient_name = StringField('Institution/Organization Name', 
                                    validators=[DataRequired(), Length(min=3, max=200)])
    country = StringField('Country', validators=[DataRequired(), Length(min=2, max=200)])
    address_line = StringField('Address Line', validators=[DataRequired(), Length(min=10, max=500)])
    shipping_continent = StringField('Shipping Continent', validators=[DataRequired(), Length(min=10, max=100)])
    city = StringField('City/State/Province', validators=[DataRequired(), Length(min=10, max=500)])
    courier = StringField('Preferred Courier', validators=[DataRequired(), Length(min=10, max=500)])
    zip_code = StringField('Zip Code/Post Code', validators=[DataRequired(), Length(min=10, max=500)])
    agree = BooleanField('I agree to the terms of engagement of this transcript')

    submit = SubmitField('Make Payment')